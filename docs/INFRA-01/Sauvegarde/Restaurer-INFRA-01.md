# Restaurer INFRA-01

## Préparer le système

Suivre [Installer INFRA-01](../Installation/Installer-INFRA-01.md) sur une nouvelle
carte SD : Raspberry Pi OS Lite 64 bits, Debian Trixie, Python 3.13 ou supérieur.
Installer Ohana-Installer **1.15.5 ou supérieur** selon le
[guide officiel](https://github.com/cedric-HAOS/Ohana-Installer/blob/main/docs/Installation.md).
Garder le DHCP de la box actif pendant la reconstruction.

Ne pas installer Agent/Vision auparavant : la restauration installe la composition
sauvegardée. Une installation partielle peut également être reprise.

## Depuis iCloud

```bash
sudo ohana restore --icloud --choose-backup
```

Saisir les informations Apple et le code 2FA dans le terminal. Sélectionner la
sauvegarde la plus récente antérieure à la panne, vérifier sa date et ses versions
avant confirmation. Sans `--choose-backup`, Installer sélectionne la dernière
sauvegarde dont le manifeste est valide.

Les sauvegardes sont dans `Ohana/Backups/infra-01`. Si aucune identité age locale
n'existe, Installer récupère automatiquement `Ohana/Recovery/infra-01.agekey`.
Une clé externe peut être fournie avec `--identity /media/usb/ohana-infra-01.agekey`.

Installer vérifie la taille et le SHA-256 de l'archive, la déchiffre et compare
le manifeste au descripteur chiffré. Depuis 1.15.3, le champ `contents` est validé
séparément : inventaire et présence des éléments déclarés sont contrôlés.
Les anciens descripteurs sans ce champ restent compatibles.

## Périmètre restauré

- `/etc/ohana-agent` : infrastructure, plugins et configuration Agent ;
- `/etc/ohana-vision` : configuration Vision ;
- `/etc/dnsmasq.d` : configuration DHCP et réservations présentes dans les fichiers ;
- `/etc/chrony/chrony.conf` : configuration NTP ;
- `/var/lib/ohana-vision/vision.db` : copie cohérente des données Vision.

Les fichiers TLS `ca.key` et `ca.srl` sont exclus. L'archive n'est pas une image
disque : elle ne restaure pas la configuration réseau du système, les baux DHCP
en cours ni les bases d'état Agent sous `/var/lib/ohana-agent`.

Les traitements temporaires restent dans `/run`, obligatoirement en `tmpfs`.
Installer réinstalle la composition sauvegardée, puis restaure les configurations
et la base Vision. Agent, Vision et Chrony sont démarrés ; dnsmasq reste arrêté.

## Depuis une copie locale

```bash
sudo ohana restore \
  --local /media/usb/infra-01-20260813T040000Z \
  --identity /media/usb/ohana-infra-01.agekey
```

## Rétablir le réseau et contrôler les services

Depuis la console du Raspberry, lancer `sudo ohana`, puis **Configurer le réseau
d'INFRA-01** : adresse `192.168.1.10/24`, passerelle `192.168.1.1`, DNS
`192.168.1.11` et `192.168.1.12`, interface Ethernet à vérifier.
Exclure `.10` de la plage DHCP de la box. Confirmer la transaction avant son
retour automatique.

```bash
ip -br address
ip route
sudo systemctl status ohana-agent ohana-vision chrony --no-pager
sudo journalctl -u ohana-agent -u ohana-vision -b -n 100 --no-pager
sudo ohana capability status
```

Ouvrir Vision sur `http://192.168.1.10:8000` et vérifier l'infrastructure,
les configurations et les connexions restaurées.

## Basculer le DHCP

Après validation, désactiver le DHCP de la box, puis lancer :

```bash
sudo ohana capability activate dhcp
```

Contrôler les paramètres d'un nouveau bail sur un client. En cas d'échec,
désactiver d'abord le DHCP d'INFRA-01, puis réactiver celui de la box :

```bash
sudo ohana capability deactivate dhcp
```

Un seul serveur DHCP doit répondre sur le réseau.

## Correctifs publiés après l'incident du 9 octobre

Les évolutions suivantes sont disponibles avec Agent 1.45.1 et Installer 1.15.5
(composition Platform 1.0.141) :

- contrôle d'intégrité SQLite avant application de la base restaurée ;
- retrait des WAL/SHM de l'installation précédente, avec sauvegarde pour retour arrière ;
- rétablissement des propriétaires et permissions des fichiers DHCP administrables ;
- récupération de la clé iCloud même si une installation neuve a créé une clé locale ;
- export/import des autorisations Katsuyu et Shizune dans
  `/etc/ohana-agent/recovery/authorizations.json`, inclus dans l'archive chiffrée.

Ce dernier export contient uniquement les autorisations durables et les inscriptions
push ; les anciens jobs et les demandes d'appairage ne sont pas réintroduits.
Les anciennes sauvegardes sans cet export restent restaurables, mais nécessitent
une nouvelle association des clients. Il faut déployer ces versions Agent/Installer avant d'en bénéficier.
Les anciennes archives ne gagnent pas rétroactivement les autorisations manquantes.

## Vérification MQTT après restauration

Contrôler la résolution de `ha-01.ohana.lan` depuis INFRA-01 et la disponibilité
du broker MQTT. La réservation actuelle de HA-01 est `192.168.1.20`. Si les DNS
locaux ne publient pas ce nom, une entrée locale explicite dans `/etc/hosts`
peut assurer la résolution, à condition de confirmer l'IP dans les réservations.
Sur une image gérée par cloud-init, utiliser `manage_etc_hosts: false` dans un
fichier sous `/etc/cloud/cloud.cfg.d` pour préserver cette entrée.

Cette configuration système ne fait pas partie de l'archive INFRA-01 actuelle.
Une connexion MQTT authentifiée et le topic ciblé `ohana/status` doivent confirmer
Agent en ligne ; l'absence d'erreurs de résolution dans les logs ne suffit pas.

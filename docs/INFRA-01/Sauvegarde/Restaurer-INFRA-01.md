# Restaurer INFRA-01

Installer un système Linux compatible sur la nouvelle machine, copier la clé
privée `age` sur un support externe, puis lancer Ohana-Installer.

## Depuis iCloud

```bash
sudo ohana restore \
  --icloud \
  --identity /media/usb/ohana-infra-01.agekey
```

Installer demande les informations iCloud et le code 2FA si nécessaire. Il
retrouve la dernière sauvegarde complètement publiée, vérifie son intégrité,
compare son manifeste au descripteur contenu dans l'archive chiffrée, installe
la composition Agent/Vision correspondante et restaure les données.

## Depuis une copie locale

```bash
sudo ohana restore \
  --local /media/usb/infra-01-20260813T040000Z \
  --identity /media/usb/ohana-infra-01.agekey
```

Les traitements temporaires ont lieu dans `/run` et sont refusés si ce chemin
n'est pas un `tmpfs`. Après restauration, Agent, Vision et Chrony sont actifs.
dnsmasq reste volontairement arrêté : vérifier que l'ancien serveur DHCP a été
désactivé, puis activer la capacité avec :

```bash
sudo ohana capability activate dhcp
```

Cette séparation évite que deux serveurs DHCP répondent simultanément, quelle
que soit la box, le routeur ou l'ancienne machine qui assurait cette fonction.

# Réplication des noms réservés DHCP vers AdGuard Home

Évolution préparée le 09/10/2026 pour la reconstruction d'INFRA-01.
La préparation dans les dépôts ne constitue pas une installation en production.

## Périmètre

INFRA-01 conserve l'autorité sur les réservations DHCP et leurs noms dans
`ohana.lan`. ZWAVE-01 reste l'origine de la configuration AdGuard Home, répliquée
vers LINKY-01. ESP-03 conserve ses températures piscine ; son futur DHCP de
secours ne fait pas partie de ce changement.

Chaque cycle du service `adguardhome-sync` effectue, dans cet ordre :

1. Lecture des réservations administrées par Ohana-Agent, création ou mise à jour
   des réécritures correspondantes sur ZWAVE-01, puis vérification par son API.
2. Réplication habituelle ZWAVE-01 → LINKY-01 avec le binaire `adguardhome-sync`.
3. Comparaison des réécritures des deux instances par leurs API. Une divergence
   fait échouer le service, même si le binaire de réplication retourne zéro.

Un timer systemd lance le cycle une minute après le démarrage, puis toutes les
cinq minutes. systemd empêche deux exécutions simultanées du même service.
Un échec de la première étape empêche la réplication de ce cycle ; les réponses
déjà présentes dans AdGuard sont conservées. Le prochain déclenchement réessaie.

## Source des noms

Le lecteur DHCP existant d'Ohana-Agent est réutilisé. Les cinq fichiers suivants
doivent exister, même lorsqu'une catégorie ne contient aucune réservation :

- `/etc/dnsmasq.d/10-infrastructure.conf`
- `/etc/dnsmasq.d/20-serveurs.conf`
- `/etc/dnsmasq.d/30-infrastructure-reseau.conf`
- `/etc/dnsmasq.d/40-passerelles-domotiques.conf`
- `/etc/dnsmasq.d/50-equipements-critiques.conf`

`00-ohana.conf` doit déclarer le domaine `ohana.lan`. Les chemins correspondent
à l'installation standard ; une installation avec des chemins personnalisés
nécessite une adaptation avant activation.

Une réservation `ha-01,192.168.1.20` produit une réécriture exacte
`ha-01.ohana.lan → 192.168.1.20`. Les réservations portant déjà un FQDN dans
`ohana.lan` sont acceptées sans ajouter deux fois le suffixe. Les noms d'un autre
domaine, invalides ou ambigus font échouer le cycle avant toute mutation.

Le fichier des baux dynamiques n'est jamais lu. Aucun wildcard n'est créé.
Les machines à IP statique sans réservation, notamment INFRA-01, ne sont pas
ajoutées par ce mécanisme : conserver leurs réécritures manuelles si nécessaires.

## Préservation des règles existantes

Le registre `/etc/ohana-agent/adguard-reservations-state.json` suit les couples
nom/adresse gérés. Seuls ces couples peuvent être supprimés quand une réservation
change ou disparaît. Les règles manuelles sans rapport sont préservées, y compris
dans `ohana.lan`. Une règle identique à une réservation est adoptée dans le registre.
Une règle manuelle différente pour un nom réservé bloque le cycle ; résoudre le
conflit avant activation, sans effacement automatique.

Le registre journalise les opérations avant leur envoi : après un timeout ou une
interruption, le prochain cycle vérifie l'état distant et reprend sans perdre la
trace d'une règle ajoutée. Un cycle sans changement ne réécrit pas le registre.
Ne pas supprimer ce fichier : les anciennes règles perdraient leur suivi.

## Installation lors de la reconstruction

Après restauration, installer Ohana-Agent **1.45.0 ou ultérieur**, contenant la commande
`/opt/ohana-agent/venv/bin/ohana-agent-adguard-reservations`, puis le binaire
`/opt/adguardhome-sync/adguardhome-sync`. Ohana-Installer ne pose pas automatiquement
les unités ci-dessous : les installer depuis ce dépôt.

Depuis la racine d'Ohana-House sur INFRA-01 :

```bash
sudo install -o root -g ohana-agent -m 640 config/adguardhome-sync/adguardhome-sync.example.yaml /etc/ohana-agent/adguardhome-sync.yaml
sudo nano /etc/ohana-agent/adguardhome-sync.yaml
sudo install -m 644 config/adguardhome-sync/adguardhome-sync.service /etc/systemd/system/adguardhome-sync.service
sudo install -m 644 config/adguardhome-sync/adguardhome-sync.timer /etc/systemd/system/adguardhome-sync.timer
sudo systemctl daemon-reload
```

Renseigner les deux mots de passe dans le fichier protégé. Les modèles utilisent
les adresses cibles ZWAVE-01 `192.168.1.11` et LINKY-01 `192.168.1.12` : vérifier
les adresses réellement déployées et adapter les URL avant activation.
Conserver `dns.rewrites: true`,
`dhcp.serverConfig: false` et `dhcp.staticLeases: false`. Le DHCP AdGuard n'est
pas activé. Conserver `cron: ""` et `api.port: 0` : le timer pilote le cycle complet.

La configuration et le registre sont protégés en `root:ohana-agent`, mode `0640`,
pour permettre à l'Agent de les lire lors de la sauvegarde chiffrée. Le service
s'exécute comme root avec le groupe primaire `ohana-agent`. Vérifier les droits
après restauration ou transfert d'une ancienne configuration.

Si une ancienne installation existe, arrêter et désactiver son service avant
de remplacer l'unité. Transférer ses identifiants vers le nouveau fichier ;
ne pas conserver une deuxième copie non sauvegardée sous `/opt`.

Prévisualiser les nombres d'ajouts et de suppressions, sans mutation :

```bash
sudo /opt/ohana-agent/venv/bin/ohana-agent-adguard-reservations --dry-run
```

Lancer un cycle, puis consulter son résultat :

```bash
sudo systemctl start adguardhome-sync.service
systemctl status adguardhome-sync.service
journalctl -u adguardhome-sync.service -n 50 --no-pager
```

Une unité `oneshot` terminée correctement est `inactive (dead)` avec
`Result=success` ; elle n'est pas un daemon `active (running)`.
Activer ensuite la planification :

```bash
sudo systemctl enable --now adguardhome-sync.timer
systemctl list-timers adguardhome-sync.timer
```

Vérifier sur chaque DNS un vrai nom réservé :

```bash
dig @192.168.1.11 ha-01.ohana.lan A
dig @192.168.1.12 ha-01.ohana.lan A
```

La comparaison API prouve la présence des règles ; les requêtes DNS prouvent
leur utilisation effective. Vérifier que les réécritures sont activées dans
AdGuard Home. Adapter l'exemple au nom réellement réservé. Les noms déjà copiés
continuent d'être résolus par AdGuard pendant une panne d'INFRA-01 ; les changements
de réservations attendent son retour.

## Sauvegarde et restauration

### Ancienne sauvegarde : ordre impératif

Le restaurateur installe la composition exacte indiquée dans le manifeste de
la sauvegarde. Installer le nouvel Agent avant restauration ne garantit donc
pas sa conservation : la restauration peut réinstaller l'ancien Agent.

1. Reconstruire Debian et préparer Ohana-Installer sur la nouvelle carte SD.
2. Restaurer la sauvegarde iCloud avec sa clé privée `age`, en laissant le
   nouveau timer DNS désactivé. La restauration remet les versions sauvegardées
   et laisse volontairement dnsmasq désactivé.
3. Mettre à jour vers Platform **1.0.140** (`ohana update --platform-version 1.0.140`)
   après restauration. Vérifier Agent 1.45.0 et la présence de sa nouvelle commande.
4. Contrôler les réservations DHCP restaurées et activer dnsmasq explicitement
   après vérification de l'absence d'un autre DHCP principal.
5. Créer la nouvelle configuration AdGuard protégée, renseigner les accès et les
   adresses réelles, installer les modèles systemd puis exécuter la prévisualisation.
6. Exécuter un cycle manuel et vérifier la résolution sur les deux AdGuard avant
   d'activer le timer. Le registre sera créé à ce premier cycle.

Les anciennes archives restent compatibles : aucun nouveau fichier n'est exigé
pour les restaurer. Ne pas activer le timer avant ces étapes. Une première
synchronisation adopte les règles déjà identiques aux réservations ; les règles
manuelles différentes sur un même nom doivent être examinées avant activation.

La configuration avec les identifiants et le registre sont maintenant placés
sous `/etc/ohana-agent`, déjà inclus dans la sauvegarde logique chiffrée iCloud
et autorisé par le restaurateur. Cela couvre les prochaines sauvegardes seulement.
Les anciennes archives ne contiennent pas ces nouveaux fichiers.

Les binaires et les unités systemd sont reconstruits depuis les logiciels et
les modèles de ce dépôt. Après restauration, préserver le fichier de configuration
et le registre récupérés : ne pas les écraser avec le modèle d'exemple.
Réinstaller les unités, vérifier les accès AdGuard, puis effectuer un cycle manuel
avant de réactiver le timer.

## Retour arrière

Arrêter et désactiver `adguardhome-sync.timer`. Les dernières réécritures restent
dans les deux AdGuard. Restaurer l'ancienne unité de service et sa configuration
pour reprendre la seule réplication AdGuard. Conserver le registre pour pouvoir
reprendre ultérieurement. La suppression des règles gérées n'est pas une étape
automatique du retour arrière.

## Références techniques

- [API officielle AdGuard Home](https://github.com/AdguardTeam/AdGuardHome/blob/master/openapi/openapi.yaml)
- [adguardhome-sync](https://github.com/bakito/adguardhome-sync)
- Modèles : `config/adguardhome-sync/`
- Implémentation : Ohana-Agent, `src/ohana_agent/host/adguard_reservations.py`

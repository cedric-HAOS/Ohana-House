# Roadmap

## Versions documentaires

### Naruto v1.0 — historique

Premier dossier d'exploitation : inventaire, procédures, sauvegarde,
restauration et reconstruction.

### Hashirama v2.0 — stable

- architecture de référence ;
- modèle Mission → Capacité → Implémentation ;
- rôle INFRA-01 ;
- DHCP, DNS et NTP résilients ;
- politique d'adressage ;
- conventions de nommage ;
- ADR-001 à ADR-007 ;
- séparation entre état actuel et architecture cible.

## Migrations effectuées

- [x] valider dnsmasq sur INFRA-01 après redémarrage ;
- [x] désactiver définitivement le DHCP Freebox après validation ;
- [x] confirmer la stratégie DNS principale/secondaire ;
- [x] décider de la renumérotation ZWAVE-01 `.11`, LINKY-01 `.12` et HA-01 `.20` ;

## Migrations restantes

- [ ] compléter les procédures de sauvegarde et de restauration d'INFRA-01 ;
- [ ] maintenir l'inventaire Shelly dans Agent et House.

## Produits logiciels

Ohana-Agent, Ohana-Vision, Ohana-Installer et Ohana-Platform disposent de leurs
propres roadmaps. Ils ne sont pas une « v3 » d'Ohana-House.

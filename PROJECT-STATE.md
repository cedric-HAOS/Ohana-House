# État du projet

## Version documentaire stable

**v2.0 — Hashirama**

L'architecture de référence, les conventions et les ADR fondateurs sont
validés. Naruto v1.0 reste l'historique du premier dossier d'exploitation.

## État du déploiement

| Élément | État |
|---|---|
| Architecture de référence | validée |
| Conventions et ADR-001 à ADR-007 | validés |
| INFRA-01 | déployé en `192.168.1.10` |
| Ohana-Agent / Vision | disponibles dans l'écosystème Ohana |
| Bascule DHCP vers INFRA-01 | à valider définitivement |
| Renumérotation ZWAVE-01 / LINKY-01 / HA-01 | non réalisée |
| Documentation état actuel / cible | consolidée |

## Prochain jalon

Valider le fonctionnement de dnsmasq sur INFRA-01 après redémarrage, désactiver
le DHCP Freebox, puis décider si la renumérotation cible `.11`, `.12` et `.20`
est encore utile.

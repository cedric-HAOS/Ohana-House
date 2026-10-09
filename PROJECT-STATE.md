# État du projet

## Version documentaire stable

**v2.2.0 — Reconstruction et réservations DNS**

L'architecture de référence, les conventions et les ADR fondateurs sont
validés. Naruto v1.0 reste l'historique du premier dossier d'exploitation.

## État du déploiement

| Élément | État |
|---|---|
| Architecture de référence | validée |
| Conventions et ADR-001 à ADR-007 | validés |
| INFRA-01 | carte SD HS signalée le 09/10/2026 ; reconstruction requise |
| Ohana-Agent / Vision | disponibles dans l'écosystème Ohana |
| Bascule DHCP vers INFRA-01 | à valider définitivement |
| Renumérotation ZWAVE-01 / LINKY-01 / HA-01 | non réalisée |
| Documentation état actuel / cible | consolidée |

## Prochain jalon

Restaurer la sauvegarde iCloud sur une nouvelle carte, mettre à jour les
composants restaurés, puis configurer et valider la réplication des réservations
DHCP vers ZWAVE-01 et LINKY-01. Les adresses effectives des deux AdGuard doivent
être vérifiées avant de renseigner les modèles, qui utilisent les adresses cibles.
ESP-03 demeure le futur DHCP de secours en conservant les températures piscine.

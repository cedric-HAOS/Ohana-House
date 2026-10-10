# État du projet

## Version documentaire stable

**2.2.1 — Reconstruction et réservations DNS.** Hashirama v2.0 est la baseline
architecturale ; Naruto v1.0 reste l'historique du premier dossier d'exploitation.
Les corrections documentaires du 10 octobre sont encore non publiées.

## Dernier état documenté

| Élément | État et source |
|---|---|
| Architecture, conventions et ADR-001 à ADR-007 | Validés dans le dossier House |
| INFRA-01 | Incident SD du 09/10, puis cycle DNS réussi à 16:57 ; recette globale de reprise à consigner |
| Réplication AdGuard | 38 noms vérifiés sur les deux DNS le 09/10 ; timer et panne à confirmer |
| Ohana-Agent / Vision | Versions locales dans leurs dépôts ; versions réellement installées à relever |
| DHCP principal | Jalon historique coché ; nouveau bail et exclusivité après reconstruction à confirmer |
| Adressage | HA-01 .20 confirmé par DNS le 09/10 ; inventaire des autres adresses à actualiser |
| ESP-03 | Prototype local non publié ; aucune qualification matérielle ni activation déduite |

Les preuves et leurs limites sont centralisées dans [Etat-Actuel.md](Etat-Actuel.md)
et le [CHANGELOG](CHANGELOG.md). Une correction documentaire ne confirme pas
l'état courant de production.

## Prochain jalon

Renseigner [Validation finale](Validation-Finale.md) après les contrôles de reprise :
services, versions, DHCP/NTP, cycle DNS/timer, MQTT, iCloud et autorisations des
clients. Actualiser l'inventaire daté. Garder les essais ESP-03 séparés de cette
qualification et conserver les températures piscine.

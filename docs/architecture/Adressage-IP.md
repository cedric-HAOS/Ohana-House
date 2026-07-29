# Adressage IP

| Élément | Valeur |
|---|---|
| Projet | Ohana-House |
| Réseau | 192.168.1.0/24 |
| Passerelle | BOX-01 — 192.168.1.1 |
| Cible DHCP | INFRA-01 — 192.168.1.10 |
| Plage dynamique cible | 192.168.1.100 à 192.168.1.199 |
| Dernière mise à jour | 29/07/2026 |

## Règle de lecture

Les adresses actuelles sont conservées jusqu'à une migration planifiée. Les
adresses cibles Hashirama ne doivent pas être activées en parallèle si elles
créent une collision.

## Adresses actuellement documentées

| Adresse | Identifiant / équipement | Statut |
|---:|---|---|
| 192.168.1.1 | BOX-01 — Freebox Pop | active |
| 192.168.1.2 | robot piscine | réservation |
| 192.168.1.10 | INFRA-01 | active |
| 192.168.1.37 | caméra salon | réservation |
| 192.168.1.40 | Shelly Plug S3 cuisine | réservation |
| 192.168.1.53 | LINKY-01 | active |
| 192.168.1.54 | ZWAVE-01 | active |
| 192.168.1.56 | Shelly Pro EM garage | réservation |
| 192.168.1.71 | KLF200 | réservation |
| 192.168.1.73 | Sunology | réservation |
| 192.168.1.78 | Shelly Pro EM laverie | réservation |
| 192.168.1.81 | Shelly Pro 4 EM | réservation |
| 192.168.1.99 | AP-01 | active |
| 192.168.1.247 | HA-01 — Home Assistant Green | active |

L'ancienne réservation de la caméra de la laverie en `192.168.1.10` est
obsolète : cette adresse appartient désormais à INFRA-01. La caméra doit être
réattribuée avant remise en service.

## Cible Hashirama

| Adresse | Identifiant | Rôle |
|---:|---|---|
| 192.168.1.1 | BOX-01 | passerelle et WireGuard |
| 192.168.1.10 | INFRA-01 | DHCP, NTP et services Ohana |
| 192.168.1.11 | ZWAVE-01 | DNS principal et Z-Wave |
| 192.168.1.12 | LINKY-01 | DNS secondaire et téléinformation |
| 192.168.1.20 | HA-01 | Home Assistant et MQTT |

## DHCP

La cible est un serveur dnsmasq unique sur INFRA-01 avec la plage
`192.168.1.100-192.168.1.199`. Pendant la migration, le DHCP Freebox peut être
réactivé temporairement pour restaurer le réseau, mais les deux serveurs ne
doivent jamais rester actifs simultanément.

Les équipements permanents utilisent une réservation DHCP. INFRA-01 conserve
une adresse statique au niveau du système afin de pouvoir fournir le DHCP après
un redémarrage complet.

## Répartition fonctionnelle cible

| Plage | Usage cible |
|---|---|
| `.1` | BOX-01 |
| `.2-.9` | réserve infrastructure |
| `.10-.19` | services d'infrastructure |
| `.20-.29` | serveurs domotiques |
| `.30-.39` | réseau et caméras |
| `.40-.99` | passerelles et équipements critiques |
| `.100-.199` | DHCP dynamique |
| `.200-.254` | réserve et adresses historiques en migration |

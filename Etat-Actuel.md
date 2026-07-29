# État actuel de l'infrastructure

Dernière consolidation : 29 juillet 2026.

Ce document sépare les éléments déjà déployés de la cible Hashirama. Il ne
remplace pas la configuration opérationnelle d'Ohana-Agent.

## Déployé

| Identifiant | Équipement | Adresse actuelle | Rôle principal |
|---|---|---:|---|
| BOX-01 | Freebox Pop | 192.168.1.1 | passerelle Internet et WireGuard |
| INFRA-01 | serveur Debian | 192.168.1.10 | services d'infrastructure et Ohana |
| LINKY-01 | Raspberry Pi Linky | 192.168.1.53 | téléinformation MQTT |
| ZWAVE-01 | Raspberry Pi Z-Wave | 192.168.1.54 | Z-Wave JS UI |
| AP-01 | Linksys LAPAC1750 | 192.168.1.99 | accès Wi-Fi |
| HA-01 | Home Assistant Green | 192.168.1.247 | Home Assistant et Mosquitto |
| DHCP | dnsmasq préparé sur INFRA-01 ; bascule finale à valider | INFRA-01, plage `.100-.199` |
| NTP | prévu sur INFRA-01 | INFRA-01 |
| DNS | services AdGuard sur les Raspberry Pi | ZWAVE-01 principal, LINKY-01 secondaire |
| WireGuard | terminaison Freebox | BOX-01 |
| Supervision | Agent et Vision installables | Agent source de vérité, Vision projection |

Le réseau physique utilise SW-01 et SW-02 comme switchs TRENDnet, puis SW-03
pour les équipements domotiques.

## Adresses cibles Hashirama

| Identifiant | Adresse cible |
|---|---:|
| BOX-01 | 192.168.1.1 |
| INFRA-01 | 192.168.1.10 |
| ZWAVE-01 | 192.168.1.11 |
| LINKY-01 | 192.168.1.12 |
| HA-01 | 192.168.1.20 |

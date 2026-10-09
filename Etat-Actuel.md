# État actuel de l'infrastructure

Dernière mise à jour : 9 octobre 2026.

## Incident INFRA-01 et choix confirmés

La carte SD d'INFRA-01 est signalée HS ; sa sauvegarde est disponible dans le
cloud selon l'opérateur. Le contenu de l'archive n'a pas été inspecté ici.
La reconstruction et les contrôles des services restent à effectuer.

- INFRA-01 conserve le rôle de DHCP principal et de référence pour `ohana.lan`.
- LINKY-01 et ZWAVE-01 hébergent AdGuard Home ; leur service de synchronisation
  sera réinstallé sur INFRA-01, complété par les seuls noms réservés DHCP.
- ESP-03 est le futur DHCP de secours ESPHome et conserve les températures piscine.

Agent 1.45.0 et les modèles House 2.2.0 préparent cette évolution ; elle n'est pas
encore déployée. Les adresses effectives des AdGuard doivent être vérifiées :
la table ci-dessous est un instantané du 29 juillet, pas une nouvelle mesure.

Ce document sépare les éléments déjà déployés de la cible Hashirama. Il ne
remplace pas la configuration opérationnelle d'Ohana-Agent.

## Dernier inventaire documenté — 29 juillet 2026

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

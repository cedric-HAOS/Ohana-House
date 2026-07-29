# Inventaire de l'infrastructure

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Inventaire |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Objectif

Ce document recense l'ensemble des équipements constituant l'infrastructure informatique et domotique de la maison.

Il constitue la référence utilisée par l'ensemble de la documentation.

Chaque équipement possède un identifiant unique, utilisé dans tous les autres documents.

---

# 2. Convention de nommage

Les équipements sont identifiés selon la convention suivante :

| Préfixe | Signification |
|----------|---------------|
| BOX | Routeur |
| SW | Switch |
| AP | Point d'accès Wi-Fi |
| HA | Home Assistant |
| RPI | Raspberry Pi |

Exemple :

- BOX-01
- SW-01
- AP-01
- HA-01
- LINKY-01

Ces identifiants sont permanents et ne changent pas, même en cas de remplacement du matériel par un modèle équivalent.

---

# 3. Infrastructure réseau

| ID | Équipement | Modèle | Fonction | Criticité |
|----|------------|---------|----------|-----------|
| BOX-01 | Freebox Pop | Freebox Pop | Accès Internet, routage, NAT et WireGuard | ⭐⭐⭐⭐⭐ |
| SW-01 | Switch principal | TRENDnet TEG-S762 | Distribution réseau | ⭐⭐⭐⭐⭐ |
| SW-02 | Switch secondaire | TRENDnet TEG-S762 | Backbone réseau | ⭐⭐⭐⭐ |
| SW-03 | Switch domotique | Linksys 5 ports Gigabit | Réseau domotique | ⭐⭐⭐ |
| AP-01 | Point d'accès Wi-Fi | Linksys LAPAC1750 | Réseau Wi-Fi | ⭐⭐⭐ |
| INFRA-01 | Serveur d'infrastructure | Debian 13 | DHCP, NTP, administration Ohana | ⭐⭐⭐⭐⭐ |

---

# 4. Infrastructure domotique

| ID | Équipement | Modèle | Fonction | Criticité |
|----|------------|---------|----------|-----------|
| HA-01 | Home Assistant Green | Home Assistant Green | Instance principale | ⭐⭐⭐⭐⭐ |
| LINKY-01 | Raspberry Pi Linky | Raspberry Pi 4 | Téléinformation Linky | ⭐⭐ |
| ZWAVE-01 | Raspberry Pi Z-Wave | Raspberry Pi 4 | Z-Wave JS UI | ⭐⭐⭐ |

---

# 5. Services hébergés

| Équipement | Services |
|------------|----------|
| INFRA-01 | dnsmasq, Chrony, Ohana-Agent |
| HA-01 | Home Assistant Core, Mosquitto, Add-ons |
| LINKY-01 | Home Assistant OS, Téléinformation, Publication MQTT, AdGuard Home |
| ZWAVE-01 | Home Assistant OS, Z-Wave JS UI, RaZberry, AdGuard Home |

---

# 6. Documents associés

## Architecture

- Architecture.md
- Topologie-Reseau.md
- Architecture-Logique.md

## Réseau

- Freebox-Pop.md
- Switches.md
- Linksys-LAPAC1750.md

## Home Assistant

- Home-Assistant-Green.md
- RPi-Linky.md
- RPi-ZWave.md

## Services

- Mosquitto.md
- AdGuard.md
- WireGuard.md
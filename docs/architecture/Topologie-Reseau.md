# Topologie réseau

|---------|--------|
| Projet | Ohana-House |
| Document | Topologie réseau |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit la topologie physique du réseau informatique de l'infrastructure **Ohana-House**.

Il présente les équipements réseau, leurs interconnexions ainsi que les capacités des différentes liaisons.

Les configurations des équipements sont documentées dans leurs chapitres respectifs.

---

# 2. Diagramme de référence

Le diagramme officiel de la topologie réseau est :

**DGM-002 – Topologie réseau**

Ce diagramme constitue la référence de l'architecture physique du réseau.

---

# 3. Organisation générale

Le réseau est organisé autour d'un backbone Ethernet reliant l'ensemble des équipements.

La distribution est assurée par trois switchs Ethernet.

Le point d'accès Wi-Fi est connecté au switch principal.

Les équipements domotiques sont regroupés sur un switch Gigabit dédié.

Le Raspberry Pi Linky est connecté en Wi-Fi.

---

# 4. Inventaire des interconnexions

| Origine | Destination | Support | Débit |
|----------|-------------|----------|-------:|
| BOX-01 | SW-01 | Ethernet | 2,5 Gb |
| SW-01 | SW-02 | Ethernet | 10 Gb |
| SW-02 | SW-03 | Ethernet | 1 Gb |
| SW-01 | AP-01 | Ethernet | 1 Gb |
| AP-01 | LINKY-01 | Wi-Fi | 802.11ac |
| SW-03 | HA-01 | Ethernet | 1 Gb |
| SW-03 | ZWAVE-01 | Ethernet | 1 Gb |

---

# 5. Description des équipements réseau

## BOX-01 — Freebox Pop

La Freebox Pop constitue le point d'entrée de l'infrastructure.

Elle assure :

- l'accès Internet ;
- le routage IPv4 / IPv6 ;
- le serveur DHCP ;
- les redirections nécessaires à WireGuard.

---

## SW-01 — Switch principal

Le switch principal constitue le cœur de la distribution réseau.

Il relie :

- la Freebox Pop ;
- le point d'accès Wi-Fi ;
- le backbone 10 Gb vers SW-02.

---

## SW-02 — Switch secondaire

Le second switch TRENDnet prolonge le backbone réseau.

Il assure la liaison vers le switch dédié à l'infrastructure domotique.

---

## SW-03 — Switch domotique

Le switch Linksys Gigabit est exclusivement dédié aux équipements domotiques.

Il relie :

- HA-01 ;
- ZWAVE-01.

---

## AP-01 — Linksys LAPAC1750

Le point d'accès Wi-Fi fournit la connectivité sans fil au Raspberry Pi Linky.

Son interface Ethernet est limitée à 1 Gb/s.

---

# 6. Analyse de la topologie

## Backbone réseau

Les switchs SW-01 et SW-02 sont interconnectés par une liaison Ethernet à 10 Gb/s.

Cette liaison constitue le backbone principal de l'infrastructure.

Elle offre une capacité largement supérieure aux besoins actuels et prépare les évolutions futures.

---

## Réseau domotique

Les équipements HA-01 et ZWAVE-01 sont regroupés sur SW-03.

Leur trafic réseau étant limité, une liaison Gigabit est largement suffisante.

---

## Réseau Wi-Fi

Le Raspberry Pi Linky est connecté au réseau via AP-01.

Cette liaison transporte essentiellement des messages MQTT de faible volume.

Son utilisation n'a donc pas d'impact significatif sur les performances du réseau.

---

## Organisation

L'architecture est organisée selon une logique fonctionnelle et non géographique.

Chaque équipement est positionné selon son rôle dans l'infrastructure.

Cette organisation facilite la compréhension du réseau et son évolution.

---

# 7. Capacités réseau

| Liaison | Capacité maximale |
|----------|------------------:|
| Backbone SW-01 ↔ SW-02 | 10 Gb/s |
| Freebox ↔ SW-01 | 2,5 Gb/s |
| SW-02 ↔ SW-03 | 1 Gb/s |
| SW-01 ↔ AP-01 | 1 Gb/s |
| SW-03 ↔ HA-01 | 1 Gb/s |
| SW-03 ↔ ZWAVE-01 | 1 Gb/s |
| AP-01 ↔ LINKY-01 | Wi-Fi 802.11ac |

---

# 8. Résilience

La topologie a été conçue afin de limiter les impacts d'une panne.

Les principes retenus sont les suivants :

- backbone dédié entre les deux switchs principaux ;
- séparation des fonctions réseau et domotique ;
- équipements critiques connectés en Ethernet ;
- liaison Wi-Fi réservée au Raspberry Pi Linky.

---

# 9. Évolutions prévues

Les évolutions actuellement envisagées sont :

- remplacement éventuel du Raspberry Pi Z-Wave par un Home Assistant Connect ZWAV-2 ;
- ajout d'un NAS ;
- ajout d'un onduleur ;
- ajout de nouveaux équipements réseau.

Ces évolutions ne remettent pas en cause la topologie générale.

---

# 10. Documents associés

## Architecture

- Architecture.md
- Architecture-Logique.md
- Inventaire.md
- Adressage-IP.md

## Réseau

- Freebox-Pop.md
- Switches.md
- Linksys-LAPAC1750.md

## Services

- AdGuard.md
- WireGuard.md

## Diagrammes

- DGM-001 – Architecture physique
- DGM-002 – Topologie réseau

---

Le présent document décrit l'état de référence de la topologie réseau au moment de sa rédaction.

Toute modification de l'architecture physique devra être répercutée dans cette documentation avant sa mise en production.
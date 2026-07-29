# Architecture logique

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Architecture logique |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit l'architecture logique de l'infrastructure **Ohana-House**.

Contrairement à la topologie réseau qui décrit les interconnexions physiques entre les équipements, ce document présente les différents services, leurs responsabilités et leurs interactions.

L'objectif est de comprendre comment les données circulent dans l'infrastructure.

---

# 2. Diagramme de référence

Le diagramme officiel de l'architecture logique est :

**DGM-003 – Architecture logique**

Ce diagramme constitue la référence des échanges entre les différents services.

---

# 3. Vue d'ensemble

L'architecture logique repose sur cinq services principaux :

| Service | Fonction |
|----------|----------|
| Home Assistant | Supervision et automatisations |
| Mosquitto | Broker MQTT |
| Z-Wave JS UI | Gestion du réseau Z-Wave |
| AdGuard Home | Résolution DNS |
| WireGuard | Accès distant sécurisé |

Chaque service est indépendant et possède une responsabilité clairement définie.

---

# 4. Téléinformation

La téléinformation permet la collecte des données du compteur Linky.

Le Raspberry Pi Linky lit les informations du compteur via son interface série.

Les données sont ensuite publiées sur le broker MQTT hébergé sur HA-01.

Home Assistant consomme ensuite ces informations afin d'alimenter les tableaux de bord, les statistiques et les automatisations.

Diagramme associé :

**DGM-004 – Flux MQTT**

Services impliqués :

- Téléinformation série
- Mosquitto
- Home Assistant

Documents associés :

- RPi-Linky.md
- Mosquitto.md
- Home-Assistant-Green.md

---

# 5. Réseau Z-Wave

Le réseau Z-Wave est entièrement géré par le Raspberry Pi Z-Wave.

Le contrôleur RaZberry communique avec les modules radio.

Z-Wave JS UI assure la passerelle entre le contrôleur et Home Assistant.

Home Assistant accède au réseau Z-Wave exclusivement par l'intermédiaire de Z-Wave JS UI.

Diagramme associé :

**DGM-005 – Flux Z-Wave**

Services impliqués :

- Z-Wave JS UI
- Contrôleur RaZberry
- Home Assistant

Documents associés :

- RPi-ZWave.md
- Home-Assistant-Green.md

---

# 6. DNS

La résolution des noms est assurée par deux instances AdGuard Home.

Ces deux serveurs DNS fonctionnent de manière indépendante.

Les clients utilisent les deux serveurs configurés par DHCP.

En cas d'indisponibilité de l'un d'eux, les requêtes DNS continuent d'être traitées par le second.

Diagramme associé :

**DGM-006 – Flux DNS / WireGuard**

Services impliqués :

- AdGuard Home
- DNS publics

Documents associés :

- AdGuard.md
- Freebox-Pop.md

---

# 7. Accès distant

L'accès distant est assuré par WireGuard.

Après authentification, le client VPN rejoint directement le réseau local.

Les différents services deviennent alors accessibles comme si le client était connecté au réseau domestique.

Diagramme associé :

**DGM-006 – Flux DNS / WireGuard**

Services impliqués :

- WireGuard
- Freebox Pop

Documents associés :

- WireGuard.md
- Freebox-Pop.md

---

# 8. Dépendances entre services

| Service | Dépend de |
|----------|-----------|
| Home Assistant | Mosquitto |
| Home Assistant | Z-Wave JS UI |
| Home Assistant | AdGuard Home |
| Téléinformation | Mosquitto |
| Z-Wave JS UI | Contrôleur RaZberry |
| WireGuard | Freebox Pop |

---

# 9. Principes de fonctionnement

L'architecture logique respecte les principes suivants :

## Découplage

Les différents services communiquent au travers de protocoles standards.

Chaque service peut évoluer indépendamment des autres.

---

## Responsabilité unique

Chaque service possède une fonction clairement identifiée.

Aucun service ne réalise plusieurs fonctions critiques.

---

## Résilience

La perte d'un service n'entraîne pas nécessairement l'arrêt complet de l'infrastructure.

Les autres services continuent de fonctionner lorsque cela est possible.

---

# 10. Évolutions prévues

Les évolutions actuellement identifiées sont :

- remplacement du Raspberry Pi Z-Wave par Home Assistant Connect ZWAV-2 ;
- ajout de nouveaux services Home Assistant ;
- évolution de la supervision.

---

# 11. Documents associés

## Architecture

- Architecture.md
- Topologie-Reseau.md
- Inventaire.md
- Adressage-IP.md

## Services

- Mosquitto.md
- AdGuard.md
- WireGuard.md

## Home Assistant

- Home-Assistant-Green.md
- RPi-Linky.md
- RPi-ZWave.md

## Diagrammes

- DGM-003 – Architecture logique
- DGM-004 – Flux MQTT
- DGM-005 – Flux Z-Wave
- DGM-006 – Flux DNS / WireGuard

---

Le présent document décrit l'état de référence de l'architecture logique au moment de sa rédaction.

Toute modification des interactions entre services devra être répercutée dans cette documentation avant sa mise en production.
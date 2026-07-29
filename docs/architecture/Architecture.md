# Architecture de l'infrastructure

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Architecture de l'infrastructure |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document présente l'architecture générale de l'infrastructure informatique et domotique d'**Ohana-House**.

Il constitue le document de référence du projet et décrit les grands principes d'organisation de l'infrastructure.

Les aspects techniques détaillés (configuration des équipements, procédures, adressage IP, services, etc.) sont documentés dans les chapitres dédiés.

---

# 2. Objectifs

L'architecture a été conçue afin de répondre aux objectifs suivants :

- Séparer les responsabilités entre les différents équipements.
- Limiter les dépendances entre les services.
- Faciliter les opérations de maintenance.
- Simplifier la restauration après une panne.
- Permettre l'évolution de l'infrastructure sans remettre en cause son architecture.

---

# 3. Principes d'architecture

## Modularité

Chaque équipement possède un rôle clairement défini.

Aucun équipement n'assure plusieurs fonctions critiques lorsqu'il est possible de les séparer.

---

## Simplicité

Les communications reposent exclusivement sur des protocoles standards :

- Ethernet
- Wi-Fi
- MQTT
- WebSocket
- DNS
- WireGuard

---

## Évolutivité

L'infrastructure a été pensée pour permettre le remplacement d'un composant sans remettre en cause son architecture globale.

Quelques exemples :

- remplacement du Raspberry Pi Z-Wave par un Home Assistant Connect ZWAV-2 ;
- remplacement d'un switch ;
- ajout d'un NAS ;
- ajout d'un onduleur.

---

## Documentation

Toute évolution importante de l'infrastructure doit être documentée dans ce dépôt Git avant sa mise en production.

---

# 4. Vue d'ensemble

L'infrastructure repose sur trois ensembles complémentaires.

## Infrastructure réseau

Elle assure la connectivité entre tous les équipements.

Équipements concernés :

- BOX-01
- SW-01
- SW-02
- SW-03
- AP-01

Diagrammes associés :

- DGM-001 – Architecture physique
- DGM-002 – Topologie réseau

---

## Infrastructure domotique

Elle héberge les différents services nécessaires au fonctionnement de la maison connectée.

Équipements concernés :

- HA-01
- LINKY-01
- ZWAVE-01

Diagramme associé :

- DGM-003 – Architecture logique

---

## Services

Les principaux services sont :

- Home Assistant
- Mosquitto
- Z-Wave JS UI
- AdGuard Home
- WireGuard

Chaque service est documenté dans son chapitre dédié.

---

# 5. Flux principaux

Les échanges entre les différents composants sont assurés par quatre flux principaux.

| Flux | Diagramme associé |
|------|-------------------|
| Téléinformation / MQTT | DGM-004 – Flux MQTT |
| Réseau Z-Wave | DGM-005 – Flux Z-Wave |
| DNS | DGM-006 – Flux DNS / WireGuard |
| Accès distant WireGuard | DGM-006 – Flux DNS / WireGuard |

Les diagrammes constituent la référence de fonctionnement des différents flux de communication.

---

# 6. Répartition des responsabilités

| Équipement | Fonction principale |
|------------|---------------------|
| BOX-01 | Accès Internet, routage et DHCP |
| SW-01 | Distribution principale du réseau |
| SW-02 | Backbone réseau |
| SW-03 | Distribution du réseau domotique |
| AP-01 | Couverture Wi-Fi |
| HA-01 | Instance Home Assistant principale |
| LINKY-01 | Acquisition de la téléinformation Linky |
| ZWAVE-01 | Gestion du réseau Z-Wave |

Chaque composant possède une responsabilité clairement définie.

Cette séparation facilite la maintenance et limite les impacts en cas de panne.

---

# 7. Dépendances

Les principales dépendances de l'infrastructure sont les suivantes.

| Composant | Dépend de |
|------------|-----------|
| HA-01 | Mosquitto |
| HA-01 | ZWAVE-01 (Z-Wave JS UI) |
| LINKY-01 | Réseau Wi-Fi |
| ZWAVE-01 | Réseau Ethernet |
| Tous les équipements | BOX-01 |

Le détail des dépendances est documenté dans les chapitres spécifiques.

---

# 8. Résilience

L'infrastructure a été conçue afin de limiter les conséquences d'une panne.

Les principaux choix retenus sont :

- séparation des fonctions Linky et Z-Wave ;
- services répartis sur plusieurs équipements ;
- double serveur DNS via AdGuard Home ;
- équipements critiques connectés en Ethernet lorsque cela est possible ;
- utilisation de protocoles standards afin de simplifier les opérations de maintenance et de restauration.

Les procédures de restauration sont décrites dans le dossier `procedures`.

---

# 9. Évolutions prévues

Les principales évolutions actuellement identifiées sont :

- migration vers Home Assistant Connect ZWAV-2 ;
- ajout d'un NAS ;
- ajout d'un onduleur ;
- amélioration de la supervision ;

Ces évolutions sont suivies dans `ROADMAP.md`.

---

# 10. Documents associés

## Architecture

- Inventaire.md
- Topologie-Reseau.md
- Architecture-Logique.md
- Décisions-d-Architecture.md
- Adressage-IP.md

## Réseau

- Freebox-Pop.md
- Switches.md
- Linksys-LAPAC1750.md

## Services

- Mosquitto.md
- AdGuard.md
- WireGuard.md

## Home Assistant

- Home-Assistant-Green.md
- RPi-Linky.md
- RPi-ZWave.md

## Procédures

Voir le dossier `procedures`.
# Home Assistant Green

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Home Assistant Green |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit l'instance principale **Home Assistant Green** de l'infrastructure **Ohana-House**.

HA-01 constitue le cœur du système domotique. Il centralise les données, orchestre les interactions entre les différents composants de l'infrastructure et fournit les services nécessaires au pilotage de l'habitation.

L'ensemble des autres composants documentés dans ce projet ont pour objectif de fournir un service à HA-01 ou d'être pilotés par celui-ci.

---

# 2. Fiche d'identité

| Élément | Valeur |
|---------|--------|
| Identifiant | HA-01 |
| Nom | Home Assistant Green |
| Fabricant | Nabu Casa |
| Catégorie | Plateforme domotique |
| Fonction principale | Centralisation et orchestration de la domotique |
| Rôle dans l'architecture | Orchestrateur |
| Adresse IP | 192.168.1.247 |
| Interface réseau | Ethernet 1 Gb/s |
| Criticité | Très haute |
| Supervision | Auto-supervision |
| Sauvegarde | Oui |
| Procédure de restauration | À rédiger |

---

# 3. Position dans l'infrastructure

| Amont | Composant | Aval |
|--------|-----------|------|
| BOX-01 → SW-01 → SW-02 → SW-03 | HA-01 | Utilisateurs, automatismes et tableaux de bord |

---

# 4. Rôle dans l'architecture

HA-01 est le composant central de l'infrastructure.

Il assure notamment :

- l'orchestration des différents services ;
- l'exécution des automatisations ;
- la centralisation des données ;
- la supervision de l'infrastructure ;
- la mise à disposition des tableaux de bord ;
- l'intégration des différents protocoles domotiques.

Les fonctions spécialisées (téléinformation, Z-Wave, DNS, VPN...) sont volontairement déportées vers des composants dédiés afin d'améliorer la modularité et la résilience de l'infrastructure.

---

# 5. Interactions avec l'infrastructure

## Téléinformation

| Source | Traitement | Destination |
|---------|------------|-------------|
| Compteur Linky | LINKY-01 | Mosquitto |
| Mosquitto | HA-01 | Entités Home Assistant |
| Home Assistant | Tableaux de bord | Utilisateurs |

---

## Réseau Z-Wave

| Source | Traitement | Destination |
|---------|------------|-------------|
| Modules Z-Wave | Contrôleur RaZberry | ZWAVE-01 |
| ZWAVE-01 | HA-01 | Entités Home Assistant |

---

## Résolution DNS

| Source | Traitement | Destination |
|---------|------------|-------------|
| HA-01 | AdGuard Home | DNS publics |

---

## Accès distant

| Source | Traitement | Destination |
|---------|------------|-------------|
| Client VPN | WireGuard | HA-01 |

---

## Messagerie MQTT

| Source | Traitement | Destination |
|---------|------------|-------------|
| LINKY-01 | Mosquitto | HA-01 |

---

# 6. Services

## Services fournis

HA-01 fournit les services suivants :

| Service | Description |
|----------|-------------|
| Automatisations | Exécution des scénarios domotiques |
| Tableaux de bord | Interface utilisateur |
| Intégrations | Communication avec les équipements |
| API | Accès aux applications et services externes |
| Supervision | Suivi de l'état de l'infrastructure |

---

## Services hébergés

| Service | Description |
|----------|-------------|
| Home Assistant OS | Système d'exploitation |
| Home Assistant Core | Plateforme domotique |
| Mosquitto | Broker MQTT |

Les autres services sont documentés dans leurs documents respectifs.

---

# 7. Dépendances

## HA-01 dépend de

- BOX-01
- SW-01
- SW-02
- SW-03
- AdGuard Home
- Mosquitto
- LINKY-01
- ZWAVE-01

---

## Les composants suivants dépendent de HA-01

- Tableaux de bord
- Automatismes
- Utilisateurs
- Intégrations

---

# 8. Criticité

| Élément | Valeur |
|---------|--------|
| Niveau | Très haute |
| Fonctionnement global | Très fortement dégradé |
| Redondance | Aucune |
| Priorité de restauration | 1 |

En cas de sinistre, HA-01 constitue le premier composant à restaurer.

---

# 9. Sauvegarde

Les sauvegardes de HA-01 comprennent notamment :

- configuration Home Assistant ;
- automatisations ;
- tableaux de bord ;
- add-ons ;
- utilisateurs ;
- intégrations ;
- secrets.

La procédure complète de sauvegarde est décrite dans le dossier **procedures**.

---

# 10. Maintenance

Les opérations de maintenance comprennent :

- mise à jour de Home Assistant OS ;
- mise à jour de Home Assistant Core ;
- mise à jour des add-ons ;
- vérification des sauvegardes ;
- contrôle des journaux ;
- vérification des intégrations ;
- contrôle des performances générales.

Toute opération importante devra être documentée avant sa mise en production.

---

# 11. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les évolutions importantes de la plateforme devront être consignées dans ce tableau.

---

# 12. Évolutions prévues

Les évolutions actuellement identifiées sont :

- documentation détaillée des intégrations ;
- documentation des sauvegardes automatiques ;
- procédures d'installation et de restauration ;
- documentation des tableaux de bord.

---

# 13. Documents associés

## Architecture

- Architecture.md
- Architecture-Logique.md
- Topologie-Reseau.md
- Decisions-d-Architecture.md

## Réseau

- Freebox-Pop.md
- Switches.md
- Linksys-LAPAC1750.md

## Services

- AdGuard.md
- WireGuard.md
- Mosquitto.md

## Home Assistant

- RPi-Linky.md
- RPi-ZWave.md

---

Le présent document décrit la configuration de référence de HA-01.

Toute modification importante devra être reportée dans cette documentation avant sa mise en production.
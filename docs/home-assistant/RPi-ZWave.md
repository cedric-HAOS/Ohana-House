# Raspberry Pi Z-Wave

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Raspberry Pi Z-Wave |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 ||

---

# 1. Introduction

Ce document décrit le Raspberry Pi dédié au réseau Z-Wave de l'infrastructure **Ohana-House**.

Cette machine est exclusivement utilisée pour héberger le serveur Z-Wave JS UI et piloter le contrôleur Z-Wave.

Le choix d'une machine dédiée permet d'isoler le réseau Z-Wave de la plateforme Home Assistant principale.

---

# 2. Fiche d'identité

| Élément | Valeur |
|---------|--------|
| Identifiant | ZWAVE-01 |
| Nom | Raspberry Pi Z-Wave |
| Fabricant | Raspberry Pi Foundation |
| Catégorie | Serveur Z-Wave |
| Fonction principale | Gestion du réseau Z-Wave |
| Adresse IP | 192.168.1.54 |
| Interface réseau | Ethernet 1 Gb/s |
| Criticité | Haute |
| Supervision | HA-01 |
| Sauvegarde | Oui |
| Procédure de restauration | À rédiger |

---

# 3. Position dans l'infrastructure

| Amont | Composant | Aval |
|--------|-----------|------|
| Contrôleur RaZberry | ZWAVE-01 | HA-01 |

---

# 4. Responsabilités

ZWAVE-01 assure les fonctions suivantes :

- hébergement du serveur Z-Wave JS UI ;
- gestion du réseau Z-Wave ;
- communication avec le contrôleur RaZberry ;
- mise à disposition du réseau Z-Wave pour Home Assistant.

Cette machine n'héberge aucun autre service.

---

# 5. Configuration

Le Raspberry Pi utilise :

| Élément | Valeur |
|---------|--------|
| Système | Home Assistant OS |
| Serveur Z-Wave | Z-Wave JS UI |
| Contrôleur | RaZberry |
| Réseau | Ethernet |

Home Assistant communique avec le serveur Z-Wave JS UI via le réseau local.

Les paramètres détaillés du réseau Z-Wave sont documentés dans la configuration Home Assistant.

---

# 6. Dépendances

ZWAVE-01 dépend :

- de l'alimentation électrique ;
- du réseau Ethernet ;
- du contrôleur RaZberry.

HA-01 dépend de ZWAVE-01 pour accéder au réseau Z-Wave.

Une indisponibilité de HA-01 n'interrompt pas le fonctionnement de Z-Wave JS UI, mais les équipements Z-Wave ne sont plus exploités par Home Assistant.

---

# 7. Criticité

| Élément | Valeur |
|---------|--------|
| Niveau | Haute |
| Fonctionnement de HA | Dégradé |
| Fonctionnement global | Partiel |
| Redondance | Aucune |

Une panne de ZWAVE-01 entraîne l'arrêt de toutes les communications avec les équipements Z-Wave.

---

# 8. Sauvegarde

Les éléments suivants doivent être sauvegardés :

- configuration Home Assistant OS ;
- configuration Z-Wave JS UI ;
- configuration du contrôleur RaZberry.

La procédure de sauvegarde est décrite dans le dossier **procedures**.

---

# 9. Maintenance

Les opérations de maintenance comprennent :

- mise à jour de Home Assistant OS ;
- mise à jour de Z-Wave JS UI ;
- contrôle des journaux ;
- vérification de la communication avec HA-01 ;
- vérification du bon fonctionnement du réseau Z-Wave.

---

# 10. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les modifications importantes devront être consignées dans ce tableau.

---

# 11. Évolutions prévues

Les évolutions actuellement identifiées sont :

- migration vers Home Assistant Connect ZWAVE-2 (version 1.1 – Yamato) ;
- rédaction de la procédure de restauration ;
- documentation détaillée du réseau Z-Wave.

---

# 12. Documents associés

## Services

- Mosquitto.md

## Home Assistant

- Home-Assistant-Green.md
- RPi-Linky.md

## Architecture

- Architecture-Logique.md
- Decisions-d-Architecture.md

---

Le présent document décrit la configuration de référence de ZWAVE-01.

Toute modification importante devra être reportée dans cette documentation avant sa mise en production.
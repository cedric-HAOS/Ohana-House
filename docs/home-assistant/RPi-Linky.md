# Raspberry Pi Linky

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Raspberry Pi Linky |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit le Raspberry Pi dédié à la collecte de la téléinformation du compteur Linky.

Cette machine est exclusivement utilisée pour acquérir les données de consommation électrique et les publier sur le broker MQTT de l'infrastructure.

Le choix d'une machine dédiée permet d'isoler cette fonction critique de la plateforme Home Assistant principale.

---

# 2. Fiche d'identité

| Élément | Valeur |
|---------|--------|
| Identifiant | LINKY-01 |
| Nom | Raspberry Pi Linky |
| Fabricant | Raspberry Pi Foundation |
| Catégorie | Serveur de collecte |
| Fonction principale | Acquisition de la téléinformation Linky |
| Adresse IP | 192.168.1.53 |
| Interface réseau | Wi-Fi |
| Criticité | Haute |
| Supervision | HA-01 |
| Sauvegarde | Oui |
| Procédure de restauration | À rédiger |

---

# 3. Position dans l'infrastructure

| Amont | Composant | Aval |
|--------|-----------|------|
| Compteur Linky | LINKY-01 | Mosquitto |

---

# 4. Responsabilités

LINKY-01 assure les fonctions suivantes :

- acquisition des données de téléinformation ;
- traitement des trames reçues ;
- publication des données sur le broker MQTT ;
- mise à disposition des informations pour Home Assistant.

Cette machine n'héberge aucun autre service.

---

# 5. Configuration

Le Raspberry Pi utilise :

| Élément | Valeur |
|---------|--------|
| Système | Home Assistant OS |
| Réseau | Wi-Fi |
| Téléinformation | Interface série |
| Publication | MQTT |
| Broker MQTT | Mosquitto (HA-01) |

Les paramètres détaillés de publication MQTT sont documentés dans la configuration Home Assistant.

---

# 6. Dépendances

LINKY-01 dépend :

- de l'alimentation électrique ;
- du réseau Wi-Fi ;
- du compteur Linky ;
- de Mosquitto.

Une indisponibilité de Mosquitto empêche la publication des données.

Une indisponibilité de HA-01 n'empêche pas LINKY-01 d'acquérir les données, mais celles-ci ne sont plus exploitées.

---

# 7. Criticité

| Élément | Valeur |
|---------|--------|
| Niveau | Haute |
| Fonctionnement de HA | Dégradé |
| Fonctionnement global | Partiel |
| Redondance | Aucune |

Une panne de LINKY-01 entraîne l'arrêt de la remontée des informations de consommation électrique.

---

# 8. Sauvegarde

Les éléments suivants doivent être sauvegardés :

- configuration Home Assistant OS ;
- configuration de la téléinformation ;
- paramètres MQTT.

La procédure de sauvegarde est décrite dans le dossier **procedures**.

---

# 9. Maintenance

Les opérations de maintenance comprennent :

- mise à jour de Home Assistant OS ;
- contrôle de la liaison série ;
- vérification des publications MQTT ;
- contrôle des journaux.

---

# 10. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les modifications importantes devront être consignées dans ce tableau.

---

# 11. Évolutions prévues

Les évolutions actuellement identifiées sont :

- documentation détaillée de la téléinformation ;
- procédure complète de restauration ;
- ajout éventuel d'une supervision spécifique.

---

# 12. Documents associés

## Services

- Mosquitto.md

## Home Assistant

- Home-Assistant-Green.md
- RPi-ZWave.md

## Architecture

- Architecture-Logique.md

---

Le présent document décrit la configuration de référence de LINKY-01.

Toute modification importante devra être reportée dans cette documentation avant sa mise en production.
# Mosquitto

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Mosquitto |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit le broker MQTT Mosquitto utilisé dans l'infrastructure **Ohana-House**.

Mosquitto assure les échanges de messages entre les différents équipements de l'infrastructure et Home Assistant.

Il constitue le point central des communications MQTT.

---

# 2. Fiche d'identité

| Élément | Valeur |
|---------|--------|
| Nom | Mosquitto |
| Catégorie | Broker MQTT |
| Hébergement | HA-01 (Home Assistant Green) |
| Fonction principale | Broker MQTT |
| Criticité | Haute |
| Supervision | Home Assistant |
| Sauvegarde | Oui |
| Procédure de restauration | À rédiger |

---

# 3. Position dans l'infrastructure

| Amont | Service | Aval |
|--------|----------|------|
| LINKY-01 | Mosquitto | HA-01 |

---

# 4. Responsabilités

Mosquitto assure les fonctions suivantes :

- réception des messages MQTT ;
- distribution des messages aux abonnés ;
- communication entre les équipements compatibles MQTT ;
- découplage des producteurs et des consommateurs de données.

Le broker constitue le point central des échanges MQTT de l'infrastructure.

---

# 5. Architecture

Mosquitto est installé comme **add-on** sur HA-01.

Les équipements MQTT se connectent directement au broker.

À ce jour, les principaux échanges concernent :

- LINKY-01 (Téléinformation Linky) ;
- HA-01.

L'architecture permet l'ajout de nouveaux clients MQTT sans modification du broker.

---

# 6. Dépendances

Mosquitto dépend :

- de HA-01 ;
- du réseau local.

Les équipements suivants utilisent le broker :

- LINKY-01 ;
- HA-01.

De futurs équipements pourront également publier ou consommer des messages MQTT.

---

# 7. Criticité

| Élément | Valeur |
|---------|--------|
| Niveau | Haute |
| Impact en cas de panne | Perte des échanges MQTT |
| Redondance | Aucune |

Une panne du broker n'interrompt pas Home Assistant mais rend indisponibles les échanges MQTT.

---

# 8. Sauvegarde

La configuration de Mosquitto est incluse dans les sauvegardes de HA-01.

Toute modification importante devra être sauvegardée avant sa mise en production.

---

# 9. Maintenance

Les opérations de maintenance comprennent :

- mise à jour de l'add-on ;
- contrôle des journaux ;
- vérification des connexions MQTT ;
- contrôle du bon fonctionnement des publications.

---

# 10. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les modifications importantes devront être consignées dans ce tableau.

---

# 11. Évolutions prévues

Les évolutions actuellement identifiées sont :

- documentation des utilisateurs MQTT ;
- procédure de restauration ;
- procédure de migration.

---

# 12. Documents associés

## Services

- AdGuard.md
- WireGuard.md

## Home Assistant

- Home-Assistant-Green.md
- RPi-Linky.md

---

Le présent document décrit la configuration de référence du broker MQTT.

Toute modification importante devra être reportée dans cette documentation avant sa mise en production.
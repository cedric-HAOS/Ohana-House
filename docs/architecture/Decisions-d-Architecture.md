# Décisions d'architecture

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Décisions d'architecture |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document recense les principales décisions d'architecture retenues pour l'infrastructure **Ohana-House**.

Il explique les motivations techniques ayant conduit à ces choix.

L'objectif est de conserver une trace des décisions structurantes afin de faciliter la maintenance, les évolutions futures et la compréhension globale de l'infrastructure.

Ce document ne décrit pas la configuration des équipements mais les principes ayant guidé leur conception.

---

# 2. Infrastructure réseau

## Serveur DHCP sur INFRA-01

### Décision

Le service DHCP cible est fourni par dnsmasq sur INFRA-01. La Freebox ne doit
conserver son DHCP que temporairement pendant une opération de reprise ou de
migration.

### Justification

INFRA-01 permet de versionner les réservations, de distribuer explicitement la
passerelle BOX-01, les deux serveurs DNS et la référence NTP, puis d'administrer
la configuration par Ohana-Agent. Un seul serveur DHCP reste actif à la fois.

---

## Backbone Ethernet 10 Gb

### Décision

Les deux switchs TRENDnet sont interconnectés par une liaison Ethernet à 10 Gb/s.

### Justification

Cette liaison constitue le backbone principal du réseau.

Elle offre une capacité largement supérieure aux besoins actuels et prépare les futures évolutions de l'infrastructure sans nécessiter de modification de la topologie.

---

## Raspberry Pi Linky connecté en Wi-Fi

### Décision

Le Raspberry Pi Linky est connecté au réseau via le point d'accès Wi-Fi.

### Justification

Le Raspberry Pi est installé à proximité du compteur Linky.

Le trafic réseau généré par la téléinformation est très faible.

Une connexion Ethernet n'apporterait aucun bénéfice significatif.

---

# 3. Infrastructure domotique

## Plusieurs équipements spécialisés

### Décision

Les fonctions principales sont réparties entre plusieurs équipements.

### Justification

Chaque équipement possède une responsabilité clairement définie.

Cette séparation facilite la maintenance, réduit les dépendances et limite les impacts en cas de panne.

---

## Home Assistant Green comme instance principale

### Décision

Le Home Assistant Green constitue le cœur de l'infrastructure domotique.

### Justification

Il héberge Home Assistant ainsi que Mosquitto.

Cette centralisation simplifie l'administration tout en limitant le nombre d'équipements nécessaires.

---

## Mosquitto hébergé sur HA-01

### Décision

Le broker MQTT est installé sur le Home Assistant Green.

### Justification

Plusieurs applications utilisent MQTT.

Le maintenir sur HA-01 simplifie les échanges et évite la multiplication des points de défaillance.

---

## Z-Wave séparé de Home Assistant

### Décision

Le réseau Z-Wave est hébergé sur un Raspberry Pi dédié.

### Justification

Cette architecture permet d'isoler le contrôleur radio du serveur principal.

Elle facilite également son remplacement futur par un Home Assistant Connect ZWAVE-2.

---

# 4. Services

## Deux instances AdGuard Home

### Décision

Deux serveurs AdGuard Home sont installés.

### Justification

Les clients disposent de deux serveurs DNS.

En cas de panne de l'un d'eux, la résolution DNS reste disponible.

---

## Utilisation de MQTT

### Décision

La téléinformation Linky est transmise via MQTT.

### Justification

MQTT découple la collecte des données de leur consommation.

Cette architecture facilite l'ajout de nouveaux consommateurs sans modifier le Raspberry Pi Linky.

---

# 5. Documentation

## Documentation versionnée

### Décision

Toute la documentation est maintenue dans un dépôt Git.

### Justification

Git permet :

- le suivi des modifications ;
- l'historique complet du projet ;
- la restauration d'une version antérieure ;
- la génération automatique des livrables.

---

## Diagrammes Mermaid

### Décision

Tous les diagrammes sont réalisés en Mermaid.

### Justification

Les diagrammes sont versionnés avec la documentation.

Ils restent facilement modifiables sans dépendre d'un logiciel propriétaire.

---

## Manuel d'exploitation

### Décision

La documentation constitue le manuel d'exploitation officiel de l'infrastructure.

### Justification

Le dépôt Git est la source de vérité.

Le PDF généré constitue le livrable destiné à la consultation et à l'impression.

---

# 6. Évolutions prévues

Les décisions suivantes sont déjà identifiées.

- remplacement du Raspberry Pi Z-Wave par un Home Assistant Connect ZWAVE-2 ;
- ajout d'un NAS ;
- ajout d'un onduleur ;
- publication d'une documentation web en complément du PDF.

---

# 7. Documents associés

## Architecture

- Architecture.md
- Topologie-Reseau.md
- Architecture-Logique.md
- Adressage-IP.md
- Capacites-Reseau.md
- Inventaire.md

## Réseau

- Freebox-Pop.md
- Switches.md

## Services

- AdGuard.md
- WireGuard.md
- Mosquitto.md

---

Le présent document décrit les décisions structurantes ayant conduit à l'architecture actuelle de l'infrastructure.

Toute évolution importante devra être précédée d'une mise à jour de ce document.
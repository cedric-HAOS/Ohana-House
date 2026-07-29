# Capacités réseau

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Capacités réseau |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document présente les capacités du réseau de l'infrastructure **Ohana-House**.

Il décrit les performances disponibles, les limites actuelles ainsi que les possibilités d'évolution de l'infrastructure.

La topologie physique est décrite dans **Topologie-Reseau.md**.

---

# 2. Vue d'ensemble

L'infrastructure repose sur un réseau Ethernet complété par une liaison Wi-Fi dédiée au Raspberry Pi Linky.

Le backbone entre les deux switchs principaux fonctionne en 10 Gb/s.

Les équipements domotiques sont connectés en Gigabit Ethernet.

---

# 3. Capacités des équipements

| Équipement | Interface | Capacité maximale |
|------------|-----------|------------------:|
| BOX-01 | Ethernet | 2,5 Gb/s |
| SW-01 | 2 × 10 Gb + 4 × 2,5 Gb | 30 Gb/s cumulés |
| SW-02 | 2 × 10 Gb + 4 × 2,5 Gb | 30 Gb/s cumulés |
| SW-03 | 5 × 1 Gb | 5 Gb/s cumulés |
| AP-01 | Ethernet | 1 Gb/s |
| HA-01 | Ethernet | 1 Gb/s |
| ZWAVE-01 | Ethernet | 1 Gb/s |
| LINKY-01 | Wi-Fi 802.11ac | Selon la qualité radio |

---

# 4. Analyse des liaisons

## Accès Internet

La Freebox est reliée au switch principal via une interface Ethernet à 2,5 Gb/s.

Cette liaison constitue la limite maximale des échanges avec Internet.

---

## Backbone réseau

Les switchs SW-01 et SW-02 sont interconnectés par une liaison Ethernet à 10 Gb/s.

Cette capacité est très supérieure aux besoins actuels de l'infrastructure.

Elle garantit une excellente évolutivité.

---

## Réseau domotique

Le switch SW-03 est relié au backbone par une liaison Gigabit.

Les équipements Home Assistant Green et Raspberry Pi Z-Wave utilisent cette liaison.

Le trafic actuel reste largement inférieur à sa capacité maximale.

---

## Réseau Wi-Fi

Le Raspberry Pi Linky communique via le point d'accès Linksys LAPAC1750.

Le trafic généré par la téléinformation est extrêmement faible et ne constitue pas une contrainte pour le réseau.

---

# 5. Analyse des performances

Les besoins actuels de l'infrastructure sont modestes.

Les principaux flux réseau sont :

| Flux | Charge estimée |
|------|----------------|
| Téléinformation MQTT | Très faible |
| Z-Wave JS UI | Très faible |
| DNS | Très faible |
| Automatisations Home Assistant | Faible |
| Accès Web Home Assistant | Faible |

Aucune liaison ne constitue actuellement un goulot d'étranglement.

---

# 6. Points forts

- Backbone 10 Gb entre les switchs principaux.
- Équipements critiques connectés en Ethernet.
- Séparation entre réseau domotique et réseau principal.
- Infrastructure largement dimensionnée par rapport aux besoins actuels.
- Possibilité d'ajouter de nouveaux équipements sans modification majeure.

---

# 7. Limites identifiées

Les limites actuellement connues sont les suivantes :

- accès Internet limité par l'interface 2,5 Gb/s de la Freebox ;
- switch domotique limité au Gigabit ;
- point d'accès limité à une liaison Ethernet Gigabit ;
- Raspberry Pi Linky dépendant de la qualité du réseau Wi-Fi.

Aucune de ces limites n'a aujourd'hui d'impact sur le fonctionnement de l'infrastructure.

---

# 8. Évolutions possibles

Les évolutions suivantes sont compatibles avec l'architecture actuelle :

- remplacement du switch domotique par un modèle 2,5 Gb/s ;
- ajout d'un NAS ;
- ajout d'un serveur de sauvegarde ;
- remplacement du point d'accès Wi-Fi ;
- migration vers une infrastructure réseau multi-gigabit.

Ces évolutions pourront être réalisées sans remise en cause de l'architecture générale.

---

# 9. Documents associés

## Architecture

- Architecture.md
- Topologie-Reseau.md
- Architecture-Logique.md
- Adressage-IP.md
- Decisions-d-Architecture.md

## Réseau

- Freebox-Pop.md
- Switches.md
- Linksys-LAPAC1750.md

---

Le présent document décrit les capacités de référence du réseau de l'infrastructure.

Toute évolution matérielle ayant un impact sur les performances devra être reportée dans cette documentation.
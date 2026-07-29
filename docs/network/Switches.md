# Switches

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Switches |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit les switchs Ethernet utilisés dans l'infrastructure **Ohana-House**.

Ils assurent la distribution du réseau local entre la Freebox Pop, les équipements domotiques et le point d'accès Wi-Fi.

Les switchs utilisés sont des équipements non administrables (unmanaged). Ils ne nécessitent aucune configuration logicielle.

---

# 2. Fiche d'identité

| Identifiant | Nom | Fabricant | Catégorie | Débit principal | Criticité |
|-------------|-----|-----------|------------|----------------:|-----------|
| SW-01 | TEG-S762 | TRENDnet | Switch principal | 10 Gb / 2,5 Gb | Haute |
| SW-02 | TEG-S762 | TRENDnet | Backbone réseau | 10 Gb / 2,5 Gb | Haute |
| SW-03 | Switch 5 ports | Linksys | Distribution domotique | 1 Gb | Moyenne |

---

# 3. Position dans l'infrastructure

| Amont | Équipement | Aval |
|--------|------------|------|
| BOX-01 | SW-01 | SW-02 / AP-01 |
| SW-01 | SW-02 | SW-03 |
| SW-02 | SW-03 | HA-01 / ZWAVE-01 |

---

# 4. Responsabilités

## SW-01

Le switch principal assure :

- la connexion avec la Freebox Pop ;
- la liaison vers SW-02 ;
- la connexion du point d'accès Wi-Fi.

---

## SW-02

Le switch secondaire assure :

- le backbone de l'infrastructure ;
- la liaison vers le réseau domotique.

---

## SW-03

Le switch Linksys est dédié aux équipements domotiques.

Il distribue le réseau aux équipements suivants :

- HA-01
- ZWAVE-01

---

# 5. Caractéristiques techniques

| Switch | Interfaces |
|----------|------------|
| SW-01 | 2 × 10 Gb + 4 × 2,5 Gb |
| SW-02 | 2 × 10 Gb + 4 × 2,5 Gb |
| SW-03 | 5 × 1 Gb |

Les switchs fonctionnent en mode non administrable.

Aucune configuration particulière n'est nécessaire.

---

# 6. Connexions

| Origine | Destination | Débit |
|----------|-------------|-------:|
| BOX-01 | SW-01 | 2,5 Gb/s |
| SW-01 | SW-02 | 10 Gb/s |
| SW-02 | SW-03 | 1 Gb/s |
| SW-01 | AP-01 | 1 Gb/s |
| SW-03 | HA-01 | 1 Gb/s |
| SW-03 | ZWAVE-01 | 1 Gb/s |

Les interconnexions sont décrites en détail dans **Topologie-Reseau.md**.

---

# 7. Dépendances

Les switchs constituent l'infrastructure de distribution du réseau local.

Une panne de :

- SW-01 impacte la majorité des équipements ;
- SW-02 isole le réseau domotique ;
- SW-03 isole Home Assistant Green et le Raspberry Pi Z-Wave.

---

# 8. Criticité

| Switch | Niveau |
|----------|---------|
| SW-01 | Haute |
| SW-02 | Haute |
| SW-03 | Moyenne |

Les deux switchs TRENDnet sont essentiels au fonctionnement du réseau.

Le switch Linksys impacte uniquement l'infrastructure domotique.

---

# 9. Sauvegarde

Les switchs étant non administrables, aucune sauvegarde de configuration n'est nécessaire.

En cas de remplacement, seul le câblage doit être reproduit.

---

# 10. Maintenance

La maintenance se limite à :

- vérifier l'alimentation ;
- contrôler les voyants d'activité ;
- vérifier les connexions Ethernet ;
- remplacer un équipement en cas de défaillance.

Aucune mise à jour logicielle n'est requise.

---

# 11. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les modifications importantes de l'infrastructure réseau devront être consignées dans ce tableau.

---

# 12. Évolutions prévues

Les évolutions identifiées sont :

- remplacement éventuel du switch Linksys par un modèle multi-gigabit ;
- ajout éventuel d'un switch administrable si les besoins évoluent.

---

# 13. Documents associés

## Architecture

- Topologie-Reseau.md
- Capacites-Reseau.md
- Decisions-d-Architecture.md

## Réseau

- Freebox-Pop.md
- Linksys-LAPAC1750.md

## Services

- AdGuard.md
- WireGuard.md

## Diagrammes

- DGM-001 – Architecture physique
- DGM-002 – Topologie réseau

---

Le présent document décrit les switchs constituant l'infrastructure réseau de référence.

Toute modification de leur rôle ou de leur architecture devra être reportée dans cette documentation avant sa mise en production.
# Linksys LAPAC1750

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | Linksys LAPAC1750 |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit le point d'accès Wi-Fi de l'infrastructure **Ohana-House**.

Le point d'accès assure la connectivité sans fil des équipements nécessitant un accès Wi-Fi.

À ce jour, seul le Raspberry Pi Linky utilise cette connectivité.

---

# 2. Fiche d'identité

| Élément | Valeur |
|---------|--------|
| Identifiant | AP-01 |
| Nom | Linksys LAPAC1750 |
| Fabricant | Linksys |
| Catégorie | Point d'accès Wi-Fi |
| Fonction principale | Accès Wi-Fi |
| Adresse IP | 192.168.1.99 |
| Interface réseau | Ethernet 1 Gb/s |
| Criticité | Moyenne |
| Supervision | Aucune |
| Sauvegarde | Oui |
| Procédure de restauration | À rédiger |

---

# 3. Position dans l'infrastructure

| Amont | Équipement | Aval |
|--------|------------|------|
| SW-01 | AP-01 | LINKY-01 |

---

# 4. Responsabilités

Le point d'accès assure :

- la couverture Wi-Fi de l'habitation ;
- la connexion des équipements sans fil ;
- la liaison réseau du Raspberry Pi Linky.

Il ne réalise aucune fonction de routage ou de DHCP.

---

# 5. Configuration

Le point d'accès est configuré avec les paramètres suivants.

| Paramètre | Valeur |
|-----------|---------|
| SSID | Freebox-0D13A7 |
| Sécurité | WPA2 |
| Bandes actives | 2,4 GHz et 5 GHz |

Les autres paramètres (canaux radio, largeur de bande, puissance d'émission, etc.) seront documentés si leur personnalisation devient nécessaire.

---

# 6. Connexions

| Interface | Destination | Débit |
|-----------|-------------|-------:|
| Ethernet | SW-01 | 1 Gb/s |
| Wi-Fi | LINKY-01 | Selon la qualité radio |

Voir également :

- DGM-001 – Architecture physique
- DGM-002 – Topologie réseau

---

# 7. Dépendances

Le Raspberry Pi Linky dépend directement du point d'accès pour accéder au réseau local.

Les autres équipements critiques utilisent une connexion Ethernet.

---

# 8. Criticité

| Élément | Valeur |
|---------|--------|
| Niveau | Moyenne |
| Impact en cas de panne | Perte du Wi-Fi |
| Redondance | Aucune |

La panne du point d'accès n'empêche pas le fonctionnement du réseau Ethernet.

---

# 9. Sauvegarde

La configuration du point d'accès devra être sauvegardée après chaque modification importante.

Les captures d'écran de configuration pourront être conservées dans :

```
assets/screenshots/linksys/
```

---

# 10. Maintenance

Les opérations de maintenance comprennent :

- mise à jour du firmware ;
- contrôle de la couverture Wi-Fi ;
- vérification des paramètres de sécurité ;
- contrôle des performances radio.

---

# 11. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les modifications importantes de la configuration devront être consignées dans ce tableau.

---

# 12. Évolutions prévues

Les évolutions actuellement identifiées sont :

- documentation complète des paramètres radio ;
- ajout des captures d'écran de configuration ;
- rédaction de la procédure de restauration.

---

# 13. Documents associés

## Architecture

- Topologie-Reseau.md
- Capacites-Reseau.md

## Réseau

- Freebox-Pop.md
- Switches.md

## Services

- AdGuard.md
- WireGuard.md

## Diagrammes

- DGM-001 – Architecture physique
- DGM-002 – Topologie réseau

---

Le présent document décrit la configuration de référence du point d'accès Wi-Fi.

Toute modification de sa configuration devra être reportée dans cette documentation avant sa mise en production.
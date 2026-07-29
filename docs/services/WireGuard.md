# WireGuard

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | WireGuard |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit le service VPN **WireGuard** utilisé dans l'infrastructure **Ohana-House**.

WireGuard permet un accès distant sécurisé au réseau domestique.

Le service est hébergé directement par **BOX-01 (Freebox Pop)**.

---

# 2. Fiche d'identité

| Élément | Valeur |
|---------|--------|
| Nom | WireGuard |
| Catégorie | Service VPN |
| Hébergement | BOX-01 (Freebox Pop) |
| Fonction principale | Accès distant sécurisé |
| Criticité | Haute |
| Supervision | Home Assistant |
| Sauvegarde | Oui |
| Procédure de restauration | À rédiger |

---

# 3. Position dans l'infrastructure

| Amont | Service | Aval |
|--------|----------|------|
| Internet | WireGuard | Réseau local |

---

# 4. Responsabilités

WireGuard assure les fonctions suivantes :

- accès sécurisé au réseau local depuis Internet ;
- chiffrement des communications ;
- authentification des clients VPN ;
- accès distant aux services internes.

L'accès VPN constitue le moyen privilégié d'administration à distance de l'infrastructure.

---

# 5. Architecture

WireGuard est hébergé directement sur **BOX-01**.

Cette architecture présente plusieurs avantages :

- aucun équipement supplémentaire n'est nécessaire ;
- le service reste disponible indépendamment de Home Assistant ;
- l'administration est centralisée sur la Freebox.

Les clients VPN sont configurés individuellement.

---

# 6. Dépendances

WireGuard dépend :

- de la connexion Internet ;
- de BOX-01 ;
- des clients VPN autorisés.

Le fonctionnement des équipements internes ne dépend pas du VPN.

Une panne de WireGuard empêche uniquement l'accès distant.

---

# 7. Criticité

| Élément | Valeur |
|---------|--------|
| Niveau | Haute |
| Impact en cas de panne | Accès distant indisponible |
| Redondance | Aucune |

WireGuard est un service critique pour l'administration distante mais n'impacte pas le fonctionnement local de l'infrastructure.

---

# 8. Sauvegarde

La configuration VPN devra être sauvegardée après chaque modification importante.

Les éléments suivants devront être conservés :

- configuration WireGuard ;
- profils des clients ;
- clés publiques des clients.

La procédure de sauvegarde sera documentée dans la section Procédures.

---

# 9. Maintenance

Les opérations de maintenance comprennent :

- ajout ou suppression d'un client VPN ;
- vérification des profils ;
- contrôle des connexions ;
- vérification du fonctionnement après mise à jour de BOX-01.

---

# 10. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les modifications importantes devront être consignées dans ce tableau.

---

# 11. Évolutions prévues

Les évolutions actuellement identifiées sont :

- documentation des profils clients ;
- procédure de création d'un nouveau client ;
- procédure de restauration ;
- ajout éventuel de captures d'écran de configuration.

---

# 12. Documents associés

## Architecture

- Architecture-Logique.md
- Decisions-d-Architecture.md

## Réseau

- Freebox-Pop.md
- AdGuard.md

## Procédures

- Installer-WireGuard.md
- Restaurer-WireGuard.md

---

Le présent document décrit la configuration de référence du service WireGuard.

Toute modification importante devra être reportée dans cette documentation avant sa mise en production.
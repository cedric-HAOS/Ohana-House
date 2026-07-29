# AdGuard Home

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Document | AdGuard Home |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

---

# 1. Introduction

Ce document décrit l'architecture et la configuration des serveurs **AdGuard Home** utilisés dans l'infrastructure **Ohana-House**.

Les serveurs AdGuard Home assurent la résolution DNS des équipements du réseau local ainsi que le filtrage des requêtes DNS.

Deux instances sont utilisées afin d'améliorer la disponibilité du service.

---

# 2. Fiche d'identité

| Élément | Valeur |
|---------|--------|
| Nom | AdGuard Home |
| Catégorie | Service réseau |
| Fonction principale | DNS et filtrage DNS |
| Instances | 2 |
| Hébergement | LINKY-01 (Raspberry Pi Linky) et ZWAVE-01 (Raspberry Pi Z-Wave) |
| Criticité | Haute |
| Supervision | Home Assistant |
| Sauvegarde | Oui |
| Procédure de restauration | À rédiger |

---

# 3. Position dans l'infrastructure

| Amont | Service | Aval |
|--------|----------|------|
| Clients du réseau | AdGuard Home | Serveurs DNS publics |

---

# 4. Responsabilités

Les instances AdGuard Home assurent les fonctions suivantes :

- résolution DNS du réseau local ;
- filtrage des domaines publicitaires ;
- filtrage des domaines malveillants ;
- amélioration des performances DNS ;
- continuité du service DNS en cas de panne d'une instance.

Les équipements du réseau utilisent ces serveurs comme résolveurs DNS principaux.

---

# 5. Architecture

L'infrastructure repose sur deux instances indépendantes.

| Instance | Hébergement | État |
|-----------|-------------|------|
| AGH-01 — principal | ZWAVE-01 | Active |
| AGH-02 — secondaire | LINKY-01 | Active |

Les deux serveurs utilisent une configuration identique.

ZWAVE-01 constitue la source de vérité. La configuration est répliquée vers LINKY-01 par le mécanisme de synchronisation documenté pour INFRA-01.

---

# 6. Dépendances

AdGuard Home dépend :

- du réseau local ;
- de la connectivité Internet ;
- des serveurs DNS publics configurés comme résolveurs amont.

Le fonctionnement de Home Assistant n'est pas interrompu si une seule instance devient indisponible.

---

# 7. Criticité

| Élément | Valeur |
|---------|--------|
| Niveau | Haute |
| Impact en cas de panne d'une instance | Faible |
| Impact en cas de panne des deux instances | Perte de la résolution DNS |
| Redondance | Oui |

La présence de deux instances améliore la disponibilité du service.

---

# 8. Sauvegarde

La configuration de chaque instance est sauvegardée régulièrement.

Les listes de filtrage, paramètres DNS et configurations personnalisées doivent être identiques sur les deux serveurs.

La méthode de sauvegarde est décrite dans la documentation des procédures.

---

# 9. Maintenance

Les opérations de maintenance comprennent :

- mise à jour d'AdGuard Home ;
- contrôle des listes de filtrage ;
- vérification des performances DNS ;
- vérification de la synchronisation des deux instances ;
- contrôle des journaux.

---

# 10. Historique fonctionnel

| Date | Version | Modification | Référence |
|------|---------|--------------|-----------|
| 2026-07-03 | v0.5.0 (Kakashi) | Création du document | Initialisation |

Les modifications importantes de la configuration devront être consignées dans ce tableau.

---

# 11. Évolutions prévues

Les évolutions actuellement identifiées sont :

- ajout des captures d'écran de configuration si nécessaire ;
- rédaction de la procédure de restauration ;
- documentation de la synchronisation Git ;
- supervision détaillée dans Home Assistant.

---

# 12. Documents associés

## Architecture

- Architecture-Logique.md
- Decisions-d-Architecture.md

## Réseau

- Freebox-Pop.md
- Linksys-LAPAC1750.md
- WireGuard.md

## Home Assistant

- Home-Assistant-Green.md

---

Le présent document décrit la configuration de référence du service AdGuard Home.

Toute modification importante devra être reportée dans cette documentation avant sa mise en production.
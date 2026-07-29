# ADR-001 — Autonomie locale de l'infrastructure

> **Statut :** ✅ Accepté
>
> **Date :** 2026-07-06
>
> **Décideurs :** Projet Ohana-House
>
> **Impact :** Majeur

---

# Contexte

L'infrastructure Ohana-House repose sur plusieurs services essentiels :

- automatisation de la maison ;
- résolution DNS ;
- attribution des adresses IP ;
- synchronisation temporelle ;
- communication entre équipements.

Historiquement, certaines de ces capacités dépendaient directement de la Freebox.

Cette dépendance est incompatible avec l'objectif d'autonomie locale poursuivi par le projet Hashirama.

---

# Problème

Une panne de la Freebox entraîne simultanément :

- perte de l'accès Internet ;
- perte du serveur DHCP ;
- indisponibilité du VPN.

Même si Home Assistant continue de fonctionner, certaines capacités fondamentales de la maison ne sont plus garanties.

L'architecture doit être repensée afin de limiter cette dépendance.

---

# Décision

L'infrastructure est réorganisée afin que les capacités fondamentales de la maison puissent continuer à fonctionner indépendamment de la disponibilité de la Freebox.

Les responsabilités sont réparties entre plusieurs machines spécialisées.

---

# Capacités garanties

L'architecture garantit les capacités suivantes.

---

## Fonctionnement local

La maison doit continuer à fonctionner sans accès Internet.

---

## Attribution des adresses IP

Les équipements doivent pouvoir rejoindre le réseau local indépendamment de la Freebox.

---

## Résolution DNS locale

Les équipements doivent continuer à résoudre les noms internes.

---

## Référence temporelle

Les équipements doivent disposer d'une heure cohérente.

---

## Continuité des automatisations

Les automatisations locales doivent rester opérationnelles.

---

# Principes retenus

## Autonomie locale

Le fonctionnement local est prioritaire sur les services Cloud.

---

## Dégradation maîtrisée

Toute panne doit provoquer une perte limitée de capacités.

---

## Responsabilité unique

Chaque machine possède une mission clairement identifiée.

---

## Simplicité

Les solutions retenues privilégient la facilité de compréhension et de restauration.

---

## Restaurabilité

Les composants critiques doivent être :

- documentés ;
- sauvegardés ;
- rapidement restaurables.

---

# Conséquences

## Avantages

- autonomie renforcée ;
- architecture plus lisible ;
- dépendances réduites ;
- restauration simplifiée.

## Inconvénients

- apparition d'un nouveau composant d'infrastructure ;
- nécessité de documenter et sauvegarder celui-ci.

Ces contraintes sont jugées acceptables.

---

# Alternatives étudiées

## Conserver les capacités sur la Freebox

Non retenu.

La dépendance au matériel du fournisseur d'accès reste trop importante.

---

## Haute disponibilité complète

Non retenue.

Complexité disproportionnée au regard des besoins d'Ohana-House.

---

# Décisions dérivées

- ADR-002 — Supervision des capacités
- ADR-003 — Services d'infrastructure (INFRA-01)

---

# Références

- Architecture-Reference.md
- Architecture-Conventions.md

---

# Conclusion

L'autonomie locale devient le principe fondateur de l'architecture Hashirama.

Toutes les futures décisions devront préserver ou renforcer cette autonomie.
# ADR-006 — Sauvegarde et restauration d'INFRA-01

> **Statut :** ✅ Accepté
>
> **Date :** 2026-07-06
>
> **Décideurs :** Projet Ohana-House
>
> **Impact :** Important

---

# Contexte

INFRA-01 devient un composant central de l'architecture Hashirama.

Il garantit plusieurs capacités fondamentales de l'infrastructure locale :

- attribution des adresses IP ;
- référence temporelle locale ;
- synchronisation des serveurs DNS ;
- supervision ;
- scripts d'administration.

Même si INFRA-01 constitue un nouveau point de défaillance unique, ce risque est accepté à condition que sa restauration soit rapide, documentée et reproductible.

---

# Problème

Une panne d'INFRA-01 peut entraîner :

- l'indisponibilité du DHCP ;
- l'indisponibilité du serveur NTP local ;
- l'arrêt de la synchronisation DNS ;
- l'absence de supervision ;
- l'indisponibilité des scripts d'administration.

Sans stratégie de sauvegarde et de restauration claire, la remise en service pourrait dépendre de manipulations manuelles ou de la mémoire de l'administrateur.

Ce fonctionnement est incompatible avec les principes de Hashirama.

---

# Décision

INFRA-01 doit être sauvegardé et restaurable selon une méthode simple, documentée et reproductible.

La stratégie retenue repose sur deux niveaux :

1. sauvegarde logique des configurations ;
2. restauration complète par réinstallation puis réapplication des configurations sauvegardées.

L'objectif n'est pas de cloner entièrement le système, mais de garantir une reconstruction rapide et fiable.

---

# Capacités garanties

## Restaurabilité

INFRA-01 doit pouvoir être reconstruit sans improvisation.

---

## Sauvegarde des configurations

Les fichiers de configuration nécessaires au fonctionnement des services d'infrastructure doivent être sauvegardés.

---

## Reproductibilité

La restauration doit s'appuyer sur des procédures documentées.

---

## Indépendance matérielle

La restauration ne doit pas dépendre strictement du Raspberry Pi 3 utilisé initialement.

INFRA-01 désigne un rôle, pas un matériel.

---

## RTO maîtrisé

L'objectif de restauration d'INFRA-01 doit être court.

La cible est une remise en service en moins de 30 minutes après disponibilité du matériel.

---

# Principes retenus

## Sauvegarde logique prioritaire

Les configurations sont plus importantes que l'image complète du système.

---

## Réinstallation propre

En cas de panne majeure, la machine est reconstruite à partir d'une installation propre.

---

## Documentation avant automatisation

La procédure manuelle doit exister avant toute automatisation future par Ohana-Agent.

---

## Matériel remplaçable

INFRA-01 doit pouvoir être remplacé par un autre Raspberry Pi ou une autre machine compatible.

---

# Éléments à sauvegarder

Les éléments suivants devront être inclus dans la stratégie de sauvegarde :

- configuration DHCP ;
- réservations DHCP ;
- configuration NTP ;
- configuration de synchronisation DNS ;
- scripts d'administration ;
- configuration de supervision ;
- configuration future d'Ohana-Agent.

---

# Conséquences

## Avantages

- restauration rapide ;
- indépendance vis-à-vis du matériel ;
- meilleure maintenabilité ;
- réduction du risque lié à INFRA-01 ;
- préparation à l'automatisation future.

## Inconvénients

- nécessité de maintenir une procédure de sauvegarde ;
- nécessité de tester régulièrement la restauration ;
- dépendance à la qualité de la documentation.

Ces contraintes sont considérées comme acceptables.

---

# Alternatives étudiées

## Image complète de la carte SD uniquement

Non retenue comme stratégie principale.

Elle peut être utile ponctuellement, mais elle dépend trop fortement du support matériel et peut masquer des problèmes de configuration.

---

## Aucune sauvegarde dédiée

Non retenue.

INFRA-01 porte trop de capacités fondamentales pour être reconstruit uniquement de mémoire.

---

## Haute disponibilité d'INFRA-01

Non retenue.

La complexité serait disproportionnée par rapport au besoin.

Une restauration rapide est préférée à une haute disponibilité complète.

---

# Décisions dérivées

Cette décision conduit notamment à :

- une procédure de sauvegarde d'INFRA-01 ;
- une procédure de restauration d'INFRA-01 ;
- une vérification périodique de restaurabilité ;
- une future intégration possible dans Ohana-Agent.

---

# Références

- Architecture-Reference.md
- Architecture-Conventions.md
- ADR-001 — Autonomie locale de l'infrastructure
- ADR-003 — Services d'infrastructure (INFRA-01)

---

# Conclusion

INFRA-01 est un composant important de l'architecture Hashirama.

Son rôle central est accepté parce qu'il reste simple, documenté, sauvegardé et rapidement restaurable.

La stratégie retenue privilégie la restauration maîtrisée plutôt que la haute disponibilité complexe.
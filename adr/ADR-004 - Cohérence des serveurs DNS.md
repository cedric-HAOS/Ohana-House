# ADR-004 — Synchronisation des instances DNS

> **Statut :** ✅ Accepté
>
> **Date :** 2026-07-06
>
> **Décideurs :** Projet Ohana-House
>
> **Impact :** Important

---

# Contexte

L'infrastructure Ohana-House repose sur deux serveurs DNS locaux afin de garantir la continuité de la résolution de noms.

Cette redondance améliore la disponibilité de la capacité de résolution DNS.

Cependant, la présence de plusieurs serveurs introduit un nouveau risque : la divergence de configuration.

Une architecture résiliente doit garantir que tous les serveurs DNS présentent une configuration cohérente.

---

# Problème

Deux serveurs DNS administrés indépendamment peuvent progressivement diverger.

Cette situation peut entraîner :

- des règles de filtrage différentes ;
- des réécritures DNS incohérentes ;
- des listes de blocage différentes ;
- des comportements imprévisibles selon le serveur utilisé.

Cette incohérence est incompatible avec les objectifs de simplicité et de prévisibilité de l'infrastructure.

---

# Décision

L'infrastructure garantit l'existence d'une configuration DNS unique.

Toutes les instances DNS doivent présenter une configuration fonctionnellement identique.

Les modifications de configuration sont propagées automatiquement entre les instances.

---

# Capacités garanties

---

## Résolution DNS cohérente

Un même nom doit produire le même résultat quel que soit le serveur DNS interrogé.

---

## Politique de filtrage cohérente

Les règles de filtrage doivent être identiques sur toutes les instances.

---

## Réécritures DNS cohérentes

Les réécritures DNS locales doivent être identiques sur toutes les instances.

---

## Disponibilité de la résolution DNS

La perte d'une instance DNS ne doit pas modifier le comportement attendu de la résolution des noms.

---

## Administration simplifiée

L'administration de la configuration DNS doit être réalisée une seule fois.

---

# Principes retenus

## Source de vérité unique

Une seule configuration fait autorité.

Les autres instances sont synchronisées automatiquement.

---

## Synchronisation automatique

La cohérence de la configuration ne doit pas dépendre d'interventions manuelles.

---

## Transparence

Le changement d'une instance DNS ne doit pas être perceptible par les équipements du réseau.

---

## Évolutivité

L'ajout d'une nouvelle instance DNS ne doit pas remettre en cause cette architecture.

---

# Conséquences

## Avantages

- comportement DNS prévisible ;
- administration simplifiée ;
- réduction des erreurs humaines ;
- meilleure résilience ;
- préparation à l'automatisation par Ohana-Agent.

## Inconvénients

- nécessité d'un mécanisme de synchronisation ;
- supervision supplémentaire.

Ces contraintes sont considérées comme acceptables.

---

# Alternatives étudiées

## Administration manuelle des deux serveurs

Non retenue.

Le risque de divergence est trop important.

---

## Serveur DNS unique

Non retenu.

Il introduit un point de défaillance unique.

---

## Synchronisation ponctuelle

Non retenue.

La cohérence doit être permanente.

---

# Décisions dérivées

Cette décision contribue notamment à :

- ADR-002 — Supervision des capacités
- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-006 — Sauvegarde et restauration d'INFRA-01

---

# Références

- Architecture-Reference.md
- Architecture-Conventions.md
- ADR-001 — Autonomie locale de l'infrastructure
- ADR-002 — Supervision des capacités
- ADR-003 — Services d'infrastructure (INFRA-01)

---

# Conclusion

La capacité de résolution DNS repose sur plusieurs instances fonctionnant comme un service unique.

La cohérence de leur configuration constitue une propriété fondamentale de l'architecture.

Les mécanismes de synchronisation pourront évoluer sans remettre en cause cette décision.
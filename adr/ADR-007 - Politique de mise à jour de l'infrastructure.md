# ADR-007 — Politique de mise à jour de l'infrastructure

> **Statut :** ✅ Accepté
>
> **Date :** 2026-07-06
>
> **Décideurs :** Projet Ohana-House
>
> **Impact :** Important

---

# Contexte

L'infrastructure Ohana-House est composée de plusieurs machines assurant des capacités complémentaires.

Chaque mise à jour comporte un risque potentiel :

- indisponibilité temporaire ;
- régression fonctionnelle ;
- incompatibilité logicielle ;
- perte de configuration.

Une politique commune est nécessaire afin de garantir que les évolutions de l'infrastructure restent maîtrisées.

---

# Problème

Une mise à jour réalisée sans méthode peut provoquer :

- une interruption de service ;
- une perte de capacités ;
- des incompatibilités entre composants ;
- une restauration complexe.

Les mises à jour doivent être considérées comme des opérations d'architecture et non comme de simples opérations de maintenance.

---

# Décision

Toutes les mises à jour de l'infrastructure suivent un processus commun.

Chaque évolution doit pouvoir être :

- préparée ;
- réalisée ;
- vérifiée ;
- annulée si nécessaire.

La stabilité de l'infrastructure est prioritaire sur l'adoption immédiate des nouvelles versions.

---

# Capacités garanties

---

## Continuité de service

Les mises à jour doivent limiter au maximum l'indisponibilité des capacités de la maison.

---

## Traçabilité

Chaque mise à jour doit être documentée.

---

## Restaurabilité

Une stratégie de retour arrière doit exister avant toute mise à jour importante.

---

## Validation

Le bon fonctionnement des capacités doit être vérifié après chaque mise à jour.

---

## Cohérence

Les différents composants doivent rester compatibles entre eux.

---

# Principes retenus

## Sauvegarde préalable

Toute mise à jour est précédée d'une sauvegarde adaptée.

---

## Validation fonctionnelle

La réussite d'une mise à jour est évaluée par la disponibilité des capacités, et non uniquement par l'absence d'erreur technique.

---

## Documentation

Toute évolution significative est reportée dans la documentation de référence.

---

## Prudence

Les versions stables sont privilégiées.

Les mises à jour sont réalisées lorsque leur bénéfice est supérieur au risque qu'elles introduisent.

---

## Mise à jour progressive

Les composants sont mis à jour progressivement.

Chaque étape est suivie d'une validation des capacités concernées avant de poursuivre.

L'ordre précis des mises à jour relève des procédures d'exploitation documentées dans Naruto.

---

# Conséquences

## Avantages

- réduction du risque de régression ;
- meilleure stabilité ;
- restauration facilitée ;
- historique des évolutions ;
- meilleure maîtrise de l'infrastructure.

## Inconvénients

- processus de mise à jour plus long ;
- nécessité de réaliser des vérifications intermédiaires.

Ces contraintes sont jugées acceptables.

---

# Alternatives étudiées

## Mise à jour automatique de tous les composants

Non retenue.

Elle ne permet pas de contrôler les régressions.

---

## Mise à jour sans sauvegarde préalable

Non retenue.

Le retour arrière doit rester possible.

---

## Mise à jour sans validation fonctionnelle

Non retenue.

Une mise à jour réussie doit être évaluée par les capacités réellement disponibles.

---

# Décisions dérivées

Cette décision conduit notamment à :

- des procédures de mise à jour dans Naruto ;
- une supervision post-mise à jour ;
- une automatisation future par Ohana-Agent.

---

# Références

- Architecture-Reference.md
- Architecture-Conventions.md
- ADR-001 — Autonomie locale de l'infrastructure
- ADR-002 — Supervision des capacités
- ADR-006 — Sauvegarde et restauration d'INFRA-01

---

# Conclusion

Les mises à jour constituent des évolutions de l'architecture.

Elles doivent préserver les capacités de la maison, garantir la possibilité d'un retour arrière et maintenir la cohérence de l'ensemble de l'infrastructure.

La stabilité reste prioritaire sur la nouveauté.
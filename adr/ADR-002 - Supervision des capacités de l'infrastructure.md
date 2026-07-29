# ADR-002 — Supervision des capacités de l'infrastructure

> **Statut :** ✅ Accepté
>
> **Date :** 2026-07-06
>
> **Décideurs :** Projet Ohana-House
>
> **Impact :** Majeur

---

# Contexte

L'infrastructure Ohana-House repose sur plusieurs capacités essentielles.

Une supervision limitée à l'état des processus logiciels ne permet pas de garantir que ces capacités sont réellement disponibles.

Une approche indépendante des technologies est nécessaire.

---

# Problème

Un logiciel peut être actif tout en étant incapable de fournir la capacité attendue.

Par exemple :

- un service DNS peut être démarré sans résoudre les noms ;
- un serveur DHCP peut être actif sans attribuer d'adresse ;
- un courtier MQTT peut être lancé sans accepter de publication.

La supervision doit donc mesurer les capacités réellement offertes à la maison.

---

# Décision

La supervision est organisée autour des capacités de l'infrastructure.

Chaque capacité est vérifiée par un contrôle fonctionnel.

Les logiciels utilisés pour fournir cette capacité ne constituent pas l'objet de la supervision.

---

# Capacités garanties

---

## Attribution des adresses IP

Vérifier qu'un équipement peut obtenir une adresse IP.

---

## Résolution DNS

Vérifier que les noms peuvent être résolus.

---

## Référence temporelle

Vérifier qu'une heure cohérente est disponible.

---

## Automatisation

Vérifier que Home Assistant répond.

---

## Communication domotique

Vérifier que les échanges avec les équipements restent possibles.

---

## Téléinformation

Vérifier que les données énergétiques continuent d'être publiées.

---

## Connectivité Internet

Vérifier l'accès aux services externes.

---

## Santé matérielle

Surveiller :

- processeur ;
- mémoire ;
- stockage ;
- température ;
- disponibilité.

---

# Principes retenus

## Capacité avant logiciel

Les contrôles portent sur les résultats obtenus.

---

## Supervision fonctionnelle

Les contrôles reproduisent le comportement réel d'un utilisateur ou d'un équipement.

---

## Dégradation maîtrisée

Les états de santé distinguent :

- fonctionnement normal ;
- fonctionnement dégradé ;
- panne.

---

## Standardisation

Tous les contrôles produisent un résultat homogène.

---

# Conséquences

## Avantages

- supervision indépendante des technologies ;
- meilleure détection des défaillances réelles ;
- préparation à Ohana-Agent ;
- tableaux de bord plus représentatifs.

## Inconvénients

- contrôles plus élaborés ;
- maintenance des scénarios de test.

Ces contraintes sont jugées acceptables.

---

# Alternatives étudiées

## Vérification des processus

Non retenue.

Elle ne garantit pas la disponibilité réelle des capacités.

---

## Vérification par ping

Non retenue.

La connectivité réseau seule est insuffisante.

---

## Supervision spécifique aux logiciels

Non retenue.

Elle crée une dépendance forte aux technologies employées.

---

# Décisions dérivées

- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-007 — Politique de mise à jour de l'infrastructure
- ADR futur - Ohana-Agent

---

# Références

- Architecture-Reference.md
- Architecture-Conventions.md
- ADR-001 — Autonomie locale de l'infrastructure

---

# Conclusion

La supervision de l'infrastructure mesure les capacités réellement offertes à la maison.

Les technologies employées peuvent évoluer sans remettre en cause cette décision d'architecture.
# ADR-003 — Services d'infrastructure (INFRA-01)

> **Statut :** ✅ Accepté
>
> **Date :** 2026-07-06
>
> **Décideurs :** Projet Ohana-House
>
> **Impact :** Majeur

---

# Contexte

L'architecture Ohana-House repose sur plusieurs machines spécialisées, chacune ayant une responsabilité clairement identifiée.

La mise en œuvre du principe d'autonomie locale (ADR-001) nécessite toutefois qu'un ensemble de capacités fondamentales soit assuré indépendamment de la Freebox et des applications domotiques.

Afin de regrouper ces responsabilités, une machine dédiée est introduite dans l'architecture : **INFRA-01**.

---

# Problème

Les capacités fondamentales de l'infrastructure étaient historiquement réparties entre plusieurs équipements ou dépendaient directement de la Freebox.

Cette organisation :

- augmente les dépendances ;
- complique les restaurations ;
- rend les responsabilités moins lisibles ;
- couple fortement les services entre eux.

Une architecture plus robuste nécessite de centraliser les capacités communes tout en conservant une séparation claire avec les services domotiques.

---

# Décision

Une machine dédiée nommée **INFRA-01** est créée.

Sa mission consiste à garantir les capacités fondamentales nécessaires au fonctionnement de l'infrastructure locale.

Les applications domotiques restent hébergées sur leurs machines spécialisées.

---

# Capacités garanties

INFRA-01 garantit les capacités suivantes.

---

## Attribution des adresses IP

Garantir qu'un équipement puisse obtenir une adresse IP sur le réseau local, indépendamment de la Freebox.

---

## Distribution d'une référence temporelle

Garantir qu'une heure cohérente soit disponible pour l'ensemble des équipements.

---

## Synchronisation de la configuration DNS

Garantir la cohérence des deux instances AdGuard.

---

## Supervision de l'infrastructure

Garantir une vision centralisée de l'état des capacités de la maison.

---

## Administration

Garantir la disponibilité des outils nécessaires à l'exploitation quotidienne.

Exemples :

- sauvegardes ;
- synchronisations ;
- diagnostics ;
- maintenance.

---

# Capacités explicitement exclues

Les capacités suivantes ne relèvent pas d'INFRA-01.

| Machine | Capacités |
|-----------|-----------|
| BOX-01 | Accès Internet, NAT, routage |
| HA-01 | Automatisation de la maison |
| ZWAVE-01 | Z-Wave, DNS principal |
| LINKY-01 | Téléinformation, DNS secondaire |

Cette séparation garantit une responsabilité unique pour chaque machine.

---

# Principes retenus

## Responsabilité unique

Chaque machine possède une mission principale, mais peut fournir plusieurs capacités complémentaires lorsque cela améliore la résilience ou simplifie l'architecture.

---

## Infrastructure indépendante

Les capacités fondamentales restent indépendantes des applications domotiques.

---

## Centralisation des capacités

Les capacités communes sont regroupées sur une seule machine.

---

## Simplicité

La solution retenue privilégie une architecture simple à comprendre, documenter et restaurer.

---

## Évolutivité

Le remplacement d'un logiciel ne doit jamais remettre en cause la décision d'architecture.

Les implémentations pourront évoluer indépendamment de cet ADR.

---

# Conséquences

## Avantages

- responsabilités clairement réparties ;
- architecture plus lisible ;
- restauration facilitée ;
- réduction des dépendances ;
- préparation naturelle à Ohana-Agent ;
- indépendance vis-à-vis des technologies utilisées.

## Inconvénients

- apparition d'un composant supplémentaire ;
- nécessité de sauvegarder INFRA-01 ;
- point de défaillance unique.

Ce point de défaillance est accepté car il est :

- documenté ;
- sauvegardé ;
- rapidement restaurable.

---

# Alternatives étudiées

## Conserver les capacités sur la Freebox

Non retenu.

La dépendance au matériel du fournisseur d'accès reste trop importante.

---

## Répartir les capacités sur plusieurs machines

Non retenu.

La multiplication des responsabilités complique l'exploitation et la restauration.

---

## Héberger les capacités sur HA-01

Non retenu.

Les applications domotiques doivent rester indépendantes des services fondamentaux de l'infrastructure.

---

# Décisions dérivées

Cette décision conduit notamment aux ADR suivants :

- ADR-004 — Cohérence des serveurs DNS
- ADR-005 — Politique d'adressage IP
- ADR-006 — Sauvegarde et restauration d'INFRA-01
- ADR-007 — Politique de mise à jour

---

# Références

- Architecture-Reference.md
- Architecture-Conventions.md
- ADR-001 — Autonomie locale de l'infrastructure
- ADR-002 — Supervision des capacités

---

# Conclusion

INFRA-01 constitue le socle technique de l'infrastructure Ohana-House.

Sa mission n'est pas d'héberger des logiciels particuliers, mais de garantir les capacités fondamentales nécessaires au fonctionnement autonome de la maison.

Les technologies utilisées pour fournir ces capacités pourront évoluer sans remettre en cause cette décision d'architecture.
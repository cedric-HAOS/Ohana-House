# Architecture Reference

> Document de référence de l'architecture cible d'Ohana-House.
>
> L’état réellement déployé est décrit dans `Etat-Actuel.md`.
>
> Ce document décrit l'architecture fonctionnelle de l'infrastructure.
> Il constitue la référence de conception du projet Hashirama.
>
> Les Architecture Decision Records (ADR) détaillent les décisions ayant conduit à cette architecture.

---

# Statut

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Phase | Hashirama |
| Version | 2.0 |
| Statut | 🟢 Validé |

---

# 1. Vision

L'objectif d'Ohana-House est de construire une infrastructure :

- autonome ;
- documentée ;
- résiliente ;
- simple à maintenir ;
- évolutive.

L'infrastructure doit continuer à assurer les fonctions essentielles même en cas de perte d'Internet ou de la Freebox.

---

# 2. Modèle architectural

L'architecture d'Ohana-House repose sur trois niveaux complémentaires :

Mission
↓
Capacité
↓
Implémentation

Les missions décrivent le rôle principal de chaque machine.

Les capacités décrivent les fonctions garanties par l'architecture.

Les implémentations correspondent aux technologies retenues pour fournir ces capacités et sont documentées dans Naruto.

---

# 3. Principes d'architecture

## Principe 1

Les décisions sont prises en fonction des capacités offertes à la maison, et non des logiciels utilisés.

## Principe 2

Chaque machine possède une mission principale clairement identifiée et peut fournir des capacités complémentaires lorsque cela améliore la résilience ou simplifie l'architecture.

## Principe 3

L'autonomie locale est prioritaire sur les services Cloud.

## Principe 4

Les services critiques privilégient les liaisons Ethernet.

## Principe 5

Une panne ne doit provoquer qu'une dégradation progressive des capacités.

## Principe 6

Les points de défaillance uniques sont acceptés uniquement lorsqu'ils sont documentés, sauvegardés et rapidement restaurables.

---

# 4. Capacités

## Niveau 1 — Infrastructure

- Attribution des adresses IP
- Résolution DNS
- Référence temporelle
- Automatisation

## Niveau 2 — Capacités domotiques

- Communication domotique
- Téléinformation
- Pilotage Z-Wave
- Pilotage Shelly
- Pilotage ESPHome
- Pilotage Velux

## Niveau 3 — Capacités externes

- Internet
- VPN
- Notifications
- Service Cloud
- Mises à jour

---

# 5. Architecture cible

                     Internet
                         │
                     BOX-01
               Modem • Routeur • NAT
                         │
─────────────────────────┼─────────────────────────
                         │
                  Infrastructure LAN
                         │
       ┌─────────┬──────────┬──────────┬──────────┐
       │         │          │          │
    HA-01    INFRA-01   ZWAVE-01   LINKY-01

---

# 6. Responsabilités

| Machine  | Mission principale    | Capacités complémentaires            |
|----------|-----------------------|--------------------------------------|
| BOX-01   | Connectivité Internet | NAT, Routage                         |
| HA-01    | Automatisation        | Communication MQTT                   |
| INFRA-01 | Infrastructure        | Administration, Supervision          |
| ZWAVE-01 | Z-Wave                | Résolution DNS principale            |
| LINKY-01 | Téléinformation       | Résolution DNS secondaire            |

---

## Capacités complémentaires

### HA-01

- Communication MQTT

### INFRA-01

- Attribution des adresses IP
- Référence temporelle
- Supervision
- Administration

### ZWAVE-01

- Résolution DNS principale

### LINKY-01

- Résolution DNS secondaire

---

# 7. Flux principaux

Capacité : Pilotage des équipements

Capacité : Téléinformation

Capacité : Résolution DNS

Capacité : Attribution des adresses IP

Capacité : Référence temporelle

---

# 8. Plan d'adressage

| Plage | Usage |
|------:|-------|
| .1 | BOX-01 |
| .2-.9 | Réserve infrastructure |
| .10-.19 | Services d'infrastructure |
| .20-.29 | Serveurs domotiques |
| .30-.39 | Infrastructure réseau |
| .40-.49 | Passerelles domotiques |
| .50-.99 | Équipements critiques |
| .100-.199 | DHCP dynamique |
| .200-.254 | Réserve |

Adresses cibles des composants structurants :

| Identifiant | Adresse cible |
|---|---:|
| BOX-01 | 192.168.1.1 |
| INFRA-01 | 192.168.1.10 |
| ZWAVE-01 | 192.168.1.11 |
| LINKY-01 | 192.168.1.12 |
| HA-01 | 192.168.1.20 |

---

# 9. Paramètres réseau

Passerelle : BOX-01
DNS principal : ZWAVE-01
DNS secondaire : LINKY-01
Serveur DHCP : INFRA-01
Serveur NTP : INFRA-01

---

# 10. Dégradation maîtrisée

La perte d'un composant ne doit entraîner que la perte de la capacité assurée par celui-ci.

L'objectif est de maintenir le fonctionnement local de la maison aussi longtemps que possible.

---

# 11. Documents associés

- HASHIRAMA.md
- Architecture-Conventions.md
- ADR/
- Documentation Naruto

---

# Conclusion

Une architecture n'est pas définie par les logiciels qu'elle utilise.

Elle est définie par les missions qu'elle remplit et les capacités qu'elle garantit.
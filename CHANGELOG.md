# Changelog

## [2.0.0-Hashirama] - 2026-07-29

### Corrigé

- orthographe unique `Ohana` dans tout le dépôt ;
- séparation de l'état actuellement déployé et de l'architecture cible ;
- plan d'adressage sans collision active avec INFRA-01 ;
- identifiants unifiés BOX-01, INFRA-01, LINKY-01, ZWAVE-01 et HA-01 ;
- statut Hashirama aligné sur la version stable ;
- intégration documentaire avec Platform, Agent, Vision et Installer ;
- noms de fichiers ADR restaurés en UTF-8.

### Ajout

- `Etat-Actuel.md`.

- HASHIRAMA.md
- Architecture-Reference.md
- Architecture-Conventions.md
- ADR-001 — Autonomie locale de l'infrastructure
- ADR-002 — Supervision des capacités de l'infrastructure
- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-004 — Cohérence des serveurs DNS
- ADR-005 — Politique d'adressage IP
- ADR-006 — Sauvegarde et restauration d'INFRA-01
- ADR-007 — Politique de mise à jour de l'infrastructure

### Architecture

- Définition de l'architecture de référence
- Introduction du modèle « Mission → Capacité → Implémentation »
- Définition des missions des machines
- Définition des capacités de l'infrastructure
- Définition de la stratégie d'autonomie locale
- Définition de la politique d'adressage IP
- Définition des conventions d'architecture

### Décisions

- Création du rôle INFRA-01
- Centralisation des capacités d'infrastructure
- Serveur DHCP dédié
- Serveur NTP dédié
- DNS principal assuré par ZWAVE-01
- DNS secondaire assuré par LINKY-01
- Synchronisation automatique des serveurs DNS
- Supervision orientée capacités
- Politique de sauvegarde d'INFRA-01
- Politique de mise à jour de l'infrastructure

### Gouvernance

- Introduction des Architecture Decision Records (ADR)
- Séparation entre architecture (Hashirama) et implémentation (Naruto)
- Standardisation des conventions d'architecture
- Intégration avec l'écosystème Ohana

---

## [1.0.0-Naruto]

### Ajout

- Documents d'exploitation
- Procédures d'installation
- Procédures de configuration
- Procédures de sauvegarde
- Procédures de maintenance
- Procédures de restauration
- Guide de reconstruction
- Chemin critique de reconstruction
- Validation finale
- START-HERE.md

### Amélioration

- Standardisation complète des procédures
- Harmonisation de la documentation
- Structuration du cycle de vie des composants
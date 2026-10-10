# Changelog

## Non publié

- Contrôle documentaire D01/D02 : restauration INFRA-01 avec Installer 1.15.6
  minimum, permissions rclone et conservation de l'identité de déchiffrement
  locale/cloud avec une copie indépendante.
- D03/D08 : reconstruction complète intégrant INFRA-01 et Ohana, checklist
  datée et états consolidés à partir des preuves historiques, avec les
  vérifications post-restauration encore à recueillir.
- D11/D15 : références remplacées par les procédures existantes, périmètre
  HAOS explicité et séquence Téléinformation avec flux HTTP/MQTT indépendants.

## [2.2.1] - 2026-10-09

### Corrigé

- Option du service `adguardhome-sync` corrigée en `--runOnStart=true`, compatible
  avec le binaire 0.9.3 ; l'ancienne option empêchait la réplication vers LINKY-01.
- Modèle systemd et procédure d'installation alignés.

Le cycle corrigé a réussi sur INFRA-01 le 09/10/2026 à 16:57 : 38 noms réservés
vérifiés sur ZWAVE-01, réplication vers LINKY-01 et comparaison API réussies.
Les deux DNS répondent `192.168.1.20` pour `ha-01.ohana.lan` selon les sorties
fournies par l'opérateur. L'activation du timer et la recette pendant une panne
d'INFRA-01 restent à confirmer. Agent 1.45.0 et Platform 1.0.140 sont inchangés.

## [2.2.0] - 2026-10-09

### Ajouté

- Réplication des noms des seules réservations DHCP INFRA-01 vers AdGuard Home
  sur ZWAVE-01, puis copie vers LINKY-01 par `adguardhome-sync`.
- Modèles de configuration, service et timer systemd ; vérification des règles
  par API, procédure de recette DNS et retour arrière.
- Parcours de reconstruction après panne de carte SD : restaurer les versions
  sauvegardées, mettre à jour vers Platform 1.0.140 / Agent 1.45.0, puis installer
  et activer explicitement le cycle DNS.

### Modifié

- Configuration et registre DNS sous `/etc/ohana-agent` pour leur inclusion
  dans les prochaines sauvegardes chiffrées. Les anciennes archives ne sont
  ni modifiées ni rendues incompatibles.
- État d'INFRA-01 indiqué indisponible selon le signalement du 09/10/2026.
- ESP-03 reste le futur DHCP de secours, avec conservation des températures
  piscine ; aucune configuration ESPHome n'est modifiée dans cette release.

Cette release publie la préparation et la documentation ; la reconstruction
et la validation en production restent à réaliser.

## [2.1.0] - 2026-08-13

### Ajouté

- procédures de sauvegarde logique et de restauration d'INFRA-01 avec
  Ohana-Agent, Vision et Ohana-Installer ;
- conservation de la clé privée `age` hors d'INFRA-01 ;
- rétention iCloud sûre, désactivée par défaut ;
- restauration DHCP inactive jusqu'à confirmation de l'arrêt de l'ancien
  serveur DHCP.

### Modifié

- l'installation et la configuration de dnsmasq et Chrony deviennent des
  capacités du profil INFRA-01 provisionnées par Ohana-Installer ;
- les procédures manuelles sont conservées comme référence de diagnostic et
  non comme parcours d'installation nominal.

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

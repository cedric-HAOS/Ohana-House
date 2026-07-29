# Standard de documentation

## Structure

Tous les documents suivent la structure suivante :

Cartouche

1. Introduction

2. ...

Documents associés

---

## Titres

Toujours des titres H1, H2, H3.

---

## Tableaux

Les tableaux sont privilégiés lorsque l'information est structurée.

---

## Diagrammes

Les diagrammes Mermaid sont référencés par leur identifiant DGM-xxx.

---

## Historique

Jamais d'historique dans les documents.

Git est la source de vérité.

---

## Qualité

🟡 Brouillon

🔵 Révision

🟢 Validé

🟣 Référence

---

# Types de documents

La documentation est organisée en deux catégories.

## Documents d'architecture

Les documents d'architecture décrivent l'organisation générale de l'infrastructure.

Ils présentent les principes de fonctionnement, les choix techniques et les interactions entre les différents composants.

Ils utilisent la structure suivante :

- Cartouche
- Introduction
- Contenu spécifique au document
- Documents associés
- Phrase de référence

Exemples :

- Architecture.md
- Topologie-Reseau.md
- Architecture-Logique.md
- Inventaire.md
- Adressage-IP.md
- Capacites-Reseau.md
- Decisions-d-Architecture.md

---

## Documents d'exploitation

Les documents d'exploitation décrivent un composant de l'infrastructure.

Ils utilisent systématiquement la structure suivante :

1. Introduction
2. Fiche d'identité
3. Responsabilités
4. Configuration
5. Connexions
6. Dépendances
7. Criticité
8. Sauvegarde
9. Maintenance
10. Historique fonctionnel
11. Évolutions prévues
12. Documents associés

Cette structure garantit une documentation homogène et facilite la recherche d'informations.

---

## Chaîne réseau

Les documents décrivant un équipement réseau doivent situer celui-ci dans la chaîne de communication.

Cette information est présentée sous la forme d'un tableau.

Exemple :

| Amont | Équipement | Aval |
|--------|------------|------|
| SW-01 | AP-01 | LINKY-01 |

Cette représentation complète les diagrammes Mermaid sans les remplacer.

---

# Organisation documentaire

Les documents sont organisés selon leur responsabilité.

## Architecture

Décrit les principes généraux de l'infrastructure.

## Réseau

Décrit les équipements réseau physiques.

## Services

Décrit les services indépendants de la plateforme domotique.

## Home Assistant

Décrit la plateforme Home Assistant et ses composants propres.

## Procédures

Décrit les opérations d'installation, de maintenance et de restauration.

---

# Modèles de documents

Afin de garantir une documentation homogène, chaque catégorie de document suit un modèle de rédaction.

## Documents d'exploitation

Les documents d'exploitation décrivent un équipement ou un service particulier.

Ils utilisent systématiquement la structure suivante :

1. Introduction
2. Fiche d'identité
3. Position dans l'infrastructure
4. Responsabilités
5. Configuration
6. Dépendances
7. Criticité
8. Sauvegarde
9. Maintenance
10. Historique fonctionnel
11. Évolutions prévues
12. Documents associés

Chaque document doit rester centré sur son unique responsabilité.

Les informations relatives à l'installation, la configuration détaillée, la maintenance, la sauvegarde, la restauration ou la migration sont décrites dans les procédures correspondantes.

Les documents d'exploitation décrivent le composant.

Les procédures décrivent les opérations réalisées sur ce composant..

---

## Documents d'architecture

Les documents d'architecture décrivent l'organisation générale de l'infrastructure.

Leur structure est adaptée au sujet traité mais comprend généralement :

- Introduction
- Description de l'architecture
- Analyse
- Documents associés

Ils décrivent les principes de conception et les interactions entre les composants, sans détailler leur configuration.

---

## Procédures

Les procédures décrivent une opération à réaliser.

Elles peuvent concerner :

- une installation ;
- une configuration ;
- une mise à jour ;
- une sauvegarde ;
- une restauration ;
- une migration.

Une procédure doit permettre de reproduire une opération de manière fiable, sans nécessiter de connaissances implicites.

## Types de procédures

Deux catégories de procédures sont utilisées dans le projet.

### Procédure d'installation

Une procédure d'installation décrit les opérations permettant de rendre un composant opérationnel.

Elle utilise la structure suivante :

1. Objectif
2. Contexte
3. Prérequis
4. Niveau de risque
5. Impact
6. Procédure
7. Vérifications
8. Retour arrière
9. Documents associés

---

### Procédure de configuration

Une procédure de configuration décrit les opérations permettant d'appliquer la configuration de référence d'Ohana-House à un composant.

Elle utilise la structure suivante :

1. Objectif
2. Contexte
3. Prérequis
4. Niveau de risque
5. Impact
6. Procédure
7. Configuration appliquée
8. Vérifications
9. Retour arrière
10. Documents associés

---

### Contenu des procédures

Une procédure doit permettre :

- de préparer l'intervention ;
- d'exécuter les opérations dans le bon ordre ;
- de vérifier le bon déroulement de l'opération ;
- de revenir à l'état précédent en cas d'échec.

Les informations décrivant un composant ne doivent pas être dupliquées dans une procédure mais référencées dans les documents d'exploitation correspondants.

---

## Rôles dans l'architecture

Chaque composant de l'infrastructure possède un rôle dans l'architecture.

Ce rôle décrit sa contribution au fonctionnement global de l'infrastructure.

Le rôle est distinct de la fonction principale du composant.

### Rôles de référence

| Rôle | Description |
|------|-------------|
| Orchestrateur | Coordonne les services, les automatisations et les interactions entre les composants. |
| Passerelle | Assure la communication entre deux réseaux, protocoles ou systèmes. |
| Distribution | Distribue le trafic réseau entre les différents équipements. |
| Collecte | Acquiert des données provenant d'un équipement ou d'un système externe. |
| Messagerie | Transporte les messages entre plusieurs composants. |
| Résolution DNS | Assure la résolution des noms de domaine et le filtrage DNS. |
| Accès distant | Permet l'administration sécurisée de l'infrastructure depuis l'extérieur. |
| Accès radio | Fournit une connectivité réseau sans fil aux équipements. |

De nouveaux rôles pourront être ajoutés si l'évolution de l'infrastructure le nécessite.

Le nombre de rôles doit rester limité afin de conserver une architecture simple et homogène.

## Modèles de procédures

Les procédures décrivent une opération permettant d'installer, configurer, maintenir, sauvegarder, restaurer ou faire évoluer un composant de l'infrastructure.

Contrairement aux documents d'exploitation, une procédure décrit **comment réaliser une action**.

Les procédures utilisent systématiquement la structure suivante :

1. Objectif
2. Contexte
3. Prérequis
4. Niveau de risque
5. Impact
6. Procédure
7. Vérifications
8. Retour arrière
9. Documents associés

---

### Style de rédaction

Les procédures sont rédigées sous forme d'instructions.

Chaque étape doit commencer par un verbe d'action clairement identifiable.

Exemples :

- Connecter le Raspberry Pi au réseau.
- Installer Home Assistant OS.
- Vérifier que le service est démarré.
- Contrôler les journaux système.

Les explications théoriques doivent rester limitées au strict nécessaire.

L'objectif d'une procédure est de permettre la réalisation d'une opération de manière fiable et reproductible.

---

### Navigation dans les interfaces

Lorsqu'une procédure décrit un chemin de navigation dans une interface graphique, celui-ci doit être présenté sous forme d'un bloc dédié.

Exemple :

```text
Paramètres
→ Modules complémentaires
→ Boutique des modules complémentaires
```

Chaque niveau de navigation est présenté sur une ligne distincte et relié au suivant par le symbole `→`.

Cette présentation est utilisée afin d'améliorer la lisibilité des procédures et d'uniformiser leur rédaction.

Les chemins de navigation ne doivent pas être rédigés sous forme de phrase.

---

### Noms officiels

Les noms des logiciels, modules complémentaires, intégrations et services doivent être écrits en utilisant leur nom officiel.

Exemples :

- Home Assistant Green
- Mosquitto Broker
- Z-Wave JS UI
- AdGuard Home

Les traductions, abréviations ou appellations approximatives doivent être évitées afin de limiter toute ambiguïté.
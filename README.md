<div align="center">

# Ohana-House

Documentation technique de l'infrastructure informatique et domotique de la
maison, déploiement de référence de l'écosystème Ohana.

![Version](https://img.shields.io/badge/stable-v1.0.0%20Naruto-blue)
![Status](https://img.shields.io/badge/status-active-orange)
![Branch](https://img.shields.io/badge/branch-Hashirama-purple)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

</div>

## Présentation

Ohana-House décrit :

- l'architecture physique et logique ;
- les équipements réseau et domotiques ;
- les services installés ;
- les procédures d'installation, d'exploitation et de restauration ;
- les décisions et standards techniques ;
- le déploiement de référence d'Ohana-Agent et d'Ohana-Vision.

L'objectif est qu'une installation puisse être comprise, maintenue et
reconstruite sans dépendre uniquement de la mémoire de son administrateur.

## État du projet

| Élément | Valeur |
| --- | --- |
| Release stable | `v1.0.0-Naruto` |
| Branche de développement | `Hashirama` |
| Prochaine release | `v2.0.0-Hashirama` |

Les détails sont maintenus dans [PROJECT-STATE.md](PROJECT-STATE.md) et
[ROADMAP.md](ROADMAP.md).

## Structure

```text
Ohana-House/
├── adr/
├── diagrams/
│   ├── flows/
│   ├── logical/
│   └── physical/
├── docs/
│   ├── architecture/
│   ├── home-assistant/
│   ├── network/
│   ├── procedures/
│   ├── services/
│   └── standards/
├── CHANGELOG.md
├── Chemin-Critique-de-Reconstruction.md
├── Guide-de-Reconstruction.md
├── HASHIRAMA.md
├── PROJECT-STATE.md
├── ROADMAP.md
├── START-HERE.md
└── Validation-Finale.md
```

## Documents principaux

- [Point d'entrée](START-HERE.md)
- [Architecture](docs/architecture/Architecture.md)
- [Topologie réseau](docs/architecture/Topologie-Reseau.md)
- [Inventaire](docs/architecture/Inventaire.md)
- [Administrer l'infrastructure avec Vision](docs/procedures/configuration/Administrer-Ohana-avec-Vision.md)
- [Guide de reconstruction](Guide-de-Reconstruction.md)
- [Chemin critique de reconstruction](Chemin-Critique-de-Reconstruction.md)
- [Validation finale](Validation-Finale.md)
- [Standards documentaires](docs/standards/Documentation.md)

## Domaines couverts

| Domaine | Contenu |
| --- | --- |
| Réseau | Freebox Pop, commutateurs, Wi-Fi, DNS et WireGuard |
| Domotique | Home Assistant, MQTT, Z-Wave et Linky |
| Exploitation | Installation, configuration, sauvegarde, maintenance, restauration et migration |
| Standards | Versionnement, nommage et rédaction documentaire |

## Diagrammes

Les diagrammes officiels sont rédigés en Mermaid dans `diagrams/`.

| ID | Diagramme |
| --- | --- |
| DGM-001 | Architecture physique |
| DGM-002 | Topologie réseau |
| DGM-003 | Architecture logique |
| DGM-004 | Flux MQTT |
| DGM-005 | Flux Z-Wave |
| DGM-006 | Flux DNS / WireGuard |

## Licence

Ce projet est distribué sous licence MIT. Voir [LICENSE](LICENSE).

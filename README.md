<div align="center">

# Ohana-House

Architecture, documentation et exploitation de l'infrastructure informatique et
domotique de référence d'Ohana.

![Version](https://img.shields.io/badge/version-v2.0%20Hashirama-blue)
![Documentation](https://img.shields.io/badge/documentation-référence-green)
![Status](https://img.shields.io/badge/status-stable-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

</div>

## Présentation

**Konoha** est le nom fonctionnel de l'infrastructure ou de la maison gérée par
Ohana. **Ohana-House** reste le nom technique de ce dépôt documentaire : il
décrit l'instance domestique de référence, ses équipements, ses services, ses
procédures et les décisions qui encadrent son évolution.

Le dépôt distingue volontairement trois niveaux :

1. **état actuellement déployé**, décrit dans [`Etat-Actuel.md`](Etat-Actuel.md) ;
2. **architecture cible Hashirama**, décrite dans
   [`Architecture-Reference.md`](Architecture-Reference.md) ;
3. **migrations restantes**, suivies dans [`ROADMAP.md`](ROADMAP.md).

Cette distinction évite de présenter comme déjà déployée une adresse, une
capacité ou une responsabilité encore en cours de migration.

## Relation avec l'écosystème Ohana

| Projet | Rôle |
|---|---|
| Ohana-Platform | architecture commune et composition des releases |
| Ohana-Agent | runtime hébergeant Shikamaru et Tsunade |
| Ohana-Vision | cockpit technique de Konoha et administration via Agent |
| Ohana-Installer | installation et mise à jour Linux/systemd |
| Ohana-House | documentation du déploiement Konoha réel et cible |

Ohana-House documente le déploiement. La configuration opérationnelle utilisée
par Vision reste portée par Ohana-Agent.

## Structure du dépôt

```text
Ohana-House/
├── README.md
├── START-HERE.md
├── Etat-Actuel.md
├── PROJECT-STATE.md
├── ROADMAP.md
├── CHANGELOG.md
├── HASHIRAMA.md
├── Architecture-Reference.md
├── Architecture-Conventions.md
├── adr/
├── diagrams/
└── docs/
    ├── architecture/
    ├── home-assistant/
    ├── network/
    ├── procedures/
    ├── services/
    └── standards/
```

## Documents principaux

- [`START-HERE.md`](START-HERE.md) — parcours de lecture ;
- [`Etat-Actuel.md`](Etat-Actuel.md) — état réellement déployé et écarts ;
- [`Architecture-Reference.md`](Architecture-Reference.md) — cible Hashirama ;
- [`docs/architecture/Adressage-IP.md`](docs/architecture/Adressage-IP.md) —
  adressage actuel et cible ;
- [`docs/architecture/Inventaire.md`](docs/architecture/Inventaire.md) —
  inventaire des composants ;
- [`Guide-de-Reconstruction.md`](Guide-de-Reconstruction.md) — ordre de
  reconstruction ;
- [`Validation-Finale.md`](Validation-Finale.md) — vérifications finales.

## Diagrammes

Les diagrammes Mermaid de référence sont dans `diagrams/` : architecture
physique, topologie réseau, architecture logique et flux DNS, MQTT, Z-Wave et
WireGuard.

## Version

Hashirama v2.0 est la version documentaire stable. Les composants logiciels
Ohana-Agent, Ohana-Vision et Ohana-Installer évoluent dans leurs propres dépôts
et ne constituent plus des versions futures d'Ohana-House.

## Licence

Projet distribué sous licence MIT.

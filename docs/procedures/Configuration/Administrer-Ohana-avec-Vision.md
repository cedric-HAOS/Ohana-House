# Administrer Ohana-House avec Ohana-Vision

| Élément | Valeur |
|---|---|
| Projet | Ohana-House |
| Procédure | Administration graphique |
| Produits minimaux | Agent 1.2.0, Vision 1.2.0, Installer 1.0.1 |
| Dernière mise à jour | 24/07/2026 |

## Objectif

Cette procédure permet de faire évoluer la topologie de référence sans modifier
manuellement `/etc/ohana-agent/infrastructure.yaml`.

## Cartographie

Dans **Configuration > Architecture**, activer **Déplacer** puis positionner les
équipements sur la grille. Les cellules correspondent aux coordonnées
`column` / `row` du layout physique.

La cartographie peut notamment représenter :

- `BOX-01`, passerelle Internet ;
- `SW-01`, `SW-02` et `SW-03`, commutateurs ;
- `AP-01`, point d'accès Wi-Fi ;
- `INFRA-01`, serveur d'infrastructure ;
- `HA-01`, Home Assistant ;
- les passerelles Z-Wave et Linky.

## Liaisons

Activer **Relier**, sélectionner la source puis la destination. Cette séquence
détermine explicitement si un équipement dépend de la box, de `SW-01`, de
`SW-02`, de `SW-03` ou de `AP-01`.

Cliquer sur une ligne pour modifier :

- la source et la destination ;
- Ethernet, Wi-Fi ou une autre technologie ;
- le sens de communication ;
- le débit ;
- le libellé.

## Services

Cliquer sur un équipement, puis utiliser **Services associés**. Les services de
référence comprennent DHCP, DNS, NTP, MQTT, Home Assistant, Z-Wave et
téléinformation. Chaque service est rattaché au nœud de l'équipement qui
l'héberge.

## Application

Les déplacements et éditions restent des brouillons jusqu'au clic sur
**Appliquer l'architecture**. Ohana-Agent valide alors toutes les références et
écrit la configuration de manière atomique.

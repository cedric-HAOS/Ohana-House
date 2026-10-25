# État documenté de l'infrastructure

Consolidation documentaire : 10 octobre 2026. Ce document rassemble des relevés
datés ; il ne constitue pas une mesure en temps réel ni une nouvelle recette.
La configuration opérationnelle reste portée par Ohana-Agent.

## Reprise après l'incident du 9 octobre

La carte SD d'INFRA-01 a été signalée HS le 9 octobre. Le
[CHANGELOG 2.2.1](CHANGELOG.md) consigne ensuite un cycle DNS réussi sur INFRA-01
à 16:57 : 38 noms réservés vérifiés sur ZWAVE-01, réplication vers LINKY-01 et
comparaison API réussies. Les deux DNS ont répondu `192.168.1.20` pour
`ha-01.ohana.lan`, selon les sorties de l'opérateur.

Ce relevé établit la remise en service du cycle à cet instant. Il ne suffit pas
à certifier tous les services restaurés, l'activation du timer ni la tenue du
cycle pendant une panne d'INFRA-01. Consigner ces contrôles dans
[Validation finale](Validation-Finale.md) et utiliser
[le guide de restauration](docs/INFRA-01/Sauvegarde/Restaurer-INFRA-01.md).

| Élément | Dernière preuve documentaire | Contrôle restant |
|---|---|---|
| INFRA-01 | Cycle DNS exécuté le 09/10 à 16:57 | Services Agent/Vision/Chrony, versions et sauvegarde après reprise à dater |
| Réservations DNS | 38 noms comparés sur les deux AdGuard le 09/10 | Timer actif et scénario de panne à confirmer |
| HA-01 | Réservation/réponse DNS .20 le 09/10 | Inventaire complet à actualiser |
| DHCP principal | Validation et arrêt Freebox cochés dans la roadmap avant consolidation | Exclusivité et nouveau bail après reconstruction à consigner |
| ESP-03 | Prototype local, non qualifié sur le matériel | Compilation/recette matérielle et activation distinctes |

INFRA-01 conserve l'autorité sur DHCP et `ohana.lan` ; ZWAVE-01 et LINKY-01
hébergent les DNS. ESP-03 conserve ses températures piscine et reste un secours
en préparation. Les versions de dépôts disponibles ne prouvent pas leur
installation sur ces machines.

## Relevé en lecture seule du 25 octobre 2026

Pris à 10:50-11:05 (heure de Paris) par ssh en lecture seule et par l'API de
Vision. Il complète le relevé du 9 octobre sans le remplacer.

| Élément | Relevé |
|---|---|
| INFRA-01 | démarré le 09/10 à 13:45, 7 % du disque utilisé, aucune unité systemd en échec |
| Composition | Platform 1.0.145 : Agent 1.48.0 et Vision 1.38.1, actifs depuis le 10/10 à 15:40 ; Installer 1.16.0 |
| Chrony | synchronisé, strate 2, écart de 0,4 ms |
| DHCP | dnsmasq actif, 42 baux, Bubule renouvelé aujourd'hui ; exclusivité non prouvée |
| DNS | `ha-01.ohana.lan` = 192.168.1.20 sur 192.168.1.10, .11 et .12 |
| Réplication AdGuard | timer toutes les 5 minutes, 38 noms vérifiés, synchronisation .11 vers .12 réussie |
| Sauvegarde INFRA-01 | `backup.infra` réussi chaque jour du 19 au 25/10 |
| Katsuyu / Shizune | `katsuyu-bubule` réclame et termine ses jobs ; passerelle Shizune disponible |

Constats du même jour, corrigés dans le dépôt Agent mais pas encore déployés :

- l'Agent écrivait environ 14 000 lignes `httpx` par jour dans le journal
  d'INFRA-01, ce qui tronquait chaque jour la collecte des journaux ;
- au changement d'heure du 25/10 à 02:00, la sauvegarde planifiée de HA-01 a
  échoué à ouvrir son investigation (horloge des jobs fausse dans l'heure
  répétée) ;
- l'incident critique `adguard_sync.status` ouvert le 24/10 à 22:37 venait d'une
  pause temporaire de la protection AdGuard, répliquée avec 11 s d'écart. La
  protection est encore suspendue jusqu'au 25/10 à 21:36 sur les deux AdGuard :
  c'est un réglage de l'opérateur à confirmer.

## Inventaire historique du 29 juillet 2026

Les adresses ci-dessous sont conservées comme historique ; ne pas les utiliser
comme constat actuel pour préparer une intervention.

| Identifiant | Équipement | Adresse relevée le 29 juillet | Rôle |
|---|---|---:|---|
| BOX-01 | Freebox Pop | 192.168.1.1 | Internet et WireGuard |
| INFRA-01 | serveur Debian | 192.168.1.10 | Infrastructure et Ohana |
| LINKY-01 | Raspberry Pi Linky | 192.168.1.53 | Téléinformation |
| ZWAVE-01 | Raspberry Pi Z-Wave | 192.168.1.54 | Z-Wave |
| AP-01 | Linksys LAPAC1750 | 192.168.1.99 | Wi-Fi |
| HA-01 | Home Assistant Green | 192.168.1.247 | Home Assistant et Mosquitto |

Le réseau physique utilise SW-01 et SW-02 TRENDnet, puis SW-03 pour les
équipements domotiques. Voir [l'inventaire](docs/architecture/Inventaire.md).

## Cible Hashirama et vérifications de terrain

| Identifiant | Adresse cible | Confirmation datée disponible ici |
|---|---:|---|
| BOX-01 | 192.168.1.1 | Pas de nouveau relevé |
| INFRA-01 | 192.168.1.10 | Cycle exécuté, configuration réseau à consigner |
| ZWAVE-01 | 192.168.1.11 | AdGuard vérifié ; adresse effective à dater |
| LINKY-01 | 192.168.1.12 | AdGuard vérifié ; adresse effective à dater |
| HA-01 | 192.168.1.20 | Réponse DNS du 09/10 à 16:57 |

Pour chaque nouveau contrôle, consigner la date Europe/Paris, les versions,
l'adresse réellement observée, le résultat et sa source. Un nom résolu ne
démontre pas à lui seul le bon fonctionnement de l'application.

# Guide de reconstruction

Ce parcours reconstruit Konoha après une perte totale. Pour la seule panne
d'INFRA-01, suivre directement [Restaurer INFRA-01](docs/INFRA-01/Sauvegarde/Restaurer-INFRA-01.md).
Les vérifications ci-dessous constituent une recette à effectuer ; elles ne
déclarent pas les opérations déjà réalisées.

## Préparer l'intervention

Identifier les machines perdues, les archives, leurs dates, les clés de
restauration et les adresses effectivement déployées. Préserver les supports
illisibles. Conserver le DHCP de la box pendant la reconstruction, après avoir
vérifié qu'aucun autre serveur ne répond. Garder une console locale pour INFRA-01.

## Rétablir les dépendances réseau et HAOS

| Étape | Procédure | Vérification avant de poursuivre |
|---|---|---|
| Freebox et Internet | [Restaurer Freebox](docs/procedures/restauration/Restaurer-Freebox.md) | Passerelle et DHCP provisoire accessibles |
| HA-01 | [Restaurer Home Assistant](docs/procedures/restauration/Restaurer-Home-Assistant.md), ou [installer Green](docs/procedures/installation/Installer-Home-Assistant-Green.md) puis [le configurer](docs/procedures/Configuration/Configurer-Home-Assistant-Green.md) | Home Assistant et Mosquitto accessibles |
| LINKY-01 et ZWAVE-01 | [Restaurer Linky](docs/procedures/restauration/Restaurer-RPi-Linky.md), [restaurer Z-Wave](docs/procedures/restauration/Restaurer-RPi-ZWave.md) | HAOS, AdGuard, téléinformation et Z-Wave vérifiés sur chaque cible |
| DNS et clients | [Configurer AdGuard](docs/procedures/Configuration/Configurer-AdGuard.md), [configurer les clients DNS](docs/procedures/Configuration/Configurer-Clients-DNS.md) | Les deux DNS répondent ; leurs adresses réelles sont connues |

En l'absence d'une sauvegarde HAOS exploitable, utiliser
[l'installation HAOS](docs/procedures/installation/Installer-Home-Assistant-OS.md)
puis les procédures de configuration de la cible. Restaurer uniquement les
instances perdues. Installer Mosquitto/AdGuard selon leurs procédures si les
add-ons ne sont pas déjà restaurés avec l'instance HAOS.

## Reconstruire INFRA-01 et Ohana

1. Suivre [Installer INFRA-01](docs/INFRA-01/Installation/Installer-INFRA-01.md)
   sur un support sain et installer Ohana-Installer 1.15.6 ou supérieur.
2. [Restaurer l'archive INFRA-01](docs/INFRA-01/Sauvegarde/Restaurer-INFRA-01.md) :
   composition sauvegardée, configurations, base Vision, permissions et identité
   `age`. Ne pas installer auparavant une autre composition Agent/Vision.
3. Rétablir le réseau .10 depuis la console ; vérifier les DNS réels et la route.
4. Vérifier Agent, Vision, Chrony, la résolution MQTT et l'accès iCloud sous
   l'utilisateur Agent. Contrôler les autorisations Katsuyu/Shizune restaurées,
   ou refaire l'association si l'archive ne les contient pas.
5. [Rétablir le cycle de réservations DNS](docs/INFRA-01/Capacites/DNS/Synchroniser-Reservations-DHCP.md)
   et vérifier sa réplication, puis son timer. Les unités House ne sont pas
   réinstallées automatiquement par Installer.
6. Comparer la composition restaurée avec `ohana versions` et les versions
   installées. Une mise à jour est une étape distincte, après validation de la
   restauration, selon [le guide Platform](https://github.com/cedric-HAOS/Ohana-Platform/blob/main/docs/Installer-Ohana-Platform.md).
7. [Mettre le DHCP en production](docs/INFRA-01/Capacites/DHCP/Mettre-en-Production-DHCP.md)
   seulement après arrêt du DHCP provisoire. Vérifier un nouveau bail réel et
   l'exclusivité du serveur ; appliquer le retour arrière en cas d'échec.

## Rétablir les applications et l'accès distant

Vérifier [les clients MQTT](docs/procedures/configuration/Configurer-Clients-MQTT.md),
la sortie HTTP Linky indépendante et Z-Wave. Rétablir
[WireGuard](docs/procedures/Configuration/Configurer-WireGuard-Freebox.md) et
[les clients VPN](docs/procedures/configuration/Configurer-Clients-VPN.md), puis
contrôler Shizune depuis le réseau de confiance et via le VPN.

Le prototype ESP-03 n'est pas un prérequis à la reconstruction : conserver son
état désarmé tant que sa recette matérielle n'est pas qualifiée.

## Sauvegarder et qualifier

Créer et contrôler les [sauvegardes HAOS](docs/procedures/sauvegarde/Sauvegarder-Home-Assistant.md),
la [sauvegarde Freebox](docs/procedures/sauvegarde/Sauvegarder-Freebox.md) et une
[nouvelle sauvegarde INFRA-01](docs/INFRA-01/Sauvegarde/Sauvegarder-INFRA-01.md).
Renseigner [Validation finale](Validation-Finale.md) avec la date, les versions
et les preuves. Déclarer la reconstruction terminée seulement lorsque les
contrôles applicables sont réussis ; consigner toute réserve séparément.

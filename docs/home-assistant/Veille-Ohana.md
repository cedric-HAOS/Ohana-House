# Veille d'Ohana depuis HA-01

HA-01 est une machine distincte d'INFRA-01. Il surveille Ohana et prévient
l'iPhone par l'application Home Assistant quand Ohana ne peut plus le faire
lui-même. Fichier : [config/home-assistant/ohana-veille.yaml](../../config/home-assistant/ohana-veille.yaml).

## Ce qui est surveillé

| Panne | Comment HA-01 la voit | Délai |
|---|---|---|
| INFRA-01 éteint ou injoignable, Vision arrêté | `binary_sensor.ohana_veille_vision` devient `unavailable` ou `off` (appel `GET /api/runtime/vitals` toutes les 60 s, par adresse IP : aucune dépendance au DNS d'INFRA-01) | 5 min |
| Agent arrêté ou figé, vu par Vision | `binary_sensor.ohana_veille_agent` (`agent.state` ≠ `active`, silence de plus de 300 s côté Vision) | 5 min |
| Agent muet côté MQTT | `sensor.ohana_platform_alertes_actives` passe à `unavailable` (message `offline` à l'arrêt, expiration après cinq battements manqués) | 10 min |
| Alertes actives (incident critique, hôte, sauvegarde, etc.) | même capteur, valeur supérieure à 0 | 10 min |

Les délais évitent qu'un redémarrage de service, un `ohana update` ou un
battement manqué réveille le téléphone. La notification porte l'étiquette
`ohana-veille` : une nouvelle panne remplace la précédente au lieu de
s'empiler, et le retour à la normale pendant 2 minutes la retire.

## Installation (à faire par l'utilisateur sur HA-01)

1. Vérifier que `configuration.yaml` charge les paquets :
   `homeassistant: packages: !include_dir_named packages`.
2. Copier `config/home-assistant/ohana-veille.yaml` dans `/config/packages/`.
3. Dans le fichier, remplacer **les deux** `notify.mobile_app_REMPLACER` par le
   service de l'iPhone : Outils de développement → Actions, chercher
   `notify.mobile_app`.
4. Vérifier que `sensor.ohana_platform_alertes_actives` existe sous ce nom
   (Outils de développement → États). S'il porte un autre nom, le corriger dans
   le fichier (trois emplacements).
5. Vérifier la configuration puis redémarrer Home Assistant. Les deux capteurs
   `binary_sensor.ohana_veille_*` doivent être à `on`.

Si l'automatisation « Santé Ohana-House » existe déjà, la désactiver une fois
celle-ci validée pour ne pas recevoir deux notifications.

## Essai réel

1. Arrêter Vision sur INFRA-01 (`sudo systemctl stop ohana-vision`).
2. Après environ 5 à 6 minutes, l'iPhone reçoit « Vision ou INFRA-01 ne
   répondent pas ».
3. Redémarrer Vision ; environ 2 minutes plus tard, la notification disparaît.
4. Répéter en arrêtant l'Agent (`sudo systemctl stop ohana-agent`) : la
   notification parle de l'Agent.

L'essai de panne est à lancer par l'utilisateur : Ohana n'arrête jamais ses
propres services.

## Limites connues

- Si HA-01 lui-même, son réseau ou la sortie Internet (relais de notification
  d'Apple) sont indisponibles, rien n'est envoyé. L'utilisateur a choisi de ne
  pas ajouter de service externe.
- Un redémarrage de Home Assistant remet les capteurs à `unavailable` pendant
  la première minute : le délai de 5 minutes absorbe ce cas.
- La veille ne remplace pas Vision : elle dit que quelque chose ne va pas, pas
  quoi. Le détail reste dans Vision et Shizune.

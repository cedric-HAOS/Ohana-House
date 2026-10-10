# Chemin critique de reconstruction

Suivre [le parcours détaillé](Guide-de-Reconstruction.md). Cocher après
vérification effective, en datant les preuves dans [Validation finale](Validation-Finale.md).

- [ ] Réseau et Internet rétablis ; un seul DHCP provisoire actif.
- [ ] Archives et identités de récupération accessibles sur un support sain.
- [ ] HA-01 et Mosquitto restaurés.
- [ ] LINKY-01 et ZWAVE-01 restaurés ; les deux AdGuard répondent.
- [ ] INFRA-01 reconstruit avec Installer 1.15.6 ou supérieur.
- [ ] Composition sauvegardée, configurations et base Vision restaurées.
- [ ] Réseau .10, route et DNS vérifiés.
- [ ] Agent, Vision et Chrony actifs ; NTP effectivement utilisable.
- [ ] Permissions rclone privées, accès iCloud et identité `age` vérifiés.
- [ ] Autorisations Katsuyu/Shizune récupérées ou association refaite.
- [ ] Réservations DNS et réplication AdGuard contrôlées ; timer vérifié.
- [ ] DHCP provisoire arrêté avant activation de dnsmasq ; nouveau bail vérifié.
- [ ] MQTT, téléinformation HTTP/MQTT et Z-Wave vérifiés fonctionnellement.
- [ ] Accès Vision/Shizune local et WireGuard vérifiés.
- [ ] Nouvelles sauvegardes HAOS, Freebox et INFRA-01 contrôlées.
- [ ] Validation finale datée et réserves consignées.

En cas d'échec de la bascule, revenir au DHCP provisoire selon
[la procédure](docs/INFRA-01/Capacites/DHCP/Mettre-en-Production-DHCP.md).
Un prototype DHCP de secours non qualifié ne remplace pas la recette du principal.

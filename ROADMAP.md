# Roadmap House

## Version documentaire

Naruto v1.0 constitue l'historique du dossier d'exploitation. Hashirama v2.0 est
la baseline d'architecture ; la version documentaire publiée est **2.2.1**.
Les composants logiciels suivent leurs propres versions et roadmaps.

## Jalons historiques

- [x] Validation de dnsmasq et arrêt du DHCP Freebox consignés dans la roadmap.
- [x] Choix DNS principal ZWAVE-01 et secondaire LINKY-01.
- [x] Décision d'adressage cible ZWAVE-01 .11, LINKY-01 .12 et HA-01 .20.
- [x] Procédures de sauvegarde logique/restauration INFRA-01 présentes.
- [x] Cycle DNS du 09/10 à 16:57 : 38 noms réservés et réponses HA-01 .20.

Ces jalons ne remplacent pas une recette après reconstruction. Les preuves et
limites sont dans [Etat-Actuel.md](Etat-Actuel.md) et le [CHANGELOG](CHANGELOG.md).

## Contrôles à consigner après reprise

- [x] Dater les versions et l'état des services Agent/Vision/Chrony. *(25/10/2026 : Platform 1.0.145, Agent 1.48.0 et Vision 1.38.1 actifs depuis le 10/10 à 15:40, Chrony synchronisé en strate 2, aucune unité en échec)*
- [ ] Vérifier un nouveau bail DHCP et l'exclusivité du serveur principal. *(25/10/2026 : dnsmasq actif, 42 baux dont Bubule renouvelé ; l'absence d'un autre serveur DHCP reste à prouver)*
- [ ] Confirmer le timer de réplication DNS et son comportement pendant une panne. *(25/10/2026 : timer actif toutes les 5 minutes, 38 noms vérifiés, `ha-01.ohana.lan` = .20 sur les trois DNS ; le comportement pendant une panne n'a pas été essayé)*
- [x] Vérifier permissions rclone, accès iCloud et nouvelle sauvegarde publiée. *(25/10/2026 : `backup.infra` réussi chaque jour du 19 au 25/10 via Katsuyu)*
- [x] Vérifier les autorisations Katsuyu/Shizune ou refaire les associations requises. *(25/10/2026 : `katsuyu-bubule` réclame et termine ses jobs, passerelle Shizune disponible)*
- [ ] Actualiser l'inventaire des adresses effectives, dont les deux AdGuard.
- [ ] Maintenir l'inventaire Shelly dans Agent et House.
- [ ] Qualifier ESP-03 sur le matériel avant toute activation du secours.

Utiliser [le guide de reconstruction](Guide-de-Reconstruction.md) et
[Validation finale](Validation-Finale.md) ; conserver une preuve datée par contrôle.

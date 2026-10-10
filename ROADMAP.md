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

- [ ] Dater les versions et l'état des services Agent/Vision/Chrony.
- [ ] Vérifier un nouveau bail DHCP et l'exclusivité du serveur principal.
- [ ] Confirmer le timer de réplication DNS et son comportement pendant une panne.
- [ ] Vérifier permissions rclone, accès iCloud et nouvelle sauvegarde publiée.
- [ ] Vérifier les autorisations Katsuyu/Shizune ou refaire les associations requises.
- [ ] Actualiser l'inventaire des adresses effectives, dont les deux AdGuard.
- [ ] Maintenir l'inventaire Shelly dans Agent et House.
- [ ] Qualifier ESP-03 sur le matériel avant toute activation du secours.

Utiliser [le guide de reconstruction](Guide-de-Reconstruction.md) et
[Validation finale](Validation-Finale.md) ; conserver une preuve datée par contrôle.

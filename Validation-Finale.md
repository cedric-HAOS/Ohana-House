# Validation finale

## Objectif

Vérifier que l'ensemble de l'infrastructure Ohana-House est opérationnel après une reconstruction ou une intervention majeure.

---

# Infrastructure

- [ ] INFRA-01 accessible à l'adresse confirmée ; route et DNS vérifiés.
- [ ] Agent et Vision actifs ; versions et composition restaurée consignées.
- [ ] HA-01 est accessible.
- [ ] LINKY-01 est accessible.
- [ ] ZWAVE-01 est accessible.

---

# Réseau

- [ ] Freebox Pop opérationnelle.
- [ ] DHCP opérationnel.
- [ ] DNS opérationnel.
- [ ] Accès Internet opérationnel.

---

# Services

- [ ] Chrony actif et contrôle NTP réussi depuis un client.
- [ ] Nouveau bail DHCP vérifié ; aucun autre serveur ne répond.
- [ ] Réservations DNS présentes sur les deux AdGuard ; réplication et timer contrôlés.
- [ ] Mosquitto opérationnel.
- [ ] AdGuard Home opérationnel.
- [ ] WireGuard opérationnel.

---

# Applications

- [ ] Téléinformation Linky reçue.
- [ ] Sortie HTTP Linky vers Agent vérifiée indépendamment de MQTT.
- [ ] Publication MQTT opérationnelle.
- [ ] Agent en ligne sur MQTT ; résumé de santé récent reçu.
- [ ] Réseau Z-Wave opérationnel.

---

# Accès

- [ ] Vision et Shizune accessibles ; autorisations récupérées ou associations refaites.
- [ ] Katsuyu enregistré si utilisé ; aucune ancienne tâche réintroduite par la restauration.
- [ ] Interface Home Assistant accessible.
- [ ] Interface AdGuard accessible.
- [ ] Interface Z-Wave JS UI accessible.

---

# Sauvegardes

- [ ] `rclone.conf` : propriétaire `ohana-agent:ohana-agent`, mode `600`, accès distant vérifié.
- [ ] Identité `age` conservée et copie de récupération indépendante accessible.
- [ ] Nouvelle sauvegarde INFRA-01 publiée : manifeste, taille et SHA-256 contrôlés.
- [ ] Sauvegarde Home Assistant réalisée.
- [ ] Sauvegarde Freebox réalisée.

---

# Journaux

- [ ] Aucun défaut critique actuel inexpliqué ; erreurs historiques datées et distinguées.
- [ ] Aucun module complémentaire en erreur.
- [ ] Aucun équipement indisponible.

---

# Conclusion

## Infrastructure

- [ ] Conforme

## Dossier d'exploitation

- [ ] Conforme

## Validation

Versions installées Agent / Vision / Installer / Katsuyu / Shizune :

.................................

Composition Platform et date de l'archive restaurée :

.................................

Preuves et réserves :

.................................

Date :

.................................

Opérateur :

.................................

Commentaires :

.............................................................................

.............................................................................

.............................................................................

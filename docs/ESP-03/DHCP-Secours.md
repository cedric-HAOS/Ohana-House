# ESP-03 : DHCP de secours automatique et températures piscine

## Statut au 9 octobre 2026

Prototype local implémenté dans `config/esp-03/` : YAML complet, composant externe
et 38 réservations. Compilation réussie avec ESPHome 2026.9.0 ; tests du protocole,
des allocations, de la reprise après redémarrage et de la bascule réussis sur hôte.
Le matériel et la bascule réelle sur le LAN ne sont pas encore validés.
Aucun déploiement ni publication de release n'a été effectué.
Voir `config/esp-03/README.md` pour l'installation et la recette.

## Configuration à préserver

Carte Waveshare ESP32-P4-Eth, variante esp32p4 avec engineering_sample: true,
framework ESP-IDF, PHY IP101 adresse 1, horloge externe GPIO50, MDC GPIO31,
MDIO GPIO52 et alimentation PHY GPIO51. Conserver l'API chiffrée, l'OTA,
le serveur web et les références aux secrets existants.

Bus OneWire GPIO16 :

- Température Piscine : adresse 0xb40b24a1862a5928, intervalle 30 s,
  filtre -5 à 35 °C et médiane sur cinq valeurs.
- Température Sortie Chauffage : adresse 0xd10b24a1882fc728, intervalle 30 s,
  filtre -5 à 70 °C et médiane sur cinq valeurs.

Les noms, adresses des sondes, filtres et identifiants d'entités doivent rester
identiques après installation du composant.

## Paramètres réseau confirmés

| Paramètre | Valeur |
|---|---|
| DHCP principal | INFRA-01, 192.168.1.10 |
| IP fixe ESP-03 | 192.168.1.67/24 |
| Passerelle | 192.168.1.1 |
| DNS | 192.168.1.11 et 192.168.1.12 |
| Domaine | ohana.lan |
| Plage principale | 192.168.1.100–192.168.1.199 |
| Bail principal | 48 heures |
| Plage du secours | 192.168.1.200–192.168.1.253, 54 adresses |
| Réservations | 38 couples MAC/IP fournis par l'opérateur |

INFRA-01 reste la référence des réservations. Le secours doit distribuer
également des adresses aux appareils sans réservation, dans sa propre plage.
Conserver les adresses réservées hors des plages dynamiques ; le secours ne
réattribue jamais une adresse dynamique de la plage du principal.

## Bascule automatique implémentée

La décision s'exécute sur ESP-03 et ne dépend pas de Home Assistant ou de l'API
Ohana-Agent. Un ping ne prouve pas la disponibilité de dnsmasq.

1. Au démarrage, écouter et tester le service DHCP avant de servir des clients.
   Un firmware de recette doit rester désarmé jusqu'à son activation explicite.
2. Identifier les réponses DHCP du principal par leur identifiant de serveur
   192.168.1.10 et valider la transaction de la sonde. Un paquet quelconque ou
   une réponse de l'ESP lui-même ne constitue pas une preuve du principal.
3. Activer le secours uniquement après plusieurs sondes échouées, si le lien
   Ethernet local est opérationnel. Une perte du lien local interdit la bascule.
4. Continuer les sondes pendant le secours. Dès qu'une réponse valide du
   principal revient, cesser les nouvelles offres et attributions du secours.
   Prévoir une temporisation avant une nouvelle activation pour éviter les
   oscillations ; ne pas attendre cette temporisation pour arrêter le secours.
5. En présence d'un autre serveur DHCP inattendu, bloquer le secours et exposer
   un état de conflit plutôt que distribuer simultanément de nouvelles adresses.

Sondes toutes les 10 secondes, fenêtre de réponse de 3 secondes, trois échecs
requis et observation initiale de 120 secondes. Le retour du principal arrête
immédiatement le secours ; une nouvelle activation attend au moins 30 secondes.
Un DHCP inattendu bloque le secours au moins 60 secondes. Bail du secours :
une heure. Ces paramètres doivent encore être validés sur le matériel.

Le stockage des allocations précède toute réponse positive. Un journal absent
ou invalide met la plage dynamique en quarantaine pendant une heure, y compris
à la première installation. Les réservations restent disponibles. Le switch
d'autorisation est initialement désactivé et son choix est ensuite conservé.

## Limites et gestion des baux

Une absence de réponse ne distingue pas une panne du principal d'une coupure
réseau entre les deux serveurs. Les sondes seules ne garantissent donc pas
l'exclusion mutuelle : ce mécanisme n'est pas un protocole de failover DHCP
avec échange des baux. La séparation des plages protège contre les allocations
dynamiques identiques, mais pas contre toutes les offres simultanées.

Le composant doit gérer OFFER, REQUEST, ACK, renouvellement, RELEASE et DECLINE.
Ne pas envoyer de NAK pour une adresse appartenant au principal. Les baux
délivrés par le secours doivent être conservés ou mis en quarantaine après
redémarrage de l'ESP : une liste vidée ne prouve pas qu'une adresse est libre.
Vérifier le comportement des clients au retour de dnsmasq avec leurs anciennes
adresses .200–.253 avant de qualifier la reprise automatique.

## Recette requise avant activation sur le LAN

- Compilation avec ESPHome 2026.9.0 et la carte fournie.
- Deux températures, API, OTA et réseau conservés ; aucune boucle bloquante.
- Principal sain : aucune offre du secours.
- Arrêt de dnsmasq, puis panne d'INFRA-01 : bascule mesurée et attribution réelle.
- Équipement réservé : même IP ; appareil non réservé : adresse .200–.253.
- Options passerelle, masque, domaine et deux DNS vérifiées dans les paquets.
- Principal revenu : arrêt des offres du secours et reprise réelle d'un client.
- Redémarrage ESP en secours : aucun bail actif réattribué à une autre MAC.
- Perte du lien Ethernet ESP et serveur DHCP inattendu : aucune activation.
- Réservations mises à jour : méthode d'export et application depuis INFRA-01
  documentée ; ne pas prétendre à une synchronisation automatique non réalisée.

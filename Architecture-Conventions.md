# Architecture Conventions

> Ce document définit les conventions utilisées dans l'ensemble du projet Ohana-House.

---

# 1. Modèle architectural

L'ensemble des documents Hashirama repose sur trois niveaux :

Mission
↓
Capacité
↓
Implémentation

Les décisions d'architecture portent sur les missions et les capacités.

Les implémentations sont documentées dans Naruto.

Les ADR décrivent :

- les missions ;
- les capacités.

Naruto décrit :

- les implémentations.

---

# 2. Conventions de nommage

Les équipements sont nommés selon leur fonction.
Les noms restent indépendants du constructeur, du modèle et des technologies utilisées.
Le remplacement d'un constructeur, d'un modèle ou d'une technologie ne modifie pas le nom fonctionnel de l'équipement.

Exemple :

Freebox
↓

OpenWRT

BOX-01 reste BOX-01.

---

# Préfixes

| Préfixe  | Description              |
|----------|--------------------------|
| BOX      | Routeur Internet         |
| HA       | Home Assistant           |
| INFRA    | Infrastructure réseau    |
| AP       | Point d'accès Wi-Fi      |
| SW       | Switch                   |
| LINKY    | Téléinformation          |
| ZWAVE    | Passerelle Z-Wave        |
| ZIGBEE   | Passerelle Zigbee        |
| MATTER   | Passerelle Matter        |
| VELUX    | Passerelle Velux         |
| PV       | Onduleur photovoltaïque  |
| SH       | Shelly                   |
| ESP      | ESPHome                  |
| CAM      | Caméra                   |
| NAS      | NAS                      |
| PRN      | Imprimante               |

---

# 3. Plan d'adressage

Les plages sont définies par fonction et non par technologie.

| Plage     | Fonction                   |
|-----------|----------------------------|
| .10-.19   | Services d'infrastructure  |
| .20-.29   | Serveurs domotiques        |
| .30-.39   | Infrastructure réseau      |
| .40-.49   | Passerelles domotiques     |
| .50-.99   | Équipements critiques      |
| .100-.199 | DHCP dynamique             |

---

# 4. Convention des ADR

Les ADR :

- sont indépendants des technologies ;
- décrivent des décisions d'architecture ;
- ne documentent pas les procédures ;
- restent stables dans le temps.

Les logiciels et configurations sont documentés dans Naruto.

---

# 5. Standard doumentaire

| Étape                | Objectif                                 |
| -------------------- | ---------------------------------------- |
| Installer            | Installer les logiciels nécessaires      |
| Configurer           | Préparer la configuration                |
| Mettre en production | Activer la capacité sur l'infrastructure |
| Sauvegarder          | Sauvegarder la capacité                  |
| Restaurer            | Restaurer la capacité                    |
| Maintenir            | Exploitation courante                    |

# 6. Convention documentaire

Chaque document comporte, lorsque cela est pertinent :

- un objectif ;
- un contexte ;
- un périmètre ;
- un statut ;
- une date de mise à jour ;
- des références vers les documents associés.

---

# 7. Convention d'installation des logiciels tiers

Les logiciels installés en dehors des dépôts officiels de Debian sont placés dans le répertoire :

```text
/opt
```

Chaque logiciel dispose de son propre sous-répertoire.

Exemple :

```text
/opt/
├── adguardhome-sync/
├── ohana-agent/
└── ...
```

Chaque répertoire contient :

- le binaire ;
- les fichiers de configuration ;
- les scripts éventuels ;
- les fichiers propres à l'application.

Les services systemd utilisent directement ce répertoire comme répertoire de travail.

Cette convention garantit :

- une séparation claire entre le système et les logiciels tiers ;
- une sauvegarde simplifiée ;
- une restauration facilitée ;
- une meilleure lisibilité de l'infrastructure.

---

# 8. Convention des informations sensibles

La documentation Ohana-House ne contient jamais :

- de mots de passe ;
- de clés API ;
- de certificats privés ;
- de secrets.

Les procédures indiquent uniquement où ces informations doivent être renseignées.

Les secrets sont stockés directement sur les machines concernées selon les mécanismes propres à chaque application.

---

# 9. Convention MQTT (future)

Tous les topics utiliseront le préfixe :

ohana/

Exemple :

ohana/health

ohana/dns/sync

ohana/dhcp/state

---

# 10. Convention Ohana-Agent (future)

Chaque plugin devra :

- avoir une responsabilité unique ;
- publier son état MQTT ;
- répondre aux commandes standardisées ;
- produire des journaux homogènes ;
- superviser une capacité et non un logiciel.

---

# Conclusion

Les conventions définies dans ce document constituent les règles communes de conception de tous les projets de l'écosystème Ohana-House.

Toute nouvelle architecture, documentation ou évolution devra respecter ces conventions afin de garantir la cohérence de l'ensemble.
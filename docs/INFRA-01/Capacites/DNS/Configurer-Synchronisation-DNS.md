# Configuration de la synchronisation DNS

> Configuration de l'outil de synchronisation des serveurs DNS sur INFRA-01.

---

# Objectif

Configurer **adguardhome-sync** afin de synchroniser automatiquement la configuration des deux serveurs DNS de l'infrastructure.

À l'issue de cette procédure, la configuration est prête mais la synchronisation n'est pas encore active.

---

# Prérequis

- Installer-Synchronisation-DNS.md terminé.
- Les deux instances AdGuard Home sont opérationnelles.
- Les accès d'administration sont disponibles sur :
  - ZWAVE-01
  - LINKY-01

---

# Architecture retenue

| Élément | Valeur |
|----------|---------|
| Source de vérité | ZWAVE-01 |
| Réplique | LINKY-01 |
| Moteur | adguardhome-sync |
| Hébergement | INFRA-01 |

---

# Création du fichier de configuration

Éditer :

```bash
sudo nano /opt/adguardhome-sync/adguardhome-sync.yaml
```

---

# Configuration

Adapter les paramètres suivants :

```yaml
cron: "*/5 * * * *"
runOnStart: true

origin:
  url: http://192.168.1.11
  username: admin
  password: <mot-de-passe>

replica:
  url: http://192.168.1.12
  username: admin
  password: <mot-de-passe>

features:
  dns:
    accessLists: true
    serverConfig: true
    rewrites: true
  dhcp:
    serverConfig: false
    staticLeases: false
  generalSettings: true
  clientSettings: true
  services: true
  filters:
    blacklist: true
    whitelist: true
    userRules: true
```

Les identifiants d'administration des deux instances AdGuard Home sont renseignés directement dans le fichier de configuration lors du déploiement.

Ils ne sont volontairement pas documentés dans Ohana-House.

---

# Protection des identifiants

Limiter les droits du fichier :

```bash
sudo chmod 600 /opt/adguardhome-sync/adguardhome-sync.yaml
```

Contrôler :

```bash
ls -l /opt/adguardhome-sync
```

Le fichier de configuration ne doit être lisible que par l'administrateur.

---

# Vérification de la configuration

Contrôler la validité du fichier :

```bash
/opt/adguardhome-sync/adguardhome-sync \
  --config /opt/adguardhome-sync/adguardhome-sync.yaml \
  --print-config-only
```

Aucune erreur ne doit être retournée.

---

# Vérifications finales

Contrôler :

- accès à ZWAVE-01 ;
- accès à LINKY-01 ;
- validité de la configuration ;
- protection des identifiants.

Le service reste arrêté.

---

# Résultat attendu

À l'issue de cette procédure :

- la configuration est prête ;
- aucune synchronisation n'est encore exécutée.

---

# Documents associés

- Installer-Synchronisation-DNS.md
- Mettre-en-Production-Synchronisation-DNS.md
- ADR-004 — Synchronisation des instances DNS
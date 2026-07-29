# Installation de la synchronisation DNS

> Installation de l'outil de synchronisation des serveurs DNS sur INFRA-01.

---

# Objectif

Installer l'outil permettant de synchroniser automatiquement les deux serveurs DNS de l'infrastructure.

À l'issue de cette procédure, **adguardhome-sync** est installé sur INFRA-01 mais n'est pas encore configuré ni mis en production.

---

# Prérequis

- Installer-INFRA-01.md terminé.
- Configurer-INFRA-01.md terminé.
- Accès Internet disponible.
- Les serveurs DNS sont installés :
  - ZWAVE-01
  - LINKY-01

---

# Solution retenue

| Élément | Valeur |
|----------|---------|
| Capacité | Cohérence des serveurs DNS |
| Implémentation | adguardhome-sync |
| Machine | INFRA-01 |

Cette implémentation est conforme à l'ADR-004 — Synchronisation des instances DNS.

---

# Vérification préalable

Contrôler que l'outil n'est pas déjà installé.

```bash
ls /opt/adguardhome-sync
```

Résultat attendu :

```text
ls: impossible d'accéder à '/opt/adguardhome-sync' : Aucun fichier ou dossier de ce nom
```

---

# Création du répertoire d'installation

Créer le répertoire :

```bash
sudo mkdir -p /opt/adguardhome-sync
```

Se placer dans ce répertoire :

```bash
cd /opt/adguardhome-sync
```

---

# Téléchargement

Télécharger la dernière version stable de **adguardhome-sync** depuis le dépôt GitHub officiel.

Sélectionner :

- Latest Release
- Linux
- ARM64

Télécharger l'archive dans :

```text
/opt/adguardhome-sync
```

---

# Décompression

Décompresser l'archive :

```bash
tar -xzf adguardhome-sync_*_linux_arm64.tar.gz
```

Vérifier le contenu :

```bash
ls -l
```

Résultat attendu :

```text
adguardhome-sync
LICENSE
README.md
```

---

# Droits d'exécution

Rendre le binaire exécutable :

```bash
chmod +x adguardhome-sync
```

---

# Vérification

Contrôler la version :

```bash
./adguardhome-sync --version
```

La version installée doit être affichée.

---

# Préparation de la configuration

Créer le futur fichier de configuration :

```bash
touch adguardhome-sync.yaml
```

Créer une sauvegarde initiale :

```bash
cp adguardhome-sync.yaml adguardhome-sync.yaml.orig
```

La configuration sera réalisée dans :

```text
Configurer-Synchronisation-DNS.md
```

---

# Création du service systemd

Créer le fichier :

```bash
sudo nano /etc/systemd/system/adguardhome-sync.service
```

Contenu :

```ini
[Unit]
Description=AdGuardHome Sync
After=network.target

[Service]
Type=simple

WorkingDirectory=/opt/adguardhome-sync

ExecStart=/opt/adguardhome-sync/adguardhome-sync \
    run \
    --config /opt/adguardhome-sync/adguardhome-sync.yaml

Restart=always
RestartSec=30

[Install]
WantedBy=multi-user.target
```

---

# Rechargement de systemd

```bash
sudo systemctl daemon-reload
```

---

# Désactivation temporaire

Le service ne doit pas encore être démarré.

Vérifier :

```bash
systemctl is-enabled adguardhome-sync
```

Résultat attendu :

```text
disabled
```

Si nécessaire :

```bash
sudo systemctl disable adguardhome-sync
```

---

# Vérifications finales

Contrôler :

```bash
ls -l /opt/adguardhome-sync
```

Vérifier :

```bash
systemctl status adguardhome-sync
```

Le résultat attendu est :

- binaire présent ;
- configuration créée ;
- service systemd créé ;
- service arrêté ;
- démarrage automatique désactivé.

---

# Résultat attendu

À l'issue de cette procédure :

- adguardhome-sync est installé sur INFRA-01 ;
- le service systemd est prêt ;
- aucune synchronisation DNS n'est encore réalisée.

La configuration sera effectuée dans :

- Configurer-Synchronisation-DNS.md

La mise en production sera effectuée dans :

- Mettre-en-Production-Synchronisation-DNS.md

---

# Documents associés

- Installer-INFRA-01.md
- Configurer-INFRA-01.md
- Configurer-Synchronisation-DNS.md
- Mettre-en-Production-Synchronisation-DNS.md
- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-004 — Synchronisation des instances DNS
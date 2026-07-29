# Configuration d'INFRA-01

> Configuration de base du serveur d'infrastructure d'Ohana-House.

---

# Objectif

Préparer le système d'exploitation d'INFRA-01 afin qu'il puisse accueillir les différentes capacités de l'infrastructure.

À l'issue de cette procédure, le système est sécurisé, à jour et prêt pour l'installation des services.

---

# Prérequis

- Procédure Installer-INFRA-01 terminée.
- Connexion Internet disponible.

---

# Mise à jour du système

Mettre à jour la liste des paquets :

```bash
sudo apt update
```

Installer les dernières mises à jour :

```bash
sudo apt full-upgrade -y
```

Supprimer les paquets inutiles :

```bash
sudo apt autoremove -y
sudo apt autoclean
```

---

# Vérification de l'identité du système

Contrôler l'adresse IP :

```bash
ip addr
```
Résultat attendu :

Vérifier que l'adresse statique `192.168.1.10/24` est active sur l'interface réseau d'INFRA-01.

Contrôler le nom d'hôte :

```bash
hostnamectl
```

Résultat attendu :

```
Static hostname: infra-01
```

Contrôler la version du système :

```bash
cat /etc/os-release
```

Contrôler l'architecture :

```bash
uname -m
```

Résultat attendu :

```
aarch64
```

---

# Configuration du fuseau horaire

Vérifier :

```bash
timedatectl
```

Si nécessaire :

```bash
sudo timedatectl set-timezone Europe/Paris
```

---

# Installation des outils d'administration

Installer les outils de base :

```bash
sudo apt install -y \
git \
curl \
wget \
vim \
htop \
tree \
unzip \
rsync \
bash-completion
```

---

# Activation des mises à jour de sécurité

Installer :

```bash
sudo apt install unattended-upgrades
```

Activer :

```bash
sudo dpkg-reconfigure unattended-upgrades
```

Les mises à jour automatiques concernent uniquement les correctifs de sécurité.

Les mises à jour fonctionnelles restent réalisées manuellement conformément à l'ADR-007.

---

# Vérification de la synchronisation temporelle

Contrôler :

```bash
timedatectl
```

Le serveur utilise encore les serveurs NTP publics.

La capacité NTP locale sera installée ultérieurement.

---

# Vérification du réseau

Afficher l'adresse IP :

```bash
ip addr
```

Afficher la passerelle :

```bash
ip route
```

Tester Internet :

```bash
ping -c 4 1.1.1.1
```

Tester la résolution DNS :

```bash
ping -c 4 github.com
```

---

# Préparation des répertoires

Créer les dossiers d'administration :

```bash
mkdir -p ~/scripts
mkdir -p ~/logs
mkdir -p ~/backup
mkdir -p ~/tmp
```

Ces répertoires accueilleront les scripts et outils d'administration d'INFRA-01.

---

# Vérifications finales

Contrôler :

- accès SSH opérationnel ;
- système à jour ;
- connexion Internet ;
- résolution DNS ;
- fuseau horaire correct ;
- outils d'administration installés.

---

# Résultat attendu

À l'issue de cette procédure :

- le système est entièrement à jour ;
- le serveur est prêt à recevoir les capacités d'infrastructure ;
- aucune capacité (DHCP, NTP, supervision...) n'est encore installée.

---

# Documents associés

- Installer-INFRA-01.md
- Installer-DHCP.md
- Installer-NTP.md
- Configurer-Synchronisation-DNS.md
- Installer-Supervision.md
- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-007 — Politique de mise à jour de l'infrastructure
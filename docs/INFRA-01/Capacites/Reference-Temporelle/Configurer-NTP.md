# Configuration de la capacité NTP

> Configuration du serveur de référence temporelle d'INFRA-01.

---

# Objectif

Configurer Chrony afin qu'il fournisse une référence temporelle à l'ensemble de l'infrastructure.

---

# Prérequis

- Installer-NTP.md terminé.
- Internet disponible.

---

# Sauvegarde

```bash
sudo cp /etc/chrony/chrony.conf /etc/chrony/chrony.conf.orig
```

---

# Configuration

Éditer :

```bash
sudo nano /etc/chrony/chrony.conf
```

Configuration proposée :

```ini
#################################################
# Ohana-House
# Chrony
#################################################

pool fr.pool.ntp.org iburst

driftfile /var/lib/chrony/chrony.drift

makestep 1.0 3

rtcsync

allow 192.168.1.0/24

local stratum 10

logdir /var/log/chrony
```

---

# Vérification

Contrôler :

```bash
chronyd -p
```

Puis :

```bash
chronyd -q
```

La configuration doit être valide.

---

# Résultat attendu

Chrony est configuré.

Le service reste arrêté.

---

# Documents associés

- Installer-NTP.md
- Mettre-en-Production-NTP.md
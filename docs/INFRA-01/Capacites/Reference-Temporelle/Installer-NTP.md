# Installation de la capacité NTP

> Installation du serveur de référence temporelle d'INFRA-01.

---

# Objectif

Installer le serveur NTP retenu par l'architecture Ohana-House.

À l'issue de cette procédure, le service NTP est installé mais n'est pas encore configuré ni mis en production.

---

# Prérequis

- Installation d'INFRA-01 terminée.
- Configuration d'INFRA-01 terminée.
- Connexion Internet disponible.

---

# Solution retenue

| Élément | Valeur |
|----------|---------|
| Capacité | Référence temporelle |
| Implémentation | Chrony |
| Machine | INFRA-01 |

---

# Vérification préalable

Contrôler qu'aucun serveur NTP n'est installé :

```bash
dpkg -l | grep chrony
```

---

# Installation

Mettre à jour les dépôts :

```bash
sudo apt update
```

Installer Chrony :

```bash
sudo apt install chrony -y
```

---

# Vérification

Contrôler :

```bash
chronyd -v
```

Puis :

```bash
systemctl status chrony
```

---

# Désactivation temporaire

Arrêter le service :

```bash
sudo systemctl stop chrony
```

Empêcher son démarrage automatique :

```bash
sudo systemctl disable chrony
```

---

# Résultat attendu

Chrony est installé mais n'est pas encore configuré.

---

# Documents associés

- Configurer-NTP.md
- Mettre-en-Production-NTP.md
- ADR-003
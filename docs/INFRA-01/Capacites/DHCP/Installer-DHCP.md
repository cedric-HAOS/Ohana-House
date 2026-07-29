# Installation de la capacité DHCP

> Installation du serveur DHCP d'INFRA-01.

---

# Objectif

Installer le serveur DHCP retenu par l'architecture Ohana-House.

À l'issue de cette procédure, le service DHCP est installé sur INFRA-01 mais n'est pas encore configuré ni mis en production.

---

# Prérequis

- Procédure Configurer-INFRA-01 terminée.
- Connexion Internet disponible.
- Aucune modification du DHCP de la Freebox.

---

# Solution retenue

| Élément | Valeur |
|----------|---------|
| Capacité | Attribution des adresses IP |
| Implémentation | dnsmasq |
| Machine | INFRA-01 |

Cette implémentation est conforme à l'ADR-005 — Politique d'adressage IP.

---

# Vérification préalable

S'assurer qu'aucun serveur DHCP n'est installé :

```bash
dpkg -l | grep dnsmasq
```

Le résultat attendu est :

```
Aucun paquet installé
```

---

# Installation

Mettre à jour les dépôts :

```bash
sudo apt update
```

Installer dnsmasq :

```bash
sudo apt install dnsmasq -y
```

---

# Vérification de l'installation

Contrôler la version installée :

```bash
dnsmasq --version
```

Contrôler que le service existe :

```bash
systemctl status dnsmasq
```

Le service peut être actif avec la configuration par défaut.

Cette situation est normale.

---

# Désactivation temporaire

Le serveur DHCP ne doit pas être utilisé avant sa configuration.

Arrêter le service :

```bash
sudo systemctl stop dnsmasq
```

Empêcher son démarrage automatique :

```bash
sudo systemctl disable dnsmasq
```

---

# Vérifications finales

Contrôler :

```bash
systemctl status dnsmasq
```

Résultat attendu :

- dnsmasq est installé ;
- le service est arrêté ;
- le démarrage automatique est désactivé.

---

# Résultat attendu

À l'issue de cette procédure :

- dnsmasq est installé sur INFRA-01 ;
- aucune configuration DHCP n'est encore appliquée ;
- la Freebox reste le seul serveur DHCP du réseau.

Le réseau de production n'est pas modifié.

---

# Documents associés

- Installer-INFRA-01.md
- Configurer-INFRA-01.md
- Configurer-DHCP.md
- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-005 — Politique d'adressage IP
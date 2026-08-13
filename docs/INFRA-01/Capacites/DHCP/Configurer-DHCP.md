# Configuration de la capacité DHCP

> Configuration du serveur DHCP d'INFRA-01.

---

# Objectif

Configurer le serveur DHCP afin qu'il soit prêt à être mis en production.

À l'issue de cette procédure, la configuration est validée mais le serveur DHCP n'est pas encore actif.

Dans le parcours normal, `ohana install` ou `ohana update` prépare cette
configuration et Vision permet ensuite d'administrer les paramètres et les
réservations. Les éditions manuelles ci-dessous servent de référence et de
procédure de secours.

---

# Prérequis

- Procédure Installer-DHCP terminée.
- L'ancien serveur assure toujours le service DHCP.
- Aucune interruption du réseau n'est prévue.

---

# Architecture retenue

| Élément | Valeur |
|----------|---------|
| Serveur DHCP | INFRA-01 |
| Implémentation | dnsmasq |
| Plage dynamique | 192.168.1.100 - 192.168.1.199 |
| Passerelle | BOX-01 |
| DNS principal | ZWAVE-01 |
| DNS secondaire | LINKY-01 |
| Serveur NTP | INFRA-01 |

---

# Sauvegarde de la configuration d'origine

Créer une copie du fichier d'origine :

```bash
sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
```

---

# Organisation des fichiers

Créer l'arborescence suivante :

```text
/etc/dnsmasq.d/
├── 00-ohana.conf
├── 10-infrastructure.conf
├── 20-serveurs.conf
├── 30-infrastructure-reseau.conf
├── 40-passerelles-domotiques.conf
├── 50-equipements-critiques.conf
├── 99-local.conf
└── README
```

---

# Configuration principale

Créer :

```bash
sudo nano /etc/dnsmasq.d/00-ohana.conf
```

Y copier :

```ini
#################################################
# Ohana-House
# Configuration principale DHCP
#################################################

interface=eth0
bind-interfaces

domain-needed
bogus-priv

dhcp-authoritative

#################################################
# Plage DHCP
#################################################

dhcp-range=192.168.1.100,192.168.1.199,255.255.255.0,24h

#################################################
# Options DHCP
#################################################

dhcp-option=option:router,192.168.1.1

dhcp-option=option:dns-server,192.168.1.11,192.168.1.12

dhcp-option=option:ntp-server,192.168.1.10

#################################################
# Domaine local
#################################################

domain=ohana.lan

local=/ohana.lan/

expand-hosts
```

---

# Réservations DHCP

## Infrastructure

Créer :

```bash
sudo nano /etc/dnsmasq.d/10-infrastructure.conf
```

INFRA-01 n'est pas déclaré dans ce fichier : son adresse
`192.168.1.10/24` est configurée statiquement dans NetworkManager afin que le
serveur DHCP ne dépende pas de lui-même. Ce fichier est réservé aux futurs
équipements d'infrastructure utilisant une réservation.

---

## Serveurs

Créer :

```bash
sudo nano /etc/dnsmasq.d/20-serveurs.conf
```

Exemple :

```ini
dhcp-host=AA:BB:CC:DD:EE:02,192.168.1.20,ha-01
```

---

## Infrastructure réseau

Créer :

```bash
sudo nano /etc/dnsmasq.d/30-infrastructure-reseau.conf
```

Exemple :

```ini
dhcp-host=AA:BB:CC:DD:EE:03,192.168.1.30,ap-01
```

---

## Passerelles domotiques

Créer :

```bash
sudo nano /etc/dnsmasq.d/40-passerelles-domotiques.conf
```

Exemple :

```ini
dhcp-host=AA:BB:CC:DD:EE:04,192.168.1.11,zwave-01
dhcp-host=AA:BB:CC:DD:EE:05,192.168.1.12,linky-01
```

---

## Équipements critiques

Créer :

```bash
sudo nano /etc/dnsmasq.d/50-equipements-critiques.conf
```

Exemple :

```ini
dhcp-host=AA:BB:CC:DD:EE:06,192.168.1.50,nas-01
```

---

# Configuration locale

Le fichier :

```text
99-local.conf
```

est réservé aux besoins temporaires ou spécifiques à l'installation.

Il ne doit jamais contenir une configuration permanente de l'infrastructure.

---

# Documentation locale

Créer le fichier :

```text
/etc/dnsmasq.d/README
```

Contenu proposé :

```text
00-ohana.conf
Configuration générale du serveur DHCP.

10-infrastructure.conf
Réservations des services d'infrastructure.

20-serveurs.conf
Réservations des serveurs.

30-infrastructure-reseau.conf
Réservations des équipements réseau.

40-passerelles-domotiques.conf
Réservations des passerelles domotiques.

50-equipements-critiques.conf
Réservations des équipements critiques.

99-local.conf
Configuration locale temporaire.
```

---

# Vérification de la configuration

Contrôler la syntaxe :

```bash
sudo dnsmasq --test
```

Résultat attendu :

```text
dnsmasq: syntax check OK
```

---

# Vérifications finales

Contrôler :

- configuration principale créée ;
- organisation des fichiers respectée ;
- syntaxe valide.

Le service DHCP reste arrêté.

---

# Résultat attendu

À l'issue de cette procédure :

- la configuration DHCP est prête ;
- les réservations sont organisées selon l'architecture d'Ohana-House ;
- la documentation est intégrée directement dans le répertoire de configuration ;
- aucune modification n'a encore été apportée au réseau.

La mise en production sera réalisée dans **Basculer-DHCP.md**.

---

# Documents associés

- Installer-DHCP.md
- Basculer-DHCP.md
- Sauvegarder-DHCP.md
- Restaurer-DHCP.md
- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-005 — Politique d'adressage IP

# Mise en production de la capacité DHCP

> Bascule du service DHCP de BOX-01 vers INFRA-01.

---

# Objectif

Mettre en production le serveur DHCP d'INFRA-01 sans interruption durable du fonctionnement du réseau.

À l'issue de cette procédure, INFRA-01 devient le serveur DHCP officiel de l'infrastructure.

---

# Prérequis

- Procédure Configurer-DHCP.md terminé.
- Configuration validée par :

```bash
sudo dnsmasq --test
```

- L'ancien serveur assure toujours le DHCP.
- Une sauvegarde de la configuration dnsmasq est disponible.

---

# Fenêtre d'intervention

Cette opération doit être réalisée :

- en présence de l'administrateur ;
- hors période d'utilisation importante du réseau ;
- avec un accès physique à INFRA-01.

---

# Vérifications avant bascule

Contrôler :

```bash
systemctl status dnsmasq
```

Le service doit être :

- installé ;
- arrêté ;
- désactivé.

Vérifier également :

```bash
ip addr
```

INFRA-01 doit disposer de son adresse statique `192.168.1.10/24` avant l’activation de dnsmasq.

---

# Préparation de dnsmasq

Autoriser son démarrage automatique sans le lancer :

```bash
sudo systemctl enable dnsmasq
```

Vérifier une dernière fois la configuration :

```bash
sudo dnsmasq --test
```

---

# Bascule DHCP

Depuis l'interface d'administration de l'ancien serveur DHCP (box Internet,
routeur, autre serveur ou autre machine) :

- désactiver le serveur DHCP ;
- appliquer la configuration ;
- ne modifier aucun autre paramètre réseau.

Démarrer immédiatement dnsmasq avec Ohana-Installer :

```bash
sudo ohana capability activate dhcp
```

L'Installer demande explicitement :

```text
L'ancien serveur DHCP a-t-il été désactivé ?
```

Il exécute `dnsmasq --test` avant d'activer et de démarrer le service.

Résultat attendu :

```text
active (running)
```

Un seul serveur DHCP doit être actif. Si dnsmasq ne démarre pas, réactiver
l'ancien serveur DHCP avant de poursuivre le diagnostic.

---

# Vérification immédiate

Sur un poste de test :

Renouveler le bail DHCP.

Sous Linux :

```bash
sudo dhclient -r
sudo dhclient
```

Sous Windows :

```cmd
ipconfig /release
ipconfig /renew
```

Contrôler :

```bash
ipconfig /all
```

ou

```bash
ip addr
```

Vérifier :

- adresse IP correcte ;
- passerelle = BOX-01 ;
- DNS principal = ZWAVE-01 ;
- DNS secondaire = LINKY-01 ;
- serveur DHCP = INFRA-01.

---

# Vérifications fonctionnelles

Tester :

Connexion Internet :

```bash
ping 1.1.1.1
```

Résolution DNS :

```bash
ping github.com
```

Résolution DNS locale :

```bash
ping ha-01.ohana.lan
```

Synchronisation NTP :

```bash
timedatectl
```

Le serveur NTP local sera mis en œuvre ultérieurement.

Cette vérification confirme uniquement qu'aucune régression n'est apparue.

---

# Validation

Contrôler plusieurs équipements :

- ordinateur fixe ;
- ordinateur portable ;
- smartphone ;
- Home Assistant ;
- Raspberry Pi.

Vérifier que tous obtiennent correctement :

- une adresse IP ;
- la passerelle ;
- les serveurs DNS.

---

# Retour arrière

En cas d'échec :

Arrêter dnsmasq :

```bash
sudo ohana capability deactivate dhcp
```

Depuis l'ancien serveur :

- réactiver le serveur DHCP.

Renouveler ensuite les baux DHCP des postes de test.

Vérifier le retour à un fonctionnement nominal.

Analyser les journaux avant toute nouvelle tentative.

---

# Résultat attendu

À l'issue de cette procédure :

- INFRA-01 assure la capacité DHCP ;
- BOX-01 ne distribue plus d'adresses IP ;
- les réservations DHCP sont opérationnelles ;
- le plan d'adressage d'Ohana-House est appliqué.

---

# Documents associés

- Installer-INFRA-01.md
- Configurer-INFRA-01.md
- Installer-DHCP.md
- Configurer-DHCP.md
- Sauvegarder-DHCP.md
- Restaurer-DHCP.md
- ADR-003 — Services d'infrastructure (INFRA-01)
- ADR-005 — Politique d'adressage IP

# Mise en production de la synchronisation DNS

> Activation de la synchronisation automatique des serveurs DNS.

---

# Objectif

Mettre en production la synchronisation automatique de la configuration des serveurs DNS.

INFRA-01 fournit les noms des réservations DHCP dans `ohana.lan`. ZWAVE-01
reste l'origine de la configuration AdGuard Home répliquée vers LINKY-01.

---

# Prérequis

- Installer-Synchronisation-DNS.md terminé.
- Configurer-Synchronisation-DNS.md terminé.
- Les deux serveurs DNS sont accessibles.

---

# Vérifications préalables

Depuis INFRA-01 :

Contrôler l'accès au DNS principal :

```bash
ping 192.168.1.11
```

Contrôler l'accès au DNS secondaire :

```bash
ping 192.168.1.12
```

---

# Première synchronisation

Exécuter une synchronisation manuelle :

```bash
sudo systemctl start adguardhome-sync.service
```

Vérifier qu'aucune erreur n'est signalée.

---

# Vérification

Depuis l'interface Web d'AdGuard Home :

Contrôler que :

- les listes de filtrage sont identiques ;
- les réécritures DNS sont identiques ;
- les paramètres DNS sont identiques ;
- les clients sont identiques.

---

# Activation du service

Autoriser le démarrage automatique :

```bash
sudo systemctl enable adguardhome-sync.timer
```

Démarrer le service :

```bash
sudo systemctl start adguardhome-sync.timer
```

---

# Vérification du service

Contrôler :

```bash
systemctl status adguardhome-sync.timer
systemctl show adguardhome-sync.service -p Result
```

Résultat attendu :

```text
Timer : active (waiting)
Dernier cycle du service : Result=success
```

---

# Vérification fonctionnelle

Modifier un paramètre mineur sur ZWAVE-01.

Attendre le délai défini dans la configuration.

Contrôler que la modification apparaît automatiquement sur LINKY-01.

---

# Retour arrière

En cas d'échec :

Arrêter le service :

```bash
sudo systemctl stop adguardhome-sync.timer adguardhome-sync.service
```

Désactiver le démarrage automatique :

```bash
sudo systemctl disable adguardhome-sync.timer
```

Corriger la configuration avant toute nouvelle tentative.

---

# Résultat attendu

À l'issue de cette procédure :

- ZWAVE-01 constitue la source de vérité ;
- LINKY-01 est synchronisé automatiquement ;
- les deux serveurs DNS présentent une configuration cohérente.

---

# Documents associés

- Installer-Synchronisation-DNS.md
- Configurer-Synchronisation-DNS.md
- ADR-004 — Synchronisation des instances DNS

Le parcours complet et les requêtes DNS de validation figurent dans
[Synchroniser-Reservations-DHCP.md](Synchroniser-Reservations-DHCP.md).

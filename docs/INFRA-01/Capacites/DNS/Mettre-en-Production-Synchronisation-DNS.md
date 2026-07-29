# Mise en production de la synchronisation DNS

> Activation de la synchronisation automatique des serveurs DNS.

---

# Objectif

Mettre en production la synchronisation automatique de la configuration des serveurs DNS.

À l'issue de cette procédure, ZWAVE-01 devient la source de vérité de la configuration DNS.

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
/opt/adguardhome-sync/adguardhome-sync \
  --config /opt/adguardhome-sync/adguardhome-sync.yaml \
  run
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
sudo systemctl enable adguardhome-sync
```

Démarrer le service :

```bash
sudo systemctl start adguardhome-sync
```

---

# Vérification du service

Contrôler :

```bash
systemctl status adguardhome-sync
```

Résultat attendu :

```text
active (running)
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
sudo systemctl stop adguardhome-sync
```

Désactiver le démarrage automatique :

```bash
sudo systemctl disable adguardhome-sync
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
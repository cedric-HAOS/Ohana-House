# Mise en production de la capacité NTP

> Activation du serveur de référence temporelle d'INFRA-01.

---

# Objectif

Mettre en production le serveur NTP de l'infrastructure.

---

# Prérequis

- Installer-NTP.md terminé.
- Configurer-NTP.md terminé.

---

# Activation

Autoriser le démarrage :

```bash
sudo systemctl enable chrony
```

Démarrer :

```bash
sudo systemctl start chrony
```

---

# Vérifications

Contrôler :

```bash
systemctl status chrony
```

Afficher les sources :

```bash
chronyc sources
```

Afficher le suivi :

```bash
chronyc tracking
```

---

# Validation

Depuis un autre équipement du réseau :

```bash
chronyc -h 192.168.1.10 tracking
```

ou

```bash
ntpdate -q 192.168.1.10
```

Vérifier que le serveur répond.

---

# Vérification de résilience

Déconnecter temporairement INFRA-01 d'Internet.

Contrôler :

```bash
chronyc tracking
```

Le serveur doit continuer à distribuer une référence temporelle locale.

---

# Retour arrière

En cas d'échec :

```bash
sudo systemctl stop chrony
sudo systemctl disable chrony
```

Analyser les journaux :

```bash
journalctl -u chrony
```

---

# Résultat attendu

À l'issue de cette procédure :

- INFRA-01 fournit la référence temporelle de l'infrastructure ;
- tous les équipements peuvent utiliser INFRA-01 comme serveur NTP ;
- la maison conserve une référence temporelle cohérente même en cas de perte temporaire d'Internet.

---

# Documents associés

- Installer-NTP.md
- Configurer-NTP.md
- ADR-003
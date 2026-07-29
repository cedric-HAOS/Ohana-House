# Guide de reconstruction

## Objectif

Ce document décrit l'ordre dans lequel reconstruire l'infrastructure **Ohana-House**.

Il constitue le point d'entrée du dossier d'exploitation après une perte totale ou lors d'une reconstruction complète.

Les opérations décrites ici s'appuient exclusivement sur les procédures du dépôt. Aucune étape ne doit être réalisée sans suivre la procédure associée.

---

# Principes

La reconstruction est réalisée selon les principes suivants :

- respecter l'ordre des phases ;
- valider chaque étape avant de poursuivre ;
- ne jamais passer à une phase suivante tant que la précédente n'est pas entièrement validée ;
- utiliser exclusivement les procédures de référence du dépôt.

---

# Phase 1 — Infrastructure

| Étape | Procédure |
|--------|-----------|
| 1 | Installer-Home-Assistant-OS.md |
| 2 | Configurer-Instance-Home-Assistant.md |
| 3 | Installer-Home-Assistant-Green.md |
| 4 | Configurer-Home-Assistant-Green.md |

Valider le bon fonctionnement de HA-01 avant de poursuivre.

---

# Phase 2 — Services

| Étape | Procédure |
|--------|-----------|
| 5 | Installer-Mosquitto.md |
| 6 | Configurer-Mosquitto.md |
| 7 | Installer-AdGuard.md |
| 8 | Configurer-AdGuard.md |
| 9 | Configurer-Clients-DNS.md |
| 10 | Configurer-WireGuard-Freebox.md |
| 11 | Configurer-Clients-VPN.md |

Valider le fonctionnement des services avant de poursuivre.

---

# Phase 3 — Applications

| Étape | Procédure |
|--------|-----------|
| 12 | Configurer-RPi-Linky.md |
| 13 | Configurer-RPi-ZWave.md |
| 14 | Configurer-Clients-MQTT.md |

Valider le fonctionnement des applications avant de poursuivre.

---

# Phase 4 — Sauvegarde

| Étape | Procédure |
|--------|-----------|
| 15 | Sauvegarder-Home-Assistant.md |
| 16 | Sauvegarder-Freebox.md |

Créer une sauvegarde complète de l'infrastructure reconstruite.

---

# Phase 5 — Validation

Exécuter :

- Validation-Finale.md

Une fois la validation terminée, l'infrastructure est considérée comme opérationnelle.
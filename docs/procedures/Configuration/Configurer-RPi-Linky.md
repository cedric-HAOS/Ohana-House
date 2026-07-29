# Configurer Raspberry Pi Linky

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer Raspberry Pi Linky |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration de l'instance **LINKY-01** après l'installation de Home Assistant OS.
>
> Elle ne couvre pas l'installation de Home Assistant OS, décrite dans la procédure **Installer Home Assistant OS**.

---

# 1. Objectif

Configurer l'instance Home Assistant dédiée à la collecte de la téléinformation Linky et à la publication des données vers le broker MQTT de l'infrastructure.

---

# 2. Contexte

Utiliser cette procédure :

- après une installation de Home Assistant OS ;
- après une reconstruction du Raspberry Pi Linky ;
- après une réinitialisation complète de l'instance.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Home Assistant OS installé ;
- accès administrateur à Home Assistant ;
- adaptateur Téléinformation raccordé au compteur Linky ;
- broker MQTT opérationnel.

---

# 4. Niveau de risque

| Élément | Valeur |
|---------|--------|
| Risque | Moyen |

---

# 5. Impact

| Élément | Valeur |
|---------|--------|
| Interruption de service | Oui |
| Impact utilisateur | Faible |
| Fenêtre de maintenance recommandée | Oui |

---

# 6. Procédure

## Étape 1

Appliquer la procédure :

- Configurer-Instance-Home-Assistant.md

---

## Étape 2

Configurer la connexion au broker MQTT.

Utiliser les paramètres définis dans :

- `Mosquitto.md`

---

## Étape 3

Configurer l'intégration Téléinformation.

Sélectionner le port série correspondant à l'adaptateur utilisé.

---

## Étape 4

Configurer la publication des données vers MQTT.

---

## Étape 5

Redémarrer l'instance Home Assistant.

---

# 7. Configuration appliquée

Paramètres spécifiques à LINKY-01 :

| Paramètre | Valeur |
|-----------|--------|
| Identifiant | LINKY-01 |
| Rôle | Collecte de la téléinformation |
| Téléinformation | Activée |
| Port série | À compléter |

---

# 8. Vérifications

Vérifier les points suivants :

- [ ] L'instance est accessible.
- [ ] La réservation DHCP est correctement appliquée.
- [ ] La connexion MQTT est opérationnelle.
- [ ] Les données de téléinformation sont reçues.
- [ ] Les données sont publiées sur le broker MQTT.
- [ ] Aucun message d'erreur n'est présent dans les journaux.

---

# 9. Retour arrière

En cas d'échec :

- vérifier la configuration réseau ;
- vérifier la réservation DHCP ;
- vérifier le raccordement de l'adaptateur Téléinformation ;
- vérifier la configuration MQTT ;
- redémarrer l'instance.

---

# 10. Documents associés

## Home Assistant

- Home-Assistant-Green.md
- RPi-Linky.md

## Réseau

- Nommage.md
- Adressage-IP.md
- Linksys-LAPAC1750.md

## Services

- Mosquitto.md

## Procédures

- Installer-Home-Assistant-OS.md
- Configurer-Mosquitto.md *(à rédiger)*
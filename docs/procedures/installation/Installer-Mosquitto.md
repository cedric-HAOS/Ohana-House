# Installer Mosquitto

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Installer Mosquitto |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit l'installation du module complémentaire **Mosquitto Broker** sur **HA-01 (Home Assistant Green)**.
>
> Elle ne couvre pas la configuration des utilisateurs MQTT, des clients MQTT ni des paramètres avancés.

---

# 1. Objectif

Installer le module complémentaire **Mosquitto Broker** sur HA-01.

À l'issue de cette procédure, le broker MQTT est installé et opérationnel.

---

# 2. Contexte

Utiliser cette procédure dans les cas suivants :

- première installation de Mosquitto ;
- reconstruction de HA-01 ;
- réinstallation du broker MQTT.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- HA-01 opérationnel ;
- accès administrateur à Home Assistant ;
- connexion Internet.

---

# 4. Niveau de risque

| Élément | Valeur |
|---------|--------|
| Risque | Faible |

---

# 5. Impact

| Élément | Valeur |
|---------|--------|
| Interruption de service | Oui (si remplacement d'un broker existant) |
| Impact utilisateur | Faible |
| Fenêtre de maintenance recommandée | Oui |

---

# 6. Procédure

## Étape 1

Ouvrir l'interface Web de Home Assistant.

---

## Étape 2

Accéder au menu :

```text
Paramètres
→ Modules complémentaires
→ Boutique des modules complémentaires
```

---

## Étape 3

Rechercher le module complémentaire :

```text
Mosquitto Broker
```

---

## Étape 4

Sélectionner **Mosquitto Broker**.

Vérifier que l'éditeur est **Home Assistant**.

---

## Étape 5

Cliquer sur **Installer**.

Attendre la fin de l'installation.

---

## Étape 6

| Option                  | Valeur |
| ----------------------- | :----: |
| Démarrer au démarrage   |    ✔   |
| Watchdog                |    ✔   |
| Mise à jour automatique |    ✔   |


---

## Étape 7

Créer un utilisateur dédié au broker MQTT.

Accéder au menu :

```text
Paramètres
→ Personnes
→ Utilisateurs
```

Créer un utilisateur réservé aux communications MQTT.

Ne pas utiliser le compte administrateur.

---

## Étape 8

Accéder à la configuration du module complémentaire.

Renseigner les identifiants de l'utilisateur MQTT créé à l'étape précédente.

---

## Étape 9

Cliquer sur **Démarrer**.

Attendre le démarrage complet du broker.

---

# 7. Vérifications

Vérifier les points suivants :

- [ ] Le module complémentaire est installé.
- [ ] Le service est démarré.
- [ ] Le statut est « En cours d'exécution ».
- [ ] Aucun message d'erreur n'est présent dans les journaux.
- [ ] Le démarrage automatique est activé.
- [ ] Watchdog est activé.
- [ ] Les mises à jour automatiques sont activées.

---

# 8. Retour arrière

En cas d'échec :

- arrêter le module complémentaire ;
- consulter les journaux ;
- corriger l'erreur identifiée ;
- redémarrer le module complémentaire.

Si nécessaire :

- désinstaller le module complémentaire ;
- reprendre la procédure depuis le début.

---

# 9. Documents associés

## Services

- Mosquitto.md

## Home Assistant

- Home-Assistant-Green.md

## Procédures

- Configurer-Mosquitto.md *(à rédiger)*
- Mettre-a-jour-Mosquitto.md *(à rédiger)*
- Restaurer-Mosquitto.md *(à rédiger)*
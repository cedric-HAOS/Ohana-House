# Configurer les clients MQTT

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer les clients MQTT |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration des équipements utilisant le broker **Mosquitto** de l'infrastructure Ohana-House.
>
> Elle ne couvre pas la configuration du broker MQTT.

---

# 1. Objectif

Configurer un équipement afin qu'il communique avec le broker MQTT de l'infrastructure.

---

# 2. Contexte

Utiliser cette procédure :

- lors de l'ajout d'un nouvel équipement MQTT ;
- après la reconstruction d'un équipement ;
- après une modification des paramètres MQTT.

---

# 3. Prérequis

- Configurer-Mosquitto.md terminé.
- Équipement connecté au réseau.
- Compte MQTT disponible.

---

# 4. Niveau de risque

| Élément | Valeur |
|---------|--------|
| Risque | Faible |

---

# 5. Impact

| Élément | Valeur |
|---------|--------|
| Interruption de service | Non |
| Impact utilisateur | Faible |
| Fenêtre de maintenance recommandée | Non |

---

# 6. Procédure

## Étape 1

Créer ou sélectionner le compte MQTT destiné à l'équipement.

---

## Étape 2

Configurer le client MQTT.

Utiliser les paramètres définis dans :

- Mosquitto.md

---

## Étape 3

Établir la connexion avec le broker.

---

## Étape 4

Vérifier que le client publie et reçoit correctement les messages MQTT.

---

## Étape 5

Contrôler les journaux du broker.

---

# 7. Configuration appliquée

Cette procédure applique la configuration de référence définie dans :

| Élément | Document |
|----------|----------|
| Broker MQTT | Mosquitto.md |

---

# 8. Vérifications

- [ ] Client connecté
- [ ] Authentification réussie
- [ ] Publication MQTT fonctionnelle
- [ ] Réception MQTT fonctionnelle
- [ ] Aucun message d'erreur

---

# 9. Retour arrière

- vérifier les identifiants ;
- vérifier la connectivité réseau ;
- vérifier les journaux Mosquitto.

---

# 10. Documents associés

- Mosquitto.md
- Configurer-Mosquitto.md
- RPi-Linky.md
- RPi-ZWave.md
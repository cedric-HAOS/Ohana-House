# Configurer Mosquitto

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer Mosquitto |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration du broker **Mosquitto Broker** après son installation sur HA-01.
>
> Elle ne couvre pas son installation, décrite dans la procédure **Installer Mosquitto**.

---

# 1. Objectif

Configurer le broker MQTT utilisé par l'ensemble de l'infrastructure Ohana-House.

---

# 2. Contexte

Utiliser cette procédure :

- après l'installation de Mosquitto ;
- après une reconstruction de HA-01 ;
- après une réinitialisation du broker.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Mosquitto installé ;
- accès administrateur à Home Assistant.

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
| Impact utilisateur | Moyen |
| Fenêtre de maintenance recommandée | Oui |

---

# 6. Procédure

## Étape 1

Créer un utilisateur dédié aux communications MQTT.

---

## Étape 2

Configurer le module complémentaire Mosquitto avec cet utilisateur.

---

## Étape 3

Redémarrer le broker.

---

## Étape 4

Configurer l'intégration MQTT dans HA-01.

---

## Étape 5

Vérifier que le broker accepte les connexions.

---

# 7. Configuration appliquée

Cette procédure applique la configuration définie dans :

| Élément | Document de référence |
|---------|-----------------------|
| Broker MQTT | Mosquitto.md |
| Home Assistant | Home-Assistant-Green.md |

Paramètres spécifiques :

| Paramètre | Valeur |
|-----------|--------|
| Authentification | Activée |
| Utilisateur dédié | Oui |
| Découverte MQTT | Activée |

---

# 8. Vérifications

- [ ] Le broker est opérationnel.
- [ ] L'intégration MQTT est connectée.
- [ ] Les clients MQTT peuvent se connecter.
- [ ] Aucun message d'erreur n'est présent.

---

# 9. Retour arrière

- vérifier les identifiants ;
- redémarrer Mosquitto ;
- consulter les journaux ;
- restaurer la configuration précédente si nécessaire.

---

# 10. Documents associés

- Mosquitto.md
- Home-Assistant-Green.md
- Installer-Mosquitto.md
- Configurer-RPi-Linky.md
- Configurer-RPi-ZWave.md
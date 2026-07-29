# Mettre à jour Mosquitto

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Mettre à jour Mosquitto |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la mise à jour du module complémentaire **Mosquitto Broker** installé sur HA-01.

---

# 1. Objectif

Mettre à jour le broker MQTT tout en garantissant la continuité des communications MQTT.

---

# 2. Contexte

Utiliser cette procédure :

- lorsqu'une nouvelle version stable est disponible ;
- après validation des notes de version.

---

# 3. Prérequis

- Sauvegarde Home Assistant récente.
- Accès administrateur.
- Aucun incident MQTT en cours.

---

# 4. Niveau de risque

| Élément | Valeur |
|---------|--------|
| Risque | Faible |

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

Vérifier qu'une mise à jour est disponible.

---

## Étape 2

Consulter les notes de version.

---

## Étape 3

Vérifier qu'une sauvegarde récente est disponible.

---

## Étape 4

Lancer la mise à jour du module complémentaire.

---

## Étape 5

Attendre le redémarrage complet de Mosquitto.

---

## Étape 6

Contrôler les journaux du broker.

---

## Étape 7

Vérifier les connexions MQTT.

---

# 7. Résultat attendu

| Élément | Valeur |
|----------|--------|
| Composant | Mosquitto Broker |
| Version | Dernière version stable |
| Broker MQTT | Opérationnel |
| Sauvegarde préalable | Réalisée |

---

# 8. Vérifications

- [ ] Le broker est démarré.
- [ ] Les clients MQTT se reconnectent automatiquement.
- [ ] Les publications MQTT sont reçues.
- [ ] Aucun message d'erreur n'est présent.

---

# 9. Retour arrière

En cas d'échec :

- restaurer la dernière sauvegarde Home Assistant ;
- vérifier les journaux ;
- reprendre la procédure.

---

# 10. Documents associés

- Mosquitto.md
- Sauvegarder-Home-Assistant.md
- Restaurer-Home-Assistant.md
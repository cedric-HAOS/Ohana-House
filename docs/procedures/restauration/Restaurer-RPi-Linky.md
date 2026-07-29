# Restaurer Raspberry Pi Linky

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Restaurer Raspberry Pi Linky |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la reconstruction complète de l'instance **LINKY-01** après une perte totale ou un remplacement du Raspberry Pi.
>
> La restauration est réalisée en appliquant les procédures d'installation et de configuration de référence d'Ohana-House.

---

# 1. Objectif

Remettre en service l'instance **LINKY-01** afin de rétablir la collecte de la téléinformation Linky et la publication des données vers le broker MQTT.

---

# 2. Contexte

Utiliser cette procédure :

- après une panne matérielle du Raspberry Pi ;
- après le remplacement de la carte SD ;
- après une corruption de Home Assistant OS ;
- lors de la reconstruction complète de l'infrastructure.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Raspberry Pi opérationnel ;
- accès au réseau local ;
- broker Mosquitto opérationnel sur HA-01 ;
- compteur Linky et interface Téléinformation raccordés.

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

Installer Home Assistant OS.

Voir :

- Installer-Home-Assistant-OS.md

---

## Étape 2

Configurer l'instance Home Assistant.

Voir :

- Configurer-Instance-Home-Assistant.md

---

## Étape 3

Configurer le Raspberry Pi Linky.

Voir :

- Configurer-RPi-Linky.md

---

## Étape 4

Vérifier la communication MQTT avec HA-01.

---

## Étape 5

Effectuer les vérifications finales.

---

# 7. État restauré

| Élément | Valeur |
|----------|--------|
| Home Assistant OS | Réinstallé |
| Instance Home Assistant | Configurée |
| Téléinformation | Opérationnelle |
| Publication MQTT | Opérationnelle |

---

# 8. Vérifications

Vérifier les points suivants :

- [ ] L'instance est accessible.
- [ ] La téléinformation est reçue.
- [ ] Les données sont publiées sur MQTT.
- [ ] Les entités sont visibles dans Home Assistant.
- [ ] Aucun message d'erreur n'est présent dans les journaux.

---

# 9. Retour arrière

En cas d'échec :

- reprendre l'installation de Home Assistant OS ;
- vérifier la configuration de l'instance ;
- vérifier la configuration MQTT ;
- vérifier le raccordement de l'interface Téléinformation ;
- reprendre la procédure depuis le début.

---

# 10. Documents associés

## Documents d'exploitation

- RPi-Linky.md
- Home-Assistant-Green.md

## Procédures

- Installer-Home-Assistant-OS.md
- Configurer-Instance-Home-Assistant.md
- Configurer-RPi-Linky.md
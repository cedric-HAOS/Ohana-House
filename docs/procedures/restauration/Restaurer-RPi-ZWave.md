# Restaurer Raspberry Pi Z-Wave

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Restaurer Raspberry Pi Z-Wave |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la reconstruction complète de l'instance **ZWAVE-01** après une perte totale ou un remplacement du Raspberry Pi.
>
> La restauration est réalisée en appliquant les procédures d'installation et de configuration de référence d'Ohana-House.

---

# 1. Objectif

Remettre en service l'instance **ZWAVE-01** afin de rétablir le fonctionnement de **Z-Wave JS UI** et des communications avec HA-01.

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
- HA-01 opérationnel ;
- contrôleur RaZberry installé.

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

Configurer le Raspberry Pi Z-Wave.

Voir :

- Configurer-RPi-ZWave.md

---

## Étape 4

Vérifier la communication entre Z-Wave JS UI et HA-01.

---

## Étape 5

Effectuer les vérifications finales.

---

# 7. État restauré

| Élément | Valeur |
|----------|--------|
| Home Assistant OS | Réinstallé |
| Instance Home Assistant | Configurée |
| Z-Wave JS UI | Opérationnel |
| Contrôleur RaZberry | Détecté |

---

# 8. Vérifications

Vérifier les points suivants :

- [ ] L'instance est accessible.
- [ ] Z-Wave JS UI est opérationnel.
- [ ] Le contrôleur RaZberry est détecté.
- [ ] HA-01 communique avec Z-Wave JS UI.
- [ ] Aucun message d'erreur n'est présent dans les journaux.

---

# 9. Retour arrière

En cas d'échec :

- reprendre l'installation de Home Assistant OS ;
- vérifier la configuration de l'instance ;
- vérifier le contrôleur RaZberry ;
- reprendre la configuration de Z-Wave JS UI ;
- reprendre la procédure depuis le début.

---

# 10. Documents associés

## Documents d'exploitation

- RPi-ZWave.md
- Home-Assistant-Green.md

## Procédures

- Installer-Home-Assistant-OS.md
- Configurer-Instance-Home-Assistant.md
- Configurer-RPi-ZWave.md
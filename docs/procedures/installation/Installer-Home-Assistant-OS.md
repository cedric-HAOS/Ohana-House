# Installer Home Assistant OS

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Installer Home Assistant OS |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit l'installation de **Home Assistant OS** sur un matériel officiellement compatible.
>
> Elle ne couvre pas la configuration de l'instance Home Assistant ni des composants qui y seront hébergés.

---

# 1. Objectif

Installer Home Assistant OS sur un équipement compatible.

À l'issue de cette procédure, le système est opérationnel, accessible sur le réseau local et prêt à être configuré.

---

# 2. Contexte

Utiliser cette procédure dans les cas suivants :

- première installation d'une instance Home Assistant OS ;
- remplacement d'un équipement ;
- reconstruction complète d'une instance Home Assistant OS.

Cette procédure est applicable à tout matériel officiellement compatible avec Home Assistant OS.

Les spécificités propres à chaque plateforme sont décrites dans les procédures correspondantes.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- équipement compatible avec Home Assistant OS ;
- support de stockage compatible (si nécessaire) ;
- alimentation adaptée ;
- ordinateur connecté à Internet ;
- accès au réseau local.

---

# 4. Niveau de risque

| Élément | Valeur |
|---------|--------|
| Risque | Faible |

---

# 5. Impact

| Élément | Valeur |
|---------|--------|
| Interruption de service | Oui (en cas de remplacement) |
| Impact utilisateur | Faible |
| Fenêtre de maintenance recommandée | Oui |

---

# 6. Procédure

## Étape 1

Télécharger l'image officielle **Home Assistant OS** correspondant au matériel utilisé.

---

## Étape 2

Écrire l'image sur le support de stockage à l'aide de l'outil recommandé pour la plateforme.

---

## Étape 3

Installer le support de stockage dans l'équipement, si nécessaire.

---

## Étape 4

Connecter l'équipement au réseau.

Utiliser :

- une connexion Ethernet lorsque l'équipement est destiné à fonctionner en réseau filaire ;
- une connexion Wi-Fi lorsque l'équipement est destiné à fonctionner en réseau sans fil.

---

## Étape 5

Mettre l'équipement sous tension.

---

## Étape 6

Attendre la fin du premier démarrage.

Cette opération peut durer plusieurs minutes.

---

## Étape 7

Vérifier que le serveur DHCP attribue une adresse IP à l'équipement.

---

## Étape 8

Depuis un navigateur Web, ouvrir :

```text
http://homeassistant.local:8123
```

Si le nom d'hôte n'est pas résolu, utiliser directement l'adresse IP attribuée.

---

## Étape 9

Vérifier que l'assistant de configuration Home Assistant est accessible.

Ne pas poursuivre la configuration.

Les opérations de configuration sont décrites dans les procédures dédiées.

---

# 7. Vérifications

Vérifier les points suivants :

- [ ] Home Assistant OS est accessible.
- [ ] Une adresse IP a été attribuée.
- [ ] L'assistant de configuration est affiché.
- [ ] Aucun message d'erreur n'est présent.

---

# 8. Retour arrière

En cas d'échec :

- vérifier l'alimentation de l'équipement ;
- vérifier le support de stockage ;
- réécrire l'image Home Assistant OS ;
- recommencer la procédure.

---

# 9. Documents associés

## Home Assistant

- Home-Assistant-Green.md
- RPi-Linky.md
- RPi-ZWave.md

## Procédures

- Configurer-RPi-Linky.md *(à rédiger)*
- Configurer-RPi-ZWave.md *(à rédiger)*
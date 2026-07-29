# Installer Home Assistant Green

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Installer Home Assistant Green |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit l'installation initiale d'un **Home Assistant Green neuf**.
>
> Elle ne couvre pas la restauration d'une sauvegarde, qui fait l'objet d'une procédure dédiée.

---

# 1. Objectif

Installer un Home Assistant Green neuf afin de disposer d'une plateforme Home Assistant opérationnelle.

À l'issue de cette procédure, le système est accessible sur le réseau local et prêt à recevoir sa configuration.

---

# 2. Contexte

Utiliser cette procédure dans les cas suivants :

- première installation ;
- remplacement d'un équipement neuf sans restauration immédiate.

Ne pas utiliser cette procédure pour restaurer une sauvegarde existante.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Home Assistant Green ;
- alimentation d'origine ;
- câble Ethernet ;
- accès au réseau local ;
- serveur DHCP disponible ;
- navigateur Web.

---

# 4. Niveau de risque

| Élément | Valeur |
|---------|--------|
| Risque | Faible |

---

# 5. Impact

| Élément | Valeur |
|---------|--------|
| Interruption de service | Oui (première installation) |
| Impact utilisateur | Aucun |
| Fenêtre de maintenance recommandée | Non |

---

# 6. Procédure

## Étape 1

Connecter le câble Ethernet entre le Home Assistant Green et le réseau local.

---

## Étape 2

Connecter l'alimentation du Home Assistant Green.

Attendre le démarrage complet du système.

Le premier démarrage peut durer plusieurs minutes.

---

## Étape 3

Vérifier que le serveur DHCP attribue une adresse IP au Home Assistant Green.

---

## Étape 4

Depuis un navigateur Web, ouvrir :

```
http://homeassistant.local:8123
```

Si le nom d'hôte n'est pas résolu, utiliser directement l'adresse IP attribuée.

---

## Étape 5

Suivre l'assistant de configuration jusqu'à l'affichage du tableau de bord Home Assistant.

Ne pas restaurer de sauvegarde à cette étape.

---

## Étape 6

Attribuer l’adresse stable prévue dans l’infrastructure au moyen d’une réservation DHCP :

```
192.168.1.247
```

La réservation DHCP est gérée par INFRA-01 conformément au document **Adressage-IP.md**.

---

## Étape 7

Redémarrer le Home Assistant Green.

---

# 7. Vérifications

Vérifier les points suivants :

- [ ] Home Assistant est accessible.
- [ ] L'adresse IP est 192.168.1.247.
- [ ] Le tableau de bord est affiché.
- [ ] Aucun message d'erreur n'est présent.
- [ ] Le système est opérationnel.

---

# 8. Retour arrière

En cas d'échec :

- vérifier le câblage réseau ;
- vérifier le fonctionnement du serveur DHCP ;
- redémarrer le Home Assistant Green ;
- recommencer la procédure.

En cas de dysfonctionnement persistant, réinitialiser le Home Assistant Green conformément à la documentation officielle.

---

# 9. Documents associés

## Architecture

- Architecture.md
- Adressage-IP.md

## Home Assistant

- Home-Assistant-Green.md

## Procédures

- Restaurer-Home-Assistant-Green.md (à rédiger)
# Sauvegarder Home Assistant

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Sauvegarder Home Assistant |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 10/10/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la sauvegarde d'une instance HAOS : HA-01, LINKY-01 ou ZWAVE-01.
>
> Choisir une sauvegarde complète et vérifier les add-ons inclus sur la cible. Une archive HA-01 ne remplace pas celle des deux autres HAOS.

---

# 1. Objectif

Créer une sauvegarde complète de l'instance HAOS choisie, incluant les
add-ons requis et leurs configurations. Sur HA-01, cela inclut Mosquitto ;
sur LINKY-01 et ZWAVE-01, cela inclut notamment leur AdGuard. Répéter la
procédure sur chaque instance, sans confondre leurs archives. Vérifier
l'identifiant, la date, le périmètre sélectionné et la clé de déchiffrement
avant de considérer l'archive comme utilisable. Le parcours iCloud Ohana
est décrit dans [le guide Platform](https://github.com/cedric-HAOS/Ohana-Platform/blob/main/docs/Guides/Sauvegarder-HAOS-vers-iCloud.md).

---

# 2. Contexte

Utiliser cette procédure :

- avant toute opération de maintenance ;
- avant une mise à jour importante ;
- de manière régulière dans le cadre de l'exploitation.

---

# 3. Prérequis

- Home Assistant opérationnel.
- Accès administrateur.

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
| Impact utilisateur | Aucun |
| Fenêtre de maintenance recommandée | Non |

---

# 6. Procédure

## Étape 1

Accéder au menu :

```text
Paramètres
→ Système
→ Sauvegardes
```

---

## Étape 2

Cliquer sur **Créer une sauvegarde**.

---

## Étape 3

Choisir une **sauvegarde complète**.

---

## Étape 4

Attendre la fin de la sauvegarde.

---

## Étape 5

Télécharger la sauvegarde sur un support externe.

---

## Étape 6

Vérifier que le fichier téléchargé est lisible et correctement stocké.

---

# 7. Sauvegarde produite

| Élément | Valeur |
|----------|--------|
| Type | Sauvegarde complète |
| Contenu | Home Assistant + modules complémentaires + configuration |
| Support | À compléter |
| Conservation | À compléter |

---

# 8. Vérifications

- [ ] Sauvegarde créée.
- [ ] Téléchargement effectué.
- [ ] Taille du fichier cohérente.
- [ ] Fichier stocké sur un support externe.
- [ ] Instance, date et add-ons inclus identifiés.
- [ ] Clé de déchiffrement conservée indépendamment de la cible.

---

# 9. Retour arrière

En cas d'échec :

- consulter les journaux Home Assistant ;
- vérifier l'espace disque disponible ;
- recommencer la sauvegarde.

---

# 10. Documents associés

- [Home Assistant Green](../../home-assistant/Home-Assistant-Green.md)
- [Installer Green](../installation/Installer-Home-Assistant-Green.md)
- [Restaurer Home Assistant](../restauration/Restaurer-Home-Assistant.md)

# Sauvegarder Home Assistant

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Sauvegarder Home Assistant |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la création d'une sauvegarde de l'instance Home Assistant Green.
>
> Cette sauvegarde inclut Home Assistant ainsi que les modules complémentaires installés (notamment Mosquitto et AdGuard Home).

---

# 1. Objectif

Créer une sauvegarde complète de Home Assistant afin de permettre la restauration de l'infrastructure en cas d'incident.

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

---

# 9. Retour arrière

En cas d'échec :

- consulter les journaux Home Assistant ;
- vérifier l'espace disque disponible ;
- recommencer la sauvegarde.

---

# 10. Documents associés

- Home-Assistant-Green.md
- Installer-Home-Assistant-Green.md
- Restaurer-Home-Assistant.md *(à rédiger)*
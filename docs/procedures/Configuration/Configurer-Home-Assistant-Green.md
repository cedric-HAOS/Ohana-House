# Configurer Home Assistant Green

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer Home Assistant Green |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ Cette procédure décrit la configuration propre à HA-01 après son installation.

---

# 1. Objectif

Configurer l'instance principale Home Assistant de l'infrastructure Ohana-House.

---

# 2. Contexte

Utiliser cette procédure :

- après l'installation de Home Assistant Green ;
- après une reconstruction complète.

---

# 3. Prérequis

- Installer-Home-Assistant-Green.md terminé ;
- Configurer-Instance-Home-Assistant.md terminé.

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
| Impact utilisateur | Important |
| Fenêtre de maintenance recommandée | Oui |

---

# 6. Procédure

## Étape 1

Appliquer la procédure :

- Configurer-Instance-Home-Assistant.md

---

## Étape 2

Vérifier la licence Home Assistant Cloud (si utilisée).

---

## Étape 3

Configurer les paramètres système.

Voir :

- Home-Assistant-Green.md

---

## Étape 4

Vérifier que les modules complémentaires installés sont opérationnels.

---

## Étape 5

Contrôler les sauvegardes automatiques.

---

## Étape 6

Contrôler les journaux système.

---

# 7. Configuration appliquée

Cette procédure applique la configuration définie dans :

| Élément | Document |
|----------|----------|
| Home Assistant Green | Home-Assistant-Green.md |
| Nommage | Nommage.md |
| Réseau | Adressage-IP.md |

---

# 8. Vérifications

- [ ] Instance accessible
- [ ] Aucun message d'erreur
- [ ] Sauvegardes opérationnelles
- [ ] Tous les add-ons démarrés

---

# 9. Retour arrière

- vérifier les journaux ;
- restaurer la dernière sauvegarde si nécessaire.

---

# 10. Documents associés

- Home-Assistant-Green.md
- Configurer-Instance-Home-Assistant.md
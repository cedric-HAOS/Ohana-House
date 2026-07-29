# Restaurer Home Assistant

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Restaurer Home Assistant |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la restauration de HA-01 à partir d'une sauvegarde complète.

---

# 1. Objectif

Restaurer l'instance Home Assistant Green après une perte totale ou une corruption de l'installation.

---

# 2. Contexte

Utiliser cette procédure :

- après une panne matérielle ;
- après une corruption du système ;
- après le remplacement de Home Assistant Green.

---

# 3. Prérequis

- Sauvegarde Home Assistant disponible.
- Home Assistant Green opérationnel.
- Accès administrateur.

---

# 4. Niveau de risque

| Élément | Valeur |
|---------|--------|
| Risque | Élevé |

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

Installer Home Assistant Green.

Voir :

- Installer-Home-Assistant-Green.md

---

## Étape 2

Restaurer la sauvegarde complète Home Assistant.

---

## Étape 3

Attendre le redémarrage complet.

---

## Étape 4

Contrôler le démarrage des modules complémentaires.

---

## Étape 5

Effectuer les vérifications finales.

---

# 7. État restauré

| Élément | Valeur |
|----------|--------|
| Home Assistant | Restauré |
| Modules complémentaires | Restaurés |
| Configuration | Restaurée |

---

# 8. Vérifications

- [ ] Home Assistant accessible
- [ ] Mosquitto opérationnel
- [ ] AdGuard opérationnel
- [ ] Automatisations fonctionnelles
- [ ] Aucun message d'erreur

---

# 9. Retour arrière

Reprendre la restauration avec une sauvegarde valide.

---

# 10. Documents associés

- Installer-Home-Assistant-Green.md
- Sauvegarder-Home-Assistant.md
- Home-Assistant-Green.md
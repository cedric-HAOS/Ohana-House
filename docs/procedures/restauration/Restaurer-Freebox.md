# Restaurer Freebox Pop

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Restaurer Freebox Pop |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la restauration de la configuration de la Freebox Pop à partir d'une sauvegarde précédemment exportée.
>
> Elle couvre uniquement la restauration de la configuration. Elle ne couvre pas le remplacement physique de la Freebox.

---

# 1. Objectif

Restaurer la configuration de la Freebox Pop afin de remettre en service les fonctionnalités réseau de l'infrastructure Ohana-House.

---

# 2. Contexte

Utiliser cette procédure :

- après une réinitialisation de la Freebox Pop ;
- après un remplacement de la Freebox Pop ;
- après une corruption de la configuration.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Freebox Pop opérationnelle ;
- accès administrateur à Freebox OS ;
- sauvegarde de configuration disponible.

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

Accéder à Freebox OS.

---

## Étape 2

Importer la sauvegarde de configuration.

---

## Étape 3

Attendre la fin de l'import.

---

## Étape 4

Redémarrer la Freebox Pop si nécessaire.

---

## Étape 5

Vérifier le bon fonctionnement des services réseau.

---

# 7. État restauré

| Élément | Valeur |
|----------|--------|
| Configuration Freebox | Restaurée |
| DHCP | Restauré |
| DNS | Restauré |
| WireGuard | Restauré |
| Configuration réseau | Restaurée |

---

# 8. Vérifications

Vérifier les points suivants :

- [ ] Accès Internet opérationnel.
- [ ] Réseau local fonctionnel.
- [ ] DHCP opérationnel.
- [ ] Résolution DNS fonctionnelle.
- [ ] WireGuard opérationnel.
- [ ] Aucun message d'erreur dans Freebox OS.

---

# 9. Retour arrière

En cas d'échec :

- vérifier l'intégrité du fichier de sauvegarde ;
- recommencer l'import ;
- réinitialiser la Freebox si nécessaire ;
- restaurer une sauvegarde plus récente si disponible.

---

# 10. Documents associés

## Réseau

- Freebox-Pop.md

## Procédures

- Sauvegarder-Freebox.md
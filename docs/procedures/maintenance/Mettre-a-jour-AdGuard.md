# Mettre à jour AdGuard Home

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Mettre à jour AdGuard Home |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la mise à jour du module complémentaire **AdGuard Home** installé sur HA-01.

---

# 1. Objectif

Mettre à jour AdGuard Home tout en garantissant la continuité du service DNS.

---

# 2. Contexte

Utiliser cette procédure :

- lorsqu'une nouvelle version stable est disponible ;
- après validation des notes de version.

---

# 3. Prérequis

- Sauvegarde Home Assistant récente.
- Accès administrateur.
- Aucun incident en cours.

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
| Impact utilisateur | Faible |
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

Attendre le redémarrage complet d'AdGuard Home.

---

## Étape 6

Contrôler les journaux du module complémentaire.

---

## Étape 7

Vérifier le bon fonctionnement du service DNS.

---

# 7. Résultat attendu

| Élément | Valeur |
|----------|--------|
| Composant | AdGuard Home |
| Version | Dernière version stable |
| Service DNS | Opérationnel |
| Sauvegarde préalable | Réalisée |

---

# 8. Vérifications

- [ ] AdGuard Home est démarré.
- [ ] Les requêtes DNS sont résolues.
- [ ] Les listes de filtrage sont chargées.
- [ ] Aucun message d'erreur n'est présent.

---

# 9. Retour arrière

En cas d'échec :

- restaurer la dernière sauvegarde Home Assistant ;
- vérifier les journaux ;
- reprendre la procédure.

---

# 10. Documents associés

- AdGuard.md
- Sauvegarder-Home-Assistant.md
- Restaurer-Home-Assistant.md
# Configurer WireGuard (Freebox)

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer WireGuard (Freebox) |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration du serveur **WireGuard** intégré à la **Freebox Pop**.
>
> Elle couvre uniquement la configuration du serveur VPN.
> La configuration des équipements utilisant le VPN est décrite dans **Configurer-Clients-VPN.md**.

---

# 1. Objectif

Configurer le serveur WireGuard de la Freebox Pop afin de permettre un accès distant sécurisé à l'infrastructure Ohana-House.

---

# 2. Contexte

Utiliser cette procédure :

- lors de la première mise en service du VPN ;
- après une réinitialisation de la Freebox Pop ;
- après une reconstruction de l'infrastructure ;
- après une modification de la configuration VPN.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Freebox Pop opérationnelle.
- Accès administrateur à Freebox OS.
- Réseau local fonctionnel.
- Accès Internet opérationnel.

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

Accéder à **Freebox OS**.

---

## Étape 2

Activer le serveur **WireGuard**.

---

## Étape 3

Configurer les paramètres du serveur conformément au document **WireGuard.md**.

---

## Étape 4

Créer les profils VPN nécessaires.

---

## Étape 5

Exporter les profils VPN.

---

## Étape 6

Enregistrer la configuration.

---

## Étape 7

Vérifier le bon fonctionnement du serveur WireGuard.

---

# 7. Configuration appliquée

| Élément | Valeur |
|----------|--------|
| Serveur VPN | WireGuard |
| Plateforme | Freebox Pop |
| Profils VPN | Créés |
| Configuration | Conforme à WireGuard.md |

---

# 8. Vérifications

Vérifier les points suivants :

- [ ] Le serveur WireGuard est actif.
- [ ] Les profils VPN sont disponibles.
- [ ] Les profils peuvent être exportés.
- [ ] Le serveur écoute correctement.
- [ ] Aucun message d'erreur n'est présent dans Freebox OS.

---

# 9. Retour arrière

En cas d'échec :

- vérifier la configuration du serveur WireGuard ;
- vérifier la connectivité Internet de la Freebox ;
- supprimer et recréer les profils VPN si nécessaire ;
- reprendre la procédure depuis le début.

---

# 10. Documents associés

## Documents d'exploitation

- WireGuard.md
- Freebox-Pop.md

## Procédures

- Configurer-Clients-VPN.md
- Sauvegarder-Freebox.md
- Restaurer-Freebox.md
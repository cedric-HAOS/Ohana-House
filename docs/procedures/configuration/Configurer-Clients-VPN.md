# Configurer les clients VPN

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer les clients VPN |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration des équipements utilisant le serveur WireGuard de la Freebox Pop.
>
> Elle ne couvre pas la configuration du serveur WireGuard.

---

# 1. Objectif

Configurer un équipement afin qu'il puisse accéder à distance à l'infrastructure Ohana-House via WireGuard.

---

# 2. Contexte

Utiliser cette procédure :

- lors de l'ajout d'un nouvel équipement ;
- après la réinstallation d'un client VPN ;
- après la régénération d'un profil WireGuard.

---

# 3. Prérequis

- Configurer-WireGuard-Freebox.md terminé.
- Profil WireGuard disponible.

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
| Impact utilisateur | Faible |
| Fenêtre de maintenance recommandée | Non |

---

# 6. Procédure

## Étape 1

Installer le client WireGuard compatible avec l'équipement.

---

## Étape 2

Importer le profil VPN.

---

## Étape 3

Activer le tunnel VPN.

---

## Étape 4

Contrôler l'attribution de l'adresse VPN.

---

## Étape 5

Vérifier l'accès à Home Assistant et aux services internes.

---

# 7. Configuration appliquée

Cette procédure applique la configuration de référence définie dans :

| Élément | Document |
|----------|----------|
| Serveur VPN | WireGuard.md |
| Freebox | Freebox-Pop.md |

---

# 8. Vérifications

- [ ] Tunnel établi
- [ ] Adresse VPN attribuée
- [ ] Accès à Home Assistant
- [ ] Accès aux équipements internes
- [ ] Aucun message d'erreur

---

# 9. Retour arrière

- vérifier le profil WireGuard ;
- vérifier les paramètres du client ;
- recréer le profil si nécessaire.

---

# 10. Documents associés

- WireGuard.md
- Freebox-Pop.md
- Configurer-WireGuard-Freebox.md
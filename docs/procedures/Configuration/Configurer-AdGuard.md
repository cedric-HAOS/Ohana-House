# Configurer AdGuard Home

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer AdGuard Home |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 04/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration du serveur **AdGuard Home** installé sur **HA-01**.
>
> Elle couvre uniquement la configuration du serveur AdGuard Home.
> La configuration des équipements utilisant ce serveur est décrite dans **Configurer-Clients-DNS.md**.

---

# 1. Objectif

Configurer le serveur **AdGuard Home** afin de fournir un service DNS sécurisé et centralisé pour l'ensemble de l'infrastructure Ohana-House.

---

# 2. Contexte

Utiliser cette procédure :

- après l'installation d'AdGuard Home ;
- après une reconstruction de HA-01 ;
- après une réinitialisation de la configuration AdGuard Home.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Installer-AdGuard.md terminé.
- Home Assistant Green opérationnel.
- Accès administrateur à Home Assistant.
- Réseau local opérationnel.

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

Accéder à l'interface d'administration AdGuard Home.

---

## Étape 2

Configurer les paramètres généraux du serveur.

---

## Étape 3

Configurer les serveurs DNS amont conformément au document **AdGuard.md**.

---

## Étape 4

Configurer les listes de filtrage.

---

## Étape 5

Configurer les paramètres de journalisation.

---

## Étape 6

Enregistrer la configuration.

---

## Étape 7

Redémarrer AdGuard Home si nécessaire.

---

# 7. Configuration appliquée

| Élément | Valeur |
|----------|--------|
| Serveur DNS | AdGuard Home |
| Configuration | Conforme à AdGuard.md |
| Listes de filtrage | Configurées |
| Journalisation | Activée |

---

# 8. Vérifications

Vérifier les points suivants :

- [ ] AdGuard Home est accessible.
- [ ] Le service DNS est opérationnel.
- [ ] Les requêtes DNS sont correctement résolues.
- [ ] Les listes de filtrage sont chargées.
- [ ] Aucun message d'erreur n'est présent dans les journaux.

---

# 9. Retour arrière

En cas d'échec :

- vérifier les paramètres de configuration ;
- contrôler les journaux AdGuard Home ;
- restaurer la dernière sauvegarde Home Assistant si nécessaire ;
- reprendre la procédure depuis le début.

---

# 10. Documents associés

## Documents d'exploitation

- AdGuard.md
- Home-Assistant-Green.md

## Procédures

- Installer-AdGuard.md
- Configurer-Clients-DNS.md
- Sauvegarder-Home-Assistant.md
- Mettre-a-jour-AdGuard.md
- Restaurer-Home-Assistant.md
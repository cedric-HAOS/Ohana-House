# Configurer une instance Home Assistant

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer une instance Home Assistant |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration commune à toute instance Home Assistant de l'infrastructure Ohana-House.
>
> Elle doit être réalisée après l'installation de Home Assistant OS et avant la configuration spécifique du rôle de l'instance.

---

# 1. Objectif

Appliquer la configuration commune à toute instance Home Assistant de l'infrastructure.

---

# 2. Contexte

Utiliser cette procédure :

- après l'installation de Home Assistant OS ;
- après une reconstruction complète d'une instance.

---

# 3. Prérequis

- Home Assistant OS installé.
- Accès administrateur.
- Réseau opérationnel.

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

Configurer le nom de l'instance conformément à :

- `Nommage.md`

---

## Étape 2

Configurer les paramètres réseau.

Utiliser :

- `Adressage-IP.md`
- `Linksys-LAPAC1750.md`
- `Freebox-Pop.md`

---

## Étape 3

Créer la réservation DHCP.

---

## Étape 4

Vérifier la résolution DNS.

---

## Étape 5

Redémarrer l'instance.

---

# 7. Configuration appliquée

Cette procédure applique la configuration de référence définie dans :

| Élément | Document |
|----------|----------|
| Nommage | Nommage.md |
| Adressage IP | Adressage-IP.md |
| Wi-Fi | Linksys-LAPAC1750.md |
| Réseau | Freebox-Pop.md |

---

# 8. Vérifications

- [ ] L'instance est accessible.
- [ ] L'adresse IP est correcte.
- [ ] Le nom de l'instance est correct.
- [ ] Le réseau fonctionne.
- [ ] La résolution DNS fonctionne.

---

# 9. Retour arrière

- vérifier les paramètres réseau ;
- vérifier la réservation DHCP ;
- redémarrer l'instance.

---

# 10. Documents associés

- Installer-Home-Assistant-OS.md
- Home-Assistant-Green.md
- RPi-Linky.md
- RPi-ZWave.md
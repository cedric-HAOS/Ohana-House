# Configurer Raspberry Pi Z-Wave

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Configurer Raspberry Pi Z-Wave |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 03/07/2026 |

> ℹ️ **Information**
>
> Cette procédure décrit la configuration de l'instance **ZWAVE-01** après l'installation de Home Assistant OS.
>
> Elle ne couvre pas l'installation de Home Assistant OS, décrite dans la procédure **Installer Home Assistant OS**.

---

# 1. Objectif

Configurer l'instance Home Assistant dédiée à l'hébergement de **Z-Wave JS UI** et à la gestion du contrôleur Z-Wave de l'infrastructure.

---

# 2. Contexte

Utiliser cette procédure :

- après une installation de Home Assistant OS ;
- après une reconstruction du Raspberry Pi Z-Wave ;
- après une réinitialisation complète de l'instance.

---

# 3. Prérequis

Les éléments suivants sont nécessaires :

- Home Assistant OS installé ;
- accès administrateur à Home Assistant ;
- contrôleur RaZberry installé ;
- HA-01 opérationnel.

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
| Impact utilisateur | Moyen |
| Fenêtre de maintenance recommandée | Oui |

---

# 6. Procédure

## Étape 1

Appliquer la procédure :

- Configurer-Instance-Home-Assistant.md

---

## Étape 2

Installer **Z-Wave JS UI**.

---

## Étape 3

Configurer le contrôleur RaZberry.

---

## Étape 4

Configurer la connexion entre **Z-Wave JS UI** et **HA-01**.

---

## Étape 5

Redémarrer les services si nécessaire.

---

# 7. Configuration appliquée

Paramètres spécifiques à ZWAVE-01 :

| Paramètre | Valeur |
|-----------|--------|
| Identifiant | ZWAVE-01 |
| Rôle | Hébergement de Z-Wave JS UI |
| Contrôleur | RaZberry |

---

# 8. Vérifications

- [ ] L'instance est accessible.
- [ ] La réservation DHCP est appliquée.
- [ ] Z-Wave JS UI est opérationnel.
- [ ] Le contrôleur RaZberry est détecté.
- [ ] HA-01 communique avec Z-Wave JS UI.
- [ ] Aucun message d'erreur n'est présent.

---

# 9. Retour arrière

- vérifier la configuration réseau ;
- vérifier le contrôleur RaZberry ;
- redémarrer les services ;
- consulter les journaux.

---

# 10. Documents associés

- Home-Assistant-Green.md
- RPi-ZWave.md
- Adressage-IP.md
- Nommage.md
- Installer-Home-Assistant-OS.md
# Restaurer Home Assistant

| Élément | Valeur |
|---------|--------|
| Projet | Ohana-House |
| Procédure | Restaurer Home Assistant |
| Version | 1.0 |
| Niveau de qualité | 🟣 Référence |
| Dernière mise à jour | 10/10/2026 |

> ℹ️ **Information**
>
> Cette procédure restaure l'instance HAOS identifiée dans l'archive : HA-01, LINKY-01 ou ZWAVE-01. Préserver la clé de déchiffrement et vérifier les add-ons réellement inclus.

---

# 1. Objectif

Restaurer l'instance HAOS cible et les add-ons présents dans sa sauvegarde.
Mosquitto appartient à HA-01 ; AdGuard aux instances LINKY-01/ZWAVE-01.
Ne pas restaurer une archive d'une autre cible pour récupérer un seul service.

---

# 2. Contexte

Utiliser cette procédure :

- après une panne matérielle ;
- après une corruption du système ;
- après le remplacement du matériel de l'instance HAOS cible.

---

# 3. Prérequis

- Sauvegarde Home Assistant disponible.
- Matériel de la cible prêt à recevoir HAOS.
- Identité de l'archive et clé de déchiffrement vérifiées.
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

Installer le matériel de la cible :

- [Home Assistant Green pour HA-01](../installation/Installer-Home-Assistant-Green.md) ;
- [Home Assistant OS pour LINKY-01 ou ZWAVE-01](../installation/Installer-Home-Assistant-OS.md).

Les parcours de reconstruction spécifiques [Linky](Restaurer-RPi-Linky.md)
et [Z-Wave](Restaurer-RPi-ZWave.md) complètent cette restauration.

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
- [ ] Add-ons attendus présents et configurés sur la bonne instance
- [ ] Mosquitto fonctionnel sur HA-01, si cette instance est restaurée
- [ ] AdGuard répond sur la cible LINKY-01/ZWAVE-01 restaurée
- [ ] Automatisations fonctionnelles
- [ ] Aucun échec actuel non expliqué dans les journaux de la cible

---

# 9. Retour arrière

Reprendre la restauration avec une sauvegarde valide.

---

# 10. Documents associés

- [Installer Green](../installation/Installer-Home-Assistant-Green.md)
- [Sauvegarder HAOS](../sauvegarde/Sauvegarder-Home-Assistant.md)
- [Home Assistant Green](../../home-assistant/Home-Assistant-Green.md)

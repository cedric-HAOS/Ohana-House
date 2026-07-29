# Nommage

## Objectif

Ce document définit les conventions de nommage utilisées dans le projet **Ohana-House**.

Ces conventions garantissent une documentation homogène, facilitent la recherche d'informations et simplifient l'évolution de l'infrastructure.

---

# Équipements

Chaque équipement possède un identifiant unique.

Le format est le suivant :

```
<Préfixe>-<Numéro>
```

Exemple :

```
SW-01
```

---

# Préfixes

| Préfixe | Catégorie | Exemple |
|---------|-----------|---------|
| BOX | Routeur / Box Internet | BOX-01 |
| SW | Switch Ethernet | SW-01 |
| AP | Point d'accès Wi-Fi | AP-01 |
| HA | Serveur Home Assistant | HA-01 |
| RPI | Raspberry Pi | LINKY-01 |
| NAS | Serveur de stockage | NAS-01 |
| UPS | Onduleur | UPS-01 |

De nouveaux préfixes pourront être ajoutés si l'infrastructure évolue.

---

# Numérotation

La numérotation commence à **01**.

Les identifiants ne sont jamais réutilisés.

Exemple :

```
SW-01
SW-02
SW-03
```

Si un switch est remplacé, il conserve son identifiant.

---

# Documents

Les documents utilisent un nom explicite.

Exemples :

```
Architecture.md

Topologie-Reseau.md

Freebox-Pop.md

WireGuard.md
```

Les espaces sont remplacés par des tirets.

Les accents sont supprimés.

---

# Diagrammes

Les diagrammes Mermaid utilisent un identifiant unique.

Format :

```
DGM-XXX
```

Exemples :

```
DGM-001
DGM-002
```

Les numéros ne sont jamais réutilisés.

---

# Versions

Les versions suivent la convention Semantic Versioning.

Exemple :

```
v0.1.0
```

Les noms de code sont définis dans **Versioning.md**.

---

# Règles générales

- Un équipement possède un identifiant unique.
- Un identifiant n'est jamais réutilisé.
- Les noms doivent être explicites.
- Les documents utilisent toujours les mêmes conventions de nommage.
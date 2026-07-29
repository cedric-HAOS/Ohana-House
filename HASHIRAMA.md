# Hashirama

## Vision

Hashirama est la deuxième évolution majeure du projet Ohana-House.

Alors que Naruto avait pour objectif de documenter l'infrastructure, Hashirama a pour objectif d'améliorer sa résilience et son autonomie.

La priorité n'est pas de supprimer tous les points de défaillance, mais de garantir que la maison continue de fonctionner localement, même en cas de perte de la connexion Internet ou d'indisponibilité prolongée de la Freebox.

---

# Principes

Toutes les évolutions de Hashirama doivent respecter les principes suivants :

- privilégier la simplicité ;
- éviter la complexité inutile ;
- conserver une administration centralisée ;
- documenter chaque décision d'architecture au moyen d'un ADR ;
- favoriser l'autonomie locale des services critiques.

---

# Objectif

En cas de perte de la Freebox pendant plusieurs jours, les services suivants doivent continuer à fonctionner :

- Home Assistant
- MQTT
- DNS
- DHCP
- ESPHome
- Shelly
- Velux
- Z-Wave
- Téléinformation Linky

La perte d'Internet ne doit pas empêcher le fonctionnement de la maison.

---

# Méthode

Chaque évolution suit les étapes suivantes :

1. Étude du besoin
2. ADR
3. Prototype
4. Validation
5. Documentation
6. Déploiement

---

# Devise

Une maison connectée doit rester intelligente, même lorsqu'elle est déconnectée.
Une architecture n'est pas définie par les logiciels qu'elle utilise, mais par les capacités qu'elle garantit.
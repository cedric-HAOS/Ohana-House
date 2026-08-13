# Sauvegarder INFRA-01

La sauvegarde d'INFRA-01 est une capacité du plugin `backup` d'Ohana-Agent.
Elle est configurable depuis **Vision → Configuration → Plugins → Sauvegardes**.

## Préparer la clé de restauration

La paire de clés doit être créée et conservée sur une autre machine :

```bash
age-keygen -o ohana-infra-01.agekey
```

Copier uniquement le destinataire public `age1...` dans Vision. La clé privée
`ohana-infra-01.agekey` ne doit jamais être enregistrée sur INFRA-01 ; conserver
au moins une copie sur un support accessible le jour d'une reconstruction.

## Contenu

Chaque sauvegarde contient les configurations Agent, Vision, dnsmasq et Chrony,
ainsi qu'un instantané cohérent de la base de données Vision. Agent crée et
chiffre l'archive dans la RAM (`tmpfs`), l'envoie à iCloud, puis publie son
manifeste de restauration en dernier. Aucune image complète de la carte SD n'est
nécessaire : le système et les logiciels sont reconstruits par Ohana-Installer.

La sauvegarde peut être lancée selon l'horaire configuré ou immédiatement depuis
la fiche de l'équipement `infra-01` dans Vision.

## Rétention iCloud

Le champ **Sauvegardes conservées dans iCloud** vaut `0` par défaut : aucune
ancienne sauvegarde n'est supprimée. Une valeur positive active la rotation,
uniquement après l'envoi et la validation complète de la nouvelle sauvegarde.
Agent ne supprime que les plus anciens dossiers horodatés qui possèdent un
manifeste publié ; une sauvegarde incomplète n'est jamais comptée comme valide.

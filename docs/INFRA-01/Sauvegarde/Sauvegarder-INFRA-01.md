# Sauvegarder INFRA-01

La sauvegarde d'INFRA-01 est une capacité du plugin `backup` d'Ohana-Agent.
Elle est configurable depuis **Vision → Configuration → Plugins → Sauvegardes**.

## Identité de restauration et copie indépendante

Ohana-Installer crée l'identité existante sous
`/etc/ohana-agent/keys/infra-01.agekey`, puis en dérive le destinataire public.
La clé appartient à `root:ohana-agent` en mode `640`, dans un répertoire `750`.
Agent copie cette identité dans `icloud:Ohana/Recovery/infra-01.agekey` avant
de publier une sauvegarde. Vision réutilise le destinataire préparé ; aucune
création manuelle de clé n'est nécessaire dans le parcours nominal.

Conserver aussi une copie de cette même identité sur un support externe protégé,
accessible lors d'une reconstruction. Ne pas afficher son contenu ni la mettre
dans Git. La copie doit correspondre à la clé des archives à restaurer : créer
une nouvelle paire ne permet pas de déchiffrer les anciennes.

Lors d'une restauration iCloud, Installer récupère l'identité cloud et la
réinstalle localement. La copie externe permet une restauration avec `--identity`
si nécessaire ; voir [Restaurer INFRA-01](Restaurer-INFRA-01.md).

## Contenu

Chaque sauvegarde contient les configurations Agent, Vision, dnsmasq et Chrony,
ainsi qu'un instantané cohérent de la base de données Vision. Avec
`use_katsuyu: true`, Agent produit le tar et l'instantané SQLite sur `tmpfs`, Katsuyu compresse
et chiffre, puis Agent relaie l'artefact vers iCloud et publie son manifeste en
dernier. Le mode local explicite compresse et chiffre sur INFRA-01.
Aucune image complète de la carte SD n'est
nécessaire : le système et les logiciels sont reconstruits par Ohana-Installer.

Pour le cycle DNS avec réservations DHCP, la configuration
`/etc/ohana-agent/adguardhome-sync.yaml` et le registre
`/etc/ohana-agent/adguard-reservations-state.json` sont inclus dans ce périmètre.
Les anciennes sauvegardes antérieures à leur création ne les contiennent pas.
Les unités systemd sont réinstallées depuis les modèles d'Ohana-House ; voir
[Synchroniser-Reservations-DHCP.md](../Capacites/DNS/Synchroniser-Reservations-DHCP.md).

La sauvegarde peut être lancée selon l'horaire configuré ou immédiatement depuis
la fiche de l'équipement `infra-01` dans Vision.

Depuis Agent 1.45.1, l'archive inclut aussi l'export des autorisations durables
Katsuyu/Shizune et des inscriptions push. Les jobs et demandes d'appairage ne
sont pas réintroduits. Les archives antérieures sans cet export restent
restaurables mais demandent une nouvelle association des clients.

## Vérifier la sauvegarde

Contrôler dans Vision le résultat réel du job et la date de la sauvegarde.
Vérifier la présence du manifeste publié en dernier, la taille et le SHA-256 de
l'archive. Un lancement ou un job de compression réussi ne suffit pas à prouver
la publication distante complète. Préparer périodiquement une recette isolée
de [restauration](Restaurer-INFRA-01.md), sans remplacer le serveur en service.

## Rétention iCloud

Le champ **Sauvegardes conservées dans iCloud** vaut `0` par défaut : aucune
ancienne sauvegarde n'est supprimée. Une valeur positive active la rotation,
uniquement après l'envoi et la validation complète de la nouvelle sauvegarde.
Agent ne supprime que les plus anciens dossiers horodatés qui possèdent un
manifeste publié ; une sauvegarde incomplète n'est jamais comptée comme valide.

# mini-trello

**mini-trello** est une application console simple permettant de gérer des tâches sous forme de tableaux (boards), inspirée de l'outil Trello. Elle permet de créer, modifier, déplacer et supprimer des tâches dans différentes colonnes.

## Fonctionnalités

- **Gestion des boards** :
  - Lister les boards existants.
  - Ajouter un nouveau board.
  - Supprimer un board.

- **Gestion des tâches** :
  - Ajouter une tâche à une colonne spécifique.
  - Déplacer une tâche entre colonnes.
  - Supprimer une tâche.
  - Lister les tâches d'une colonne.

## Structure du projet

- `main.py` : Point d'entrée principal du programme. Gère le menu principal et les interactions utilisateur.
- `affichage.py` : Contient les fonctions liées à l'affichage et à l'interaction utilisateur.
- `trello.py` : Contient les fonctions principales pour la gestion des boards et des tâches.
- `gestion_fichiers.py` : Gère la lecture et l'écriture des données dans le fichier `trello.json`.
- `trello.json` : Fichier de stockage des données des boards et des tâches.
- `.gitignore` : Fichier listant les fichiers et dossiers à ignorer par Git.
- `LICENSE` : Licence GNU GPL v2 pour le projet.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <url-du-repo>
   cd mini-trello
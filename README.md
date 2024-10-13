# Jeu de Labyrinthe

Un jeu de labyrinthe développé en Python utilisant Tkinter pour l'interface graphique. Le joueur doit naviguer à travers un labyrinthe généré aléatoirement pour atteindre la sortie tout en collectant des points. Ce projet a été réalisé pour offrir une expérience de jeu immersive avec des graphismes simples et un gameplay engageant.

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Lancement du jeu](#lancement-du-jeu)
- [Contrôles](#contrôles)
- [Mécaniques de jeu](#mécaniques-de-jeu)
- [Contribuer](#contribuer)
- [Acknowlegements](#acknowledgements)
- [License](#license)

## Fonctionnalités

- **Labyrinthe généré aléatoirement** : Chaque partie offre une expérience unique avec un labyrinthe différent.
- **Niveaux de difficulté croissants** : À chaque victoire, le joueur passe au niveau suivant avec un labyrinthe plus complexe.
- **Éclairage dynamique** : Le joueur est accompagné d'une lampe torche qui éclaire son chemin, ajoutant une dimension stratégique à la navigation.
- **Système de score** : Les joueurs gagnent des points chaque fois qu'ils atteignent la sortie.
- **Animations de sprites** : Les personnages sont représentés par des sprites animés pour une expérience visuelle améliorée.
- **Pas de pièges** : Simplification du gameplay en retirant les éléments de piège ou de fausse sortie.

## Technologies utilisées

- **Python 3** : Langage de programmation utilisé pour développer le jeu.
- **Tkinter** : Bibliothèque standard de Python pour créer des interfaces graphiques.
- **Pillow** : Bibliothèque pour le traitement d'images (affichage des sprites).
- **random** : Module de Python pour générer des labyrinthes aléatoires.

## Installation

1. **Prérequis** :
   - Assurez-vous d'avoir Python 3 installé sur votre machine. Vous pouvez télécharger Python [ici](https://www.python.org/downloads/).

2. **Cloner le dépôt** :
   - Clonez ce dépôt ou téléchargez les fichiers dans un dossier de votre choix.

   ```bash
   git clone git@github.com:M10-white/inventory_manager.git
   ```

3. **Installer les dépendances** :
   Installez la bibliothèque Pillow si ce n'est pas déjà fait :

   ```
   pip install Pillow
   ```

4. **Télécharger les images nécessaires** :
   Créez un dossier nommé `assets` dans le répertoire principal du projet et téléchargez les images suivantes :
   - `player_up.png` : Sprite pour le mouvement vers le haut.
   - `player_down.png` : Sprite pour le mouvement vers le bas.
   - `player_left.png` : Sprite pour le mouvement vers la gauche.
   - `player_right.png` : Sprite pour le mouvement vers la droite.
   - `door.png` : Image représentant la sortie.

## Lancement du jeu

Pour démarrer le jeu, exécutez le fichier `maze_game.py` à l'aide de la commande suivante :

```
python maze_game.py
```

## Contrôles

**Flèches directionnelles** :
- Flèche haut : monter
- Flèche bas : descendre
- Flèche gauche : aller à gauche
- Flèche droite : aller à droite

## Mécaniques de jeu

- **Navigation** : Le joueur se déplace à travers le labyrinthe en utilisant les touches fléchées.
- **Éclairage** : Le joueur est éclairé par une lampe torche, qui illumine une zone autour de lui, rendant certaines parties du labyrinthe visibles.
- **Score** : Le score est affiché en haut à gauche de l'écran et est mis à jour chaque fois que le joueur atteint la sortie.
- **Niveaux** : Une fois la sortie atteinte, le joueur passe au niveau suivant avec un nouveau labyrinthe à explorer.

## Contribuer

Si vous souhaitez contribuer à ce projet :

1. Forkez le dépôt.
2. Créez votre branche (`git checkout -b feature/MaFonctionnalité`).
3. Commitez vos changements (`git commit -m 'Ajoute une nouvelle fonctionnalité'`).
4. Poussez vers la branche (`git push origin feature/MaFonctionnalité`).
5. Ouvrez une Pull Request.

## Acknowledgements

- Tkinter pour l'interface graphique.
- Pillow pour le traitement d'images.
- Python pour le langage de programmation.
- Un grand merci à la communauté open source pour leurs ressources et leurs conseils.

## License

Ce projet est sous licence MIT. Pour plus de détails, consultez le fichier LICENSE.

```
N'hésitez pas à ajuster le contenu selon vos préférences ou à ajouter des sections spécifiques que vous jugez nécessaires. Si vous avez d'autres demandes, faites-le moi savoir !
```
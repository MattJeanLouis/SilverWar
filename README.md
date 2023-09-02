
# SilverWar

## Introduction

Bienvenue dans l'univers de SilverWar ! Ce jeu en Python vous transportera dans un monde où les vaisseaux spatiaux règnent en maîtres. Mettez-vous aux commandes de votre propre vaisseau et préparez-vous à des batailles épiques !

## Histoire

Dans un futur lointain, l'humanité a colonisé des planètes aux confins de l'univers. Mais la paix est fragile, et des conflits ont éclaté entre les différentes factions spatiales. Vous êtes le capitaine d'un vaisseau de la flotte Silver, une des factions les plus puissantes. Votre mission, si vous l'acceptez, est de défendre votre territoire contre les flottes adverses et de conquérir de nouveaux mondes. Chaque décision que vous prendrez aura des répercussions sur l'issue de la guerre. Alors choisissez judicieusement et que la force soit avec vous !

## Fonctionnalités Clés

- **Combats en temps réel**: Prenez part à des batailles spatiales intenses.
- **Customisation du vaisseau**: Améliorez vos armes, boucliers et compétences spéciales.


## Dépendances

Ce jeu utilise la bibliothèque `colorama` pour des effets de couleur dans le terminal. Pour l'installer, exécutez la commande suivante :

```
pip install colorama
```

## Comment Jouer

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances avec la commande `pip install -r requirements.txt`.
3. Exécutez `python app.py` pour démarrer le jeu.
4. Suivez les instructions à l'écran pour prendre les commandes de votre vaisseau et entrer en bataille.

## Commandes

- `Attaque` : Pour attaquer un vaisseau ennemi.
- `Défense` : Pour activer les boucliers de votre vaisseau.
- `Compétence` : Pour utiliser une compétence spéciale.

## Licence

Ce jeu est distribué sous la licence MIT. Pour plus d'informations, voir le fichier `LICENSE`.

---


## Explication du Code

Le jeu est écrit en Python et utilise une architecture orientée objet pour organiser le code. Voici un aperçu des principales classes et fonctions :

- `Chateau (à renommer en Vaisseau)`: Cette classe représente un vaisseau (actuellement nommé château). Elle contient des attributs comme `attaque`, `defense`, et `competence`.

- `printf(input_string, delay=0.01)`: Une fonction pour afficher du texte avec un délai entre chaque caractère. Utilisé pour améliorer l'expérience utilisateur.

- `colorama`: Cette bibliothèque est utilisée pour ajouter des effets de couleur dans le terminal.

### Comment le jeu fonctionne

1. Le jeu commence par initialiser votre vaisseau avec des attributs prédéfinis.
2. Vous entrez ensuite dans une boucle de jeu où vous pouvez choisir différentes actions comme attaquer, défendre, etc.
3. Les attributs de votre vaisseau changent en fonction de vos actions, et le jeu se termine lorsque certaines conditions sont remplies.

Note : Le nom `Chateau` sera remplacé par `Vaisseau` dans une future mise à jour.


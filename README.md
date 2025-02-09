## Présentation

Bonjour !

J'ai choisi Python comme langage car c'est celui avec lequel j'ai le plus d'affinité, avec une approche orientée objet pour structurer le code.

J'ai fait l'hypothèse que les lignes du fichier d'entrée apparaissent toujours  suivant l'ordre C - M - T - A, et qu'aucun aventurier n'a de séquence vide.

## Description des classes

### Cell 
    
Une case (cellule) sur la carte est représentée par une classe **Cell**. La classe possède deux attributs : 
* La valeur, qui indique le nombre de trésors à récupérer sur la cellule 
* L'accessibilité, qui indique si un aventurier peut se rendre sur la cellule

Voici la correspondance entre le type de cellule et les valeurs de ses attributs :

|       | Plaine | Montagne | Trésor | Aventurier | Aventurier et Trésor |
|-------|:----------:|:----------:|:----------:|:----------:|:----------:|
| **Valeur** | 0  | -1  | t >= 1  | 0  | t >= 1  |
| **Accessibilité** | True  | False  | True  | False  | False  |

La valeur -1 pour les cellules Montagne permet de faire la distinction avec une cellule Aventurier.

### Map

La classe **Map** permet de représenter la carte par une matrice rectangulaire de **Cell**. Le programme principal met à jour la carte de manière itérative. 

### Adventurer 

Un aventurier est implémenté grâce à la classe **Adventurer** qui conserve les informations suivantes :
* Son nom
* Ses coordonnées sur la carte
* Son orientation 
* La séquence de mouvements qu'il lui reste à faire
* Le nombre de trésors qu'il a ramassés

### Group 

La classe **Group** correspond à un groupe d'aventurier, c'est à dire une liste d'aventuriers de type **Adventurer**.

## Fonctionnement

Le programme **main** fonctionne en trois temps :
1. Récupération du fichier d'entrée pour la création de la carte et du groupe d'aventuriers  
2. Boucle principale. À chaque itération, les aventuriers effectuent un mouvement de leur séquence en suivant l'ordre d'apparition dans le fichier d'entrée
3. Affichage final

## Utilisation

Le format d'entrée doit être respecté.
### Une entrée 
```
python3 main.py inputs/num_du_fichier.txt
```
### Plusieurs fichiers ayant chacun 

### Lancer tous les tests
```
python3 -m unittest discover tests/
```
### Lancer un test spécifique
```
python3 -m unittest tests.nom_du_test
```

from src.map import Map 
from src.group import Group
import sys
import os

def main(input_file):


    ## ---------------------------------- Récupération et convertion de l'input ---------------------------------- ##

    # Ajout d'une ligne vide à la fin du fichier pour traiter correctement la dernière ligne
    with open(input_file, 'a') as f:
        f.write('\n')
    # Récupération du fichier d'entrée
    with open(input_file, 'r') as f:
        tmp = f.readlines()
        lignes = list(tmp)
        # Création de la carte et du groupe d'aventuriers
        map = Map(lignes)
        group = Group(lignes)
    #with open(input_file, 'w') as f:
    #   f.writelines(lignes[:-1])


    ## -------------------------------------------- Boucle principale -------------------------------------------- ##

    # Condition d'arrêt : tous les aventuriers ont fini leur séquence
    while not group.allDone():
        for adventurer in group.get():
            # Vérification de l'état de la séquence de l'aventurier
            if not adventurer.isDone():
                # Récupération du prochain mouvement de l'aventurier
                next_move = adventurer.getNextMove()
                # Cas où le mouvement est tourner
                if next_move == 'D' or next_move == 'G':
                    adventurer.setOrientation(next_move)
                # Cas où le mouvement est avancer
                else:
                    # Vérification de l'accessibilité de la cellule devant l'aventurier
                    x_next, y_next = adventurer.getNextCell()
                    if map.getAccessibility(x_next, y_next):
                        # Mise à jour de la position de l'aventurier
                        x_cur, y_cur = adventurer.getPosition()
                        adventurer.setPosition(x_next, y_next)
                        # Mise à jour de l'accessibilité de la case où l'aventurier était
                        map.setCellAccessibility(x_cur, y_cur, True)
                        # Mise à jour de l'accessibilité de la case où l'aventurier vient de se rendre
                        map.setCellAccessibility(x_next, y_next, False)
                        # Vérification de la présence d'un trésor sur la case où l'aventurier vient de se rendre
                        if map.hasTreasures(x_next, y_next):
                            # Retrait d'un trésor de la cellule
                            map.removeTreasure(x_next, y_next)
                            # Ajout d'un trésor à l'aventurier
                            adventurer.addTreasure()
                # Incrémentation éventuelle du nombre d'aventuriers qui ont fini
                if adventurer.isDone(): group.addAdventurerDone()
                else: continue
            else: continue


    ## --------------------------------------------- Affichage final --------------------------------------------- ##

    map.display()
    group.display()



if len(sys.argv) != 2:
    print("Veuillez respecter le format de la commande : python3 main.py <chemin_relatif_du_fichier>")
    sys.exit(1)

input_file = sys.argv[1]

if not os.path.exists(input_file):
   print(f"Erreur : Le fichier '{input_file}' n'existe pas.")
else:
    main(input_file)

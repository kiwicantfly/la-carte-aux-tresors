# class Group:
#   list[Adventurer] group
#   int number_of_adventurers
#   int number_of_adventurers_done 

from src.adventurer import Adventurer

class Group:
    def __init__(self, input_file):
        self.__group = []
        self.__number_of_adventurers = 0
        self.__number_of_adventurers_done = 0
        for line in input_file:
            if line[0] == 'A':
                self.__number_of_adventurers += 1
                name, x, y, orientation, sequence = tuple(line[4:-1].split(" - "))
                x, y = int(x), int(y)
                adventurer = Adventurer(name, x, y, orientation, sequence)
                self.__group.append(adventurer)
            else: continue

    # Renvoie la liste des d'aventuriers
    def get(self) -> None:
        return self.__group

    # Renvoie le nombre d'aventuriers 
    def getNumberOfAdventurers(self) -> int:
        return self.__number_of_adventurers
    
    # Renvoie le nombre d'aventuriers qui ont fini leur séquence
    def getNumberOfAdventurersDone(self) -> int:
        return self.__number_of_adventurers_done

    # Ajoute 1 au nombre d'aventuriers qui ont fini leur séquence
    def addAdventurerDone(self) -> None:
        self.__number_of_adventurers_done += 1
    
    # Renvoie vrai si tous les aventuriers ont réalisé leur séquence
    def allDone(self) -> bool:
        return self.__number_of_adventurers == self.__number_of_adventurers_done

    # Affiche tous les aventuriers du groupe
    def display(self) -> None:
        for adventurer in self.__group:
            adventurer.display()
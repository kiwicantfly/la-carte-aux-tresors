# class Adventurer:
#   str name
#   int x
#   int y
#   str orientation
#   list[str] sequence
#   int treasure 

# Matrice qui permet de déterminer la prochaine orientation de l'aventurier
next_orientation = {'N': {'G':'O', 'D':'E'},
                    'E': {'G':'N', 'D':'S'},
                    'S': {'G':'E', 'D':'O'},
                    'O': {'G':'S', 'D':'N'}
                    }

class Adventurer:
    def __init__(self, name: str, x0: int, y0: int, orientation: str, sequence: str):
        self.__name = name
        self.__x = x0
        self.__y = y0
        self.__orientation = orientation
        self.__sequence = list(sequence)
        self.__treasure = 0

    # Renvoie l'orientation de l'aventurier
    def getOrientation(self) -> str:
        return self.__orientation
    
    # Renvoie le nombre de trésors de l'aventurier
    def getTreasure(self) -> int:
        return self.__treasure
    
    # Renvoie les coordonnées de l'aventurier
    def getPosition(self) -> tuple[int, int]:
        return self.__x, self.__y
    
    # Modifie les coordonnées de l'aventurier 
    def setPosition(self, x: int, y: int) -> None:
        self.__x, self.__y = x, y
    
    # Établit l'orientation de l'aventurier après avoir tourné à gauche ou à droite
    def setOrientation(self, direction: str) -> None:
        self.__orientation = next_orientation[self.__orientation][direction]

    # Ajoute un trésor à l'aventurier
    def addTreasure(self) -> None:
        self.__treasure += 1

    # Renvoie vrai si l'aventurier a réalisé tous les mouvements de la séquence
    def isDone(self) -> bool:
        return len(self.__sequence) == 0
    
    # Renvoie le prochain mouvement de la séquence et l'enlève de la séquence
    def getNextMove(self) -> str:
        if len(self.__sequence) > 0 : return self.__sequence.pop(0)
        return ''

    # Renvoie les coordonnées de la cellule se situant devant l'aventurier
    def getNextCell(self) -> tuple[int, int]:
        if self.__orientation == 'N':
            return self.__x, self.__y - 1
        elif self.__orientation == 'S':
            return self.__x, self.__y + 1
        elif self.__orientation == 'E':
            return self.__x + 1, self.__y
        else:
            return self.__x - 1, self.__y
    
    def display(self) -> None:
        print("A -", self.__name, "-", self.__x, "-", self.__y, "-", self.__orientation, "-", self.__treasure, end='\n')
# class Cell:
#   int value
#   bool accessibility
#
# value =
#   0 si la cellule est une plaine
#   -1 si la cellule est une montagne
#   t >= 1 si la cellule est un trésor
#
# accessibility = 
#   True si la cellule est une plaine
#   True si la cellule est un trésor
#   False si la cellule est une montagne
#   False si la cellule est un aventurier
#   False si la cellule est un trésor avec un aventurier

class Cell:
    # Une cellule est une plaine par défaut
    def __init__(self, accessibility: bool = True, value: int = 0):
        self.__value = value
        self.__accessibility = accessibility
    
    # Renvoie la valeur de la cellule
    def getValue(self) -> int:
        return self.__value
    
    # Renvoie l'accessibilité de la cellule 
    def getAccessibility(self) -> bool:
        return self.__accessibility
    
    # Modifie l'accessibilité de la cellule 
    def setAccessibility(self, accessibility: bool) -> None:
        self.__accessibility = accessibility
    
    # Modifie la valeur de la cellule 
    def setValue(self, value: int) -> None:
        self.__value = max(0, value)
        
# class Map:
#   int col
#   int row
#   list[list[Cell]] map
#   list[str] display
#   dict[tuple[[int, int], int] treasure
#
# treasure =
#   hash table : [clé = coordonnées du trésor, valeur = nombre de trésors]


from src.cell import Cell

class Map:
    def __init__(self, input_file: list[str]):  
        # On fait l'hypothèse que la première ligne donne les dimensions de la carte
        assert input_file[0][0] == 'C', "Veuillez donner les dimensions de la carte dans la première ligne."
        self.__col, self.__row = tuple(input_file[0][4:-1].split(" - "))
        self.__col, self.__row = int(self.__col), int(self.__row)
        self.__map = [[Cell() for _ in range(self.__col)] for _ in range(self.__row)]     
        # Récupération des lignes 'C' et 'M' pour l'affichage final
        self.__display = [input_file[0][:-1]]
        # Récupération des trésors dans une hash table  
        self.__treasures = dict()
        for line in input_file:
            if line[0] == 'M':
                self.__display.append(line[:-1])
                x, y = tuple(line[4:-1].split(" - "))
                x, y = int(x), int(y)
                self.__map[y][x] = Cell(False, -1)
            elif line[0] == 'T':
                x, y, t = tuple(line[4:-1].split(" - "))
                x, y, t = int(x), int(y), int(t)
                self.__map[y][x] = Cell(True, t)
                self.__treasures[(x, y)] = t
            elif line[0] == 'A':
                _, x, y, _, _ = tuple(line[4:-1].split(" - "))
                x, y = int(x), int(y)
                self.__map[y][x] = Cell(False, 0)
            else: continue

    # Renvoie vrai si la cellule située aux coordonnées x y est accessible
    def getAccessibility(self, x: int, y: int) -> bool:
        # Cas où on sort de la carte
        if x >= self.__col or x < 0 or y >= self.__row or y < 0: return False
        # Cas où on est dans la carte
        return self.__map[y][x].getAccessibility()

    # Change l'accessibilité de la cellule située aux coordonnées x y
    def setCellAccessibility(self, x: int, y: int, accessibility: bool) -> None:
        self.__map[y][x].setAccessibility(accessibility)
    
    # Indique si un trésor peut être récupéré dans la cellule
    def hasTreasures(self, x: int, y: int) -> bool:
        return self.__map[y][x].getValue() > 0
    
    # Enlève un trésor d'une cellule
    def removeTreasure(self, x: int, y: int) -> None:
        cell_value = self.__map[y][x].getValue()
        if cell_value > 0:
            self.__map[y][x].setValue(cell_value - 1)
            self.__treasures[(x, y)] -= 1
            self.__removeFromTreasuresDict(x, y)
        else: pass

    # Retire la cellule de la hash table si la cellule n'a plus de trésors
    def __removeFromTreasuresDict(self, x: int, y: int) -> None:
        if self.__treasures[(x, y)] == 0:
            del self.__treasures[(x, y)]
        else: pass

    # Affichage final des lignes 'C', 'M' et 'T'
    def display(self) -> None:
        for line in self.__display:
            print(line)
        for coordinates, value in self.__treasures.items():
            print("T -", coordinates[0], "-", coordinates[1], "-", value)
    
#--------------------------------------------------------------------------------------------------------------------------------    

    # Affichage de la carte pour voir les valeurs et l'accessibilité des cases
    def displayValueAccessibility(self) -> None:
        for i in range(self.__row):
            for j in range(self.__col):
                print((self.__map[i][j].getValue(), self.__map[i][j].getAccessibility()), end='\t')
            print('\n')

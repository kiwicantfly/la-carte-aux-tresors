from random import randint
import sys

def generate_map(col=5, row=5, M=8, T=4, Tmax=3, A=5, Smax=10):
    assert A + T + M <= col * row, "La somme du nombre de montagnes, du nombre de trésors et du nombre d'aventuriers ne doit pas dépasser la taille de la carte !"
    pick = [(k%col, k//col) for k in range(col*row)]
    print(f'C - {col} - {row}', end='\n')
    for _ in range(M):
        m = pick.pop(randint(0, len(pick)-1))
        print(f'M - {m[0]} - {m[1]}', end='\n')
    for _ in range(T):
        t = pick.pop(randint(0, len(pick)-1))
        print(f'T - {t[0]} - {t[1]} - {randint(1, Tmax)}', end='\n')
    orientation = ['N', 'S', 'E', 'O']
    movement = ['A', 'A', 'G', 'D']
    for k in range(A):
        a = pick.pop(randint(0, len(pick)-1))
        s = randint(5, Smax)
        sequence = ''
        for _ in range(s):
            sequence += movement[randint(0, 3)]
        print(f'A - Aventurier{k} - {a[0]} - {a[1]} - {orientation[randint(0, 3)]} - {sequence}', end='\n')

with open("inputs/input_generated.txt", 'w') as input_file:
    sys.stdout = input_file
    generate_map()
    sys.stdout = sys.__stdout__
    print("Un nouveau fichier input_generated.txt a été créé. Vous pouvez le consulter dans le dossier inputs.")


from random import randint

def generate_map(col=5, row=5, M=8, T=4, Tmax=3, A=5, Smax=10):
    assert A + T + M <= col * row
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

generate_map(5, 9, 10, 15, 5, 20, 30)
import time
from PIL import Image
import numpy as np
from random import seed
from random import randint
import keyboard

# R = Player
# O = Wall
#  = Tile
# S = Target
# B = Box
# * = B

Grid = []

Gridx = int(input('Give Grid x size:\n'))
Gridy = int(input('Give Grid y size:\n'))
for i in range(Gridx*Gridy):
    Grid.append('0')

Grid = np.reshape(Grid, (Gridx, Gridy))

for i in [0, Gridx-1]:
    for j in range(0, Gridy):
        Grid[i][j] = 'O'

for i in range(0, Gridx):
    for j in [0, Gridy-1]:
        Grid[i][j] = 'O'

for i in range(0, Gridx):
    for j in range(0, Gridy):
        if Grid[i][j] != 'O':
            Grid[i][j] = ' '

Fax = 1

while Fax == 1:
    Px = int(input('Give player position x:\n'))
    Py = int(input('Give player position y:\n'))
    if Grid[Px][Py] == ' ':     # Zid out of bound
        Fax = 0
    else:
        print('Invalid Position\n')

Grid[Px][Py] = 'R'

NB = int(input('Number of boxes:\n'))
for i in range(NB):
    Fax = 1
    while Fax == 1:
        Bx = int(input('Give Box ' + str(i) + ' position x:\n'))
        By = int(input('Give Box ' + str(i) + ' position y:\n'))
        if Grid[Bx][By] == ' ':  # Zid out of bound
            Fax = 0
            Grid[Bx][By] = 'B'
        else:
            print('Invalid Position\n')

for i in range(NB):
    Fax = 1
    while Fax == 1:
        Bx = int(input('Give target ' + str(i) + ' position x:\n'))
        By = int(input('Give target ' + str(i) + ' position y:\n'))
        if Grid[Bx][By] == ' ':  # Zid out of bound
            Fax = 0
            Grid[Bx][By] = 'S'
        else:
            print('Invalid Position\n')

NW = int(input('Number of walls to add:\n'))

print(Grid)
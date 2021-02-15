"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import os

ON = 255
OFF = 0
vals = [ON, OFF]
gen = 1
datas = ""


def randomGrid(N):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

'''def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 255, 255, 255, 255, 0],
                             [0, 255, 0, 0, 0, 255, 0],
                             [0, 0, 0, 0, 0, 255, 0],
                             [0, 255, 0, 0, 255, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]])
    #glider = np.array([[0,    0, 255], 
     #                  [255,  0, 255],
      #                 [0,  255, 255]])
    grid[i:i+6, j:j+7] = glider'''

#STILL LIFES
def block(newGrid, N):
    cBlock = 0
    auxGrid = newGrid.copy()
    isBlock = False
    block = np.array([[0, 0, 0, 0],
                      [0, 255, 255, 0],
                      [0, 255, 255, 0],
                      [0, 0, 0, 0]])

    auxBlock = np.zeros((4,4))

    for i in range(N):
        for j in range(N):
            for auxX in range(4):
                for auxY in range(4):
                    try:
                        auxBlock[auxX][auxY] = newGrid[i+auxX][j+auxY]
                    except IndexError:
                        auxBlock[auxX][auxY] = 0
                        pass

            #print("aux Block", auxBlock)
            isBlock = (auxBlock == block).all()
            #print("is block", isBlock)
            if(isBlock):
                cBlock = cBlock + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(4):
                            for auxY in range(4):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass

        isBlock = False
        #print("cBlock: ", cBlock)
    return cBlock, auxGrid

def beehive(newGrid, N):
    cBeehive = 0
    auxGrid = newGrid.copy()
    isBeehive = False
    beehive = np.array([[0, 0, 0, 0, 0, 0],
                        [0, 0, 255, 255, 0, 0],
                        [0, 255, 0, 0, 255, 0],
                        [0, 0, 255, 255, 0, 0],
                        [0, 0, 0, 0, 0, 0]])

    auxBeeh = np.zeros((5, 6))

    for i in range(N):
        for j in range(N):
            for auxX in range(5):
                for auxY in range(6):
                    try:
                        auxBeeh[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxBeeh[auxX][auxY] = 0
                        pass

            isBeehive = (auxBeeh == beehive).all()
            if (isBeehive):
                cBeehive = cBeehive + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(5):
                            for auxY in range(6):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass

        isBeehive = False
    return cBeehive, auxGrid

def loaf(newGrid, N):
    cLoaf = 0
    auxGrid = newGrid.copy()
    isLoaf = False
    loaf = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, 255, 255, 0, 0],
                     [0, 255, 0, 0, 255, 0],
                     [0, 0, 255, 0, 255, 0],
                     [0, 0, 0, 255, 0, 0],
                     [0, 0, 0, 0, 0, 0]])

    auxLoaf = np.zeros((6, 6))

    for i in range(N):
        for j in range(N):
            for auxX in range(6):
                for auxY in range(6):
                    try:
                        auxLoaf[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxLoaf[auxX][auxY] = 0
                        pass

            isLoaf = (auxLoaf == loaf).all()
            if (isLoaf):
                cLoaf = cLoaf + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(6):
                            for auxY in range(6):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass
        isLoaf = False
    return cLoaf, auxGrid

def boat(newGrid, N):
    cBoat = 0
    auxGrid = newGrid.copy()
    isBoat = False
    boat = np.array([[0, 0, 0, 0, 0],
                     [0, 255, 255, 0, 0],
                     [0, 255, 0, 255, 0],
                     [0, 0, 255, 0, 0],
                     [0, 0, 0, 0, 0]])

    auxBoat = np.zeros((5, 5))

    for i in range(N):
        for j in range(N):
            for auxX in range(5):
                for auxY in range(5):
                    try:
                        auxBoat[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxBoat[auxX][auxY] = 0
                        pass

            isBoat = (auxBoat == boat).all()
            if (isBoat):
                cBoat = cBoat + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(5):
                            for auxY in range(5):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass

        isBoat = False
    return cBoat, auxGrid

def tub(newGrid, N):
    cTub = 0
    auxGrid = newGrid.copy()
    isTub = False
    tub = np.array([[0, 0, 0, 0, 0],
                    [0, 0, 255, 0, 0],
                    [0, 255, 0, 255, 0],
                    [0, 0, 255, 0, 0],
                    [0, 0, 0, 0, 0]])

    auxTub = np.zeros((5, 5))

    for i in range(N):
        for j in range(N):
            for auxX in range(5):
                for auxY in range(5):
                    try:
                        auxTub[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxTub[auxX][auxY] = 0
                        pass

            isTub = (auxTub == tub).all()
            if (isTub):
                cTub = cTub + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(5):
                            for auxY in range(5):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass

        isTub = False
    return cTub, auxGrid

#OSCILATORS
def blinker(newGrid, N):
    cBlink = 0
    auxGrid = newGrid.copy()
    blinker1 = np.array([[0, 0, 0, 0, 0],
                         [0, 0, 255, 0, 0],
                         [0, 0, 255, 0, 0],
                         [0, 0, 255, 0, 0],
                         [0, 0, 0, 0, 0]])

    blinker2 = np.array([[0, 0, 0, 0, 0],
                         [0, 255, 255, 255, 0],
                         [0, 0, 0, 0, 0]])

    auxBlink1 = np.zeros((5, 5))
    auxBlink2 = np.zeros((3, 5))

    for i in range(N):
        for j in range(N):
            for auxX in range(5):
                for auxY in range(5):
                    try:
                        auxBlink1[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxBlink1[auxX][auxY] = 0
                        pass

            for auxX in range(3):
                for auxY in range(5):
                    try:
                        auxBlink2[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxBlink2[auxX][auxY] = 0
                        pass

            if ((auxBlink1 == blinker1).all() or (auxBlink2 == blinker2).all()):
                cBlink = cBlink + 1
                if(auxBlink1 == blinker1).all():
                    for i in range(N):
                        for j in range(N):
                            for auxX in range(5):
                                for auxY in range(5):
                                    try:
                                        auxGrid[i + auxX][j + auxY] = 0
                                    except IndexError:
                                        pass
                elif (auxBlink2==blinker2).all():
                    for i in range(N):
                        for j in range(N):
                            for auxX in range(3):
                                for auxY in range(5):
                                    try:
                                        auxGrid[i + auxX][j + auxY] = 0
                                    except IndexError:
                                        pass

    return cBlink, auxGrid

def toad(newGrid, N):
    cToad = 0
    auxGrid = newGrid.copy()
    toad1 = np.array([[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 255, 0, 0],
                      [0, 255, 0, 0, 255, 0],
                      [0, 255, 0, 0, 255, 0],
                      [0, 0, 255, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0]])

    toad2 = np.array([[0, 0, 0, 0, 0, 0],
                      [0, 0, 255, 255, 255, 0],
                      [0, 255, 255, 255, 0, 0],
                      [0, 0, 0, 0, 0, 0]])

    auxToad1 = np.zeros((6, 6))
    auxToad2 = np.zeros((4, 6))

    for i in range(N):
        for j in range(N):
            for auxX in range(6):
                for auxY in range(6):
                    try:
                        auxToad1[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxToad1[auxX][auxY] = 0
                        pass

            for auxX in range(4):
                for auxY in range(6):
                    try:
                        auxToad2[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxToad2[auxX][auxY] = 0
                        pass

            if ((auxToad1 == toad1).all() or (auxToad2 == toad2).all()):
                cToad = cToad + 1
                if(auxToad1==toad1).all():
                    for i in range(N):
                        for j in range(N):
                            for auxX in range(6):
                                for auxY in range(6):
                                    try:
                                        auxGrid[i + auxX][j + auxY] = 0
                                    except IndexError:
                                        pass
                elif(auxToad2==toad2).all():
                    for i in range(N):
                        for j in range(N):
                            for auxX in range(4):
                                for auxY in range(6):
                                    try:
                                        auxGrid[i + auxX][j + auxY] = 0
                                    except IndexError:
                                        pass

    return cToad, auxGrid

def beacon(newGrid, N):
    cBeacon = 0
    auxGrid = newGrid.copy()
    beacon1 = np.array([[0, 0, 0, 0, 0, 0],
                        [0, 255, 255, 0, 0, 0],
                        [0, 255, 255, 0, 0, 0],
                        [0, 0, 0, 255, 255, 0],
                        [0, 0, 0, 255, 255, 0],
                        [0, 0, 0, 0, 0, 0]])

    beacon2 = np.array([[0, 0, 0, 0, 0, 0],
                        [0, 255, 255, 0, 0, 0],
                        [0, 255, 0, 0, 0, 0],
                        [0, 0, 0, 0, 255, 0],
                        [0, 0, 0, 255, 255, 0],
                        [0, 0, 0, 0, 0, 0]])

    auxBeac1 = np.zeros((6, 6))
    auxBeac2 = np.zeros((6, 6))

    for i in range(N):
        for j in range(N):
            for auxX in range(6):
                for auxY in range(6):
                    try:
                        auxBeac1[auxX][auxY] = newGrid[i + auxX][j + auxY]
                        auxBeac2[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxBeac1[auxX][auxY] = 0
                        auxBeac2[auxX][auxY] = 0
                        pass

            if ((auxBeac1 == beacon1).all() or (auxBeac2 == beacon2).all()):
                cBeacon = cBeacon + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(6):
                            for auxY in range(6):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass

    return cBeacon, auxGrid

#SPACESHIPS
def glider(newGrid, N):
    cGlider = 0
    isGlid = False
    auxGrid = newGrid.copy()
    glider1 = np.array([[0, 0, 0, 0, 0],
                        [0, 0, 255, 0, 0],
                        [0, 0, 0, 255, 0],
                        [0, 255, 255, 255, 0],
                        [0, 0, 0, 0, 0]])

    glider2 = np.array([[0, 0, 0, 0, 0],
                        [0, 255, 0, 255, 0],
                        [0, 0, 255, 255, 0],
                        [0, 0, 255, 0, 0],
                        [0, 0, 0, 0, 0]])

    glider3 = np.array([[0, 0, 0, 0, 0],
                        [0, 0, 0, 255, 0],
                        [0, 255, 0, 255, 0],
                        [0, 0, 255, 255, 0],
                        [0, 0, 0, 0, 0]])

    glider4 = np.array([[0, 0, 0, 0, 0],
                        [0, 255, 0, 0, 0],
                        [0, 0, 255, 255, 0],
                        [0, 255, 255, 0, 0],
                        [0, 0, 0, 0, 0]])

    auxGlid1 = np.zeros((5, 5))
    auxGlid2 = np.zeros((5, 5))
    auxGlid3 = np.zeros((5, 5))
    auxGlid4 = np.zeros((5, 5))

    for i in range(N):
        for j in range(N):
            for auxX in range(5):
                for auxY in range(5):
                    try:
                        auxGlid1[auxX][auxY] = newGrid[i + auxX][j + auxY]
                        auxGlid2[auxX][auxY] = newGrid[i + auxX][j + auxY]
                        auxGlid3[auxX][auxY] = newGrid[i + auxX][j + auxY]
                        auxGlid4[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxGlid1[auxX][auxY] = 0
                        auxGlid2[auxX][auxY] = 0
                        auxGlid3[auxX][auxY] = 0
                        auxGlid4[auxX][auxY] = 0
                        pass

            if ((auxGlid1 == glider1).all() or (auxGlid2 == glider2).all() or (auxGlid3 == glider3).all() or (auxGlid4 == glider4).all()):
                cGlider = cGlider + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(5):
                            for auxY in range(5):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass

    return cGlider, auxGrid

def lightWeight(newGrid, N):
    cLight = 0
    auxGrid = newGrid.copy()
    lightWeight1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                             [0, 255, 0, 0, 255, 0, 0],
                             [0, 0, 0, 0, 0, 255, 0],
                             [0, 255, 0, 0, 0, 255, 0],
                             [0, 0, 255, 255, 255, 255, 0],
                             [0, 0, 0, 0, 0, 0, 0]])

    lightWeight2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 255, 255, 0, 0],
                             [0, 255, 255, 0, 255, 255, 0],
                             [0, 255, 255, 255, 255, 0, 0],
                             [0, 0, 255, 255, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]])

    lightWeight3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 255, 255, 255, 255, 0],
                             [0, 255, 0, 0, 0, 255, 0],
                             [0, 0, 0, 0, 0, 255, 0],
                             [0, 255, 0, 0, 255, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]])

    lightWeight4 = np.array([[0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 255, 255, 0, 0, 0],
                             [0, 255, 255, 255, 255, 0, 0],
                             [0, 255, 255, 0, 255, 255, 0],
                             [0, 0, 0, 255, 255, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]])

    auxLight1 = np.zeros((6, 7))
    auxLight2 = np.zeros((6, 7))
    auxLight3 = np.zeros((6, 7))
    auxLight4 = np.zeros((6, 7))

    for i in range(N):
        for j in range(N):
            for auxX in range(6):
                for auxY in range(7):
                    try:
                        auxLight1[auxX][auxY] = newGrid[i + auxX][j + auxY]
                        auxLight2[auxX][auxY] = newGrid[i + auxX][j + auxY]
                        auxLight3[auxX][auxY] = newGrid[i + auxX][j + auxY]
                        auxLight4[auxX][auxY] = newGrid[i + auxX][j + auxY]
                    except IndexError:
                        auxLight1[auxX][auxY] = 0
                        auxLight2[auxX][auxY] = 0
                        auxLight3[auxX][auxY] = 0
                        auxLight4[auxX][auxY] = 0
                        pass

            if (auxLight1 == lightWeight1).all() or (auxLight2 == lightWeight2).all() or (auxLight3 == lightWeight3).all() or (auxLight4 == lightWeight4).all():
                cLight = cLight + 1
                for i in range(N):
                    for j in range(N):
                        for auxX in range(6):
                            for auxY in range(7):
                                try:
                                    auxGrid[i + auxX][j + auxY] = 0
                                except IndexError:
                                    pass

    return cLight, auxGrid

def others(newGrid, N):
    others = 0
    for i in range(N):
        for j in range(N):
            if newGrid[i][j] == 255:
                others = others + 1

    return others

def update(frameNum, img, grid, N):
    global gen
    print("Generation: ", gen)
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()
    # TODO: Implement the rules of Conway's Game of Life
    for i in range(N):
        for j in range(N):
            alive = 0

            try:
                if (grid[i + 1][j - 1] == 255):
                    alive = alive + 1
                if (grid[i][j - 1] == 255):
                    alive = alive + 1
                if (grid[i - 1][j - 1] == 255):
                    alive = alive + 1
                if (grid[i - 1][j] == 255):
                    alive = alive + 1
                if (grid[i - 1][j + 1] == 255):
                    alive = alive + 1
                if (grid[i][j + 1] == 255):
                    alive = alive + 1
                if (grid[i + 1][j + 1] == 255):
                    alive = alive + 1
                if (grid[i + 1][j] == 255):
                    alive = alive + 1
            except IndexError:
                pass

            if (newGrid[i][j] == 255):
                if (alive < 2):
                    newGrid[i][j] = 0
                elif (alive > 3):
                    newGrid[i][j] = 0
            elif(newGrid[i][j] == 0):
                if (alive == 3):
                    newGrid[i][j] = 255

    #Counting blinkers, gliders, etc.
    tBlock, newGrid1 = block(newGrid, N)
    tBeehi, newGrid2 = beehive(newGrid1, N)
    tLoaf, newGrid3 = loaf(newGrid2, N)
    tBoat, newGrid4 = boat(newGrid3, N)
    tTub, newGrid5 = tub(newGrid4, N)

    tBlink, newGrid6 = blinker(newGrid5, N)
    tToad, newGrid7 = toad(newGrid6, N)
    tBeacon, newGrid8 = beacon(newGrid7, N)

    tGlider, newGrid9 = glider(newGrid8, N)
    tLight, newGrid10 = lightWeight(newGrid9, N)

    tOthers = others(newGrid10, N)

    global datas
    datas = datas + "\n###### Generation: " + str(gen) + " ######\n" + "Total Blocks: " + str(
        tBlock) + "\nTotal Beehive: " + str(tBeehi) + "\nTotal Loafs: " + str(tLoaf) + \
            "\nTotal Boats: " + str(tBoat) + "\nTotal Tubs: " + str(tTub) + "\nTotal Blinkers: " + str(
        tBlink) + "\nTotal Toads: " + str(tToad) + "\nTotal Beacons: " + str(tBeacon) + \
            "\nTotal Gliders: " + str(tGlider) + "\nTotal Light-weight spaceship: " + str(tLight) + "\nTotal others: " + str(tOthers) + "\n"
    #print(datas)

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    gen = gen + 1

    #if frameNum == gen-1:
    info = open("info.txt", 'w')
    n = info.write(datas)
    info.close()

    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments

    file = open('inputC.txt', 'r')
    lines = file.readlines()
    datas = ""
    
    # set grid size
    N = 0
        
    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    #grid = randomGrid(N) #Creates a random grid
    # Uncomment lines to see the "glider" demo
    #addGlider(1, 1, grid)

    for i in range(len(lines)):
        if i==0:
            N=int(lines[i])
            grid = np.zeros(N * N).reshape(N, N)
            continue
        data = lines[i].split(',')
        coordX = int(data[0])
        coordY = int(data[1])
        grid[coordX][coordY] = 255

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                  frames = 5,
                                  interval=updateInterval,
                                  save_count=50,
                                  repeat=False )

    plt.show()

# call main
if __name__ == '__main__':
    main()
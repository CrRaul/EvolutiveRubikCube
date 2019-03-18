from Chromosome import Chromosome
from RubikCube import RubikCube
from ControllerRubikCube import ControllerRubikCube
import random


population = []
dimPop = 50
iteratorGen = 0
numOfMoves = 100

bestFitnessFile = open("bestFitnessFile.txt","a")
movesBestGenFile = open("movesBestGenFile.txt", "a")
bestFitnessFile.write("Gen      Fit      Moves\n" )



def setCube():
    r = RubikCube()
    r.initColor()
    c = ControllerRubikCube(r)
   # F R B D F F U' D' R D L R' U B' U L'
    c.moveFace(0)
    c.moveFace(2)
    c.moveFace(4)
    c.moveFace(10)
    c.moveFace(0)
    c.moveFace(0)
    c.moveFace(9)
    c.moveFace(11)
    c.moveFace(2)
    c.moveFace(10)
    c.moveFace(6)
    c.moveFace(3)
    c.moveFace(8)
    c.moveFace(5)
    c.moveFace(8)
    c.moveFace(7)

    return c.returnCube()

def fitnessPop(cube):
    for i in range(0, dimPop):
        population[i].fitnessCalc(cube)

def XO(F, M):
    mF = F.returnMoves()
    mM = M.returnMoves()
    posF = F.returnPosFitMax()
    posM = M.returnPosFitMax()

    mXO = []

    

    XO = Chromosome(numOfMoves)
    XO.setMoves(mXO)
    return XO

def fitnessSum():
    sum = 0 
    for i in range(0, dimPop):
        sum += population[i].returnFitness()
    return sum

# RSW
def selection(sum): 
    sum = random.uniform(0, sum)
    s = 0
    for i in range(0, dimPop):
        s += population[i].returnFitness()
        if(s >= sum):
            return population[i]

def getBest():
    best = population[0]
    for i in range(1, dimPop):
        if population[i].returnFitness() > best.returnFitness():
            best = population[i]
    return best

def sortPop(): 
    for i in range(0, dimPop):
        for j in range(i, dimPop):
            if population[i].returnFitness() < population[j].returnFitness():
                a = population[i]
                population[i] = population[j]
                population[j] = a
##########################################################################################

cube = setCube()
print(cube.returnMatrix())
for i in range(0, dimPop):
    population.append(Chromosome(numOfMoves))
fitnessPop(cube)

while(True):
    newPop = []
    sortPop()
    sum = fitnessSum()

    for j in range(0, dimPop):
        M = selection(sum)
        F = selection(sum)
        xo = XO(F,M)

        prob = random.uniform(0,1)
        if prob < 0.05:
            xo.mutation(10)

        xo.fitnessCalc(cube)

        newPop.append(xo)

    population = newPop[:]
    fitnessPop(cube)

    bestChr = getBest()
    bestFit = bestChr.returnFitness()
    bestFitnessFile.write(str(iteratorGen) + "   " + str(bestFit) + "    " + str(bestChr.returnPosFitMax()) + "\n")
    movesBestGenFile.write(str(iteratorGen) + "   " + str(bestChr.returnMoves()) + "\n")
    print(iteratorGen)
    if(bestFit > 0.9):
        break

    if(iteratorGen % 20 ==0):
        bestFitnessFile.close()
        movesBestGenFile.close()
        bestFitnessFile = open("bestFitnessFile.txt","a")
        movesBestGenFile = open("movesBestGenFile.txt", "a")

    iteratorGen += 1


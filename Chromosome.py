from ControllerRubikCube import ControllerRubikCube
import random

class Chromosome():
    def __init__(self, numberOfMoves):
        self.__moves = []
        self.__numMoves = numberOfMoves
        self.__fitness = 0
        self.__posFitMax = 0

        for i in range(0,self.__numMoves):
            self.__moves.append(random.randint(0,11))

    def setMoves(self, moves):
        self.__moves = moves[:]

    # Calculate the fitness of the cube in some moment
    def fitStateCube(self, matr):
        posX = [0,1,0,-1,-1,1,1,-1]
        posY = [-1,0,1,0,-1,-1,1,1]

        num = 6

        for i in range(0,8):
            if matr[1 + posX[i]][4 + posY[i]] == matr[1][4]:
                num += 1
            if matr[4 + posX[i]][1 + posY[i]] == matr[4][1]:
                num += 1
            if matr[4 + posX[i]][4 + posY[i]] == matr[4][4]:
                num += 1
            if matr[4 + posX[i]][7 + posY[i]] == matr[4][7]:
                num += 1
            if matr[7 + posX[i]][4 + posY[i]] == matr[7][4]:
                num += 1
            if matr[10 + posX[i]][4 + posY[i]] == matr[10][4]:
                num += 1
        return num

    # Calculate the full fitness
    def fitnessCalc(self, cube):
        ctrl = ControllerRubikCube(cube)
      
        matr = cube.returnMatrix()
        num = self.fitStateCube(matr)

        self.__fitness = num / 54
        
        for i in range(0, self.__numMoves):
            ctrl.moveFace(self.__moves[i])
            
            cubeM = ctrl.returnCube()
            matr = cubeM.returnMatrix()
            num = self.fitStateCube(matr)

            if(self.__fitness < num/54):
                self.__fitness = num/54
                self.__posFitMax = i
        

    def mutation(self, number):
        for i in range(0, number):
            self.__moves[random.randint(0,self.__numMoves-1)] = random.randint(0,11)

    def returnMoves(self):
        return self.__moves

    def returnFitness(self):
        return self.__fitness

    def returnPosFitMax(self):
        return self.__posFitMax

    def returnMatrix(self):
        return self.returnMatrix()

    def __repr__(self):
        return str(self.__moves) + " " + str(self.__fitness)
   


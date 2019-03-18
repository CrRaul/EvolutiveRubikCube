import numpy

#                                          |             
#       1 1 1                          1 1 7
#       2 2 2                          2 2 8
#       3 3 3                          3 3 9
# 1 1 1 2 2 2 3 3 3    pos = 5   1 1 1 2 2 1 3 3 3
# 1 1 1 2 2 2 3 3 3    ======>   1 1 1 2 2 2 3 3 3
# 1 1 1 2 2 2 3 3 3              1 1 1 2 2 3 3 3 3
#       4 4 4                          4 4 2
#       5 5 5                          5 5 2 
#       6 6 6                          6 6 2
#       7 7 7                          7 7 4
#       8 8 8                          8 8 5
#       9 9 9                          9 9 6 
def rotateMiddleLongPartClock(matr, pos):
    for i in range(9,12):
        matr[i-9][6] = matr[i][pos]
    for i in range(11,2,-1):
        matr[i][pos] = matr[i-3][pos]
    for i in range(0,3):
        matr[i][pos] = matr[i][6]
    return matr


def rotateMiddleLongPartClockInverse(matr, pos):
    for i in range(0,3):
        matr[i][6] = matr[i][pos]
    for i in range(0,9):
        matr[i][pos] = matr[i+3][pos]
    for i in range(9,12):
        matr[i][pos] = matr[i-9][6]
    return matr

# ----------------------------------------------------------

#       1 1 1                          1 1 1
#       2 2 2                          2 2 2
#       3 3 3                          3 3 3
# 7 9 8 4 5 6 7 8 9    pos = 3   4 5 6 7 8 9 1 2 3   <====
# 1 1 1 2 2 2 3 3 3    ======>   1 1 1 2 2 2 3 3 3
# 1 1 1 2 2 2 3 3 3              1 1 1 2 2 2 3 3 3
#       4 4 4                          4 4 4
#       5 5 5                          5 5 5 
#       6 6 6                          6 6 6
#       7 7 7                          7 7 7
#       8 8 8                          8 8 8
#       3 2 1                          8 9 7
def rotateMiddleShortPartClock(matr, pos):
    for i in range(0,3):
        matr[2][i] = matr[pos][i]
    for i in range(0,6):
        matr[pos][i] = matr[pos][i+3]
    for i in range(0,3):
        matr[pos][8-i] = matr[14-pos][i+3]
        matr[14-pos][i+3] = matr[2][2-i]
    return matr


#          1 1 1                          1 1 1
#          2 2 2                          2 2 2
#          3 3 3                          3 3 3
# => 7 9 8 4 5 6 7 8 9    pos = 3   1 2 3 7 9 8 4 5 6   
#    1 1 1 2 2 2 3 3 3    ======>   1 1 1 2 2 2 3 3 3
#    1 1 1 2 2 2 3 3 3              1 1 1 2 2 2 3 3 3
#          4 4 4                          4 4 4
#          5 5 5                          5 5 5 
#          6 6 6                          6 6 6
#          7 7 7                          7 7 7
#          8 8 8                          8 8 8
#          3 2 1                          9 8 7
def rotateMiddleShortPartClockInverse(matr, pos):
    for i in range(0,3):
        matr[2][i] = matr[pos][i+6]
    for i in range(8,2,-1):
        matr[pos][i] = matr[pos][i-3]
    for i in range(0,3):
        matr[pos][i] = matr[14-pos][5-i]
    for i in range(0,3):
        matr[14-pos][i+3] = matr[2][2-i]
    return matr

# ----------------------------------------------------------

def rotate3x3FaceClock(matr, line, col):
    face = numpy.zeros(shape=(3,3))
    for i in range(0,3):
        for j in range(0,3):
            face[i][j] = matr[line+i][col+j]
    face = numpy.rot90(face,3)
    for i in range(0,3):
        for j in range(0,3):
            matr[line+i][col+j] = face[i][j]
    return matr


def rotate3x3FaceClockInverse(matr, line, col):
    face = numpy.zeros(shape=(3,3))
    for i in range(0,3):
        for j in range(0,3):
            face[i][j] = matr[line+i][col+j]
    face = numpy.rot90(face)
    for i in range(0,3):
        for j in range(0,3):
            matr[line+i][col+j] = face[i][j]
    return matr


#########################################################################################################

class RubikCube():
    def __init__(self):
        self.__cube = numpy.zeros(shape=(12,9))
    
    # Desc:     fill the matrix with value of solved rubik cube
    # In:       --
    # Out:      --
    def initColor(self):
        for i in range(0,12):
            for j in range(3,6):
                if(i<=2):
                    self.__cube[i][j] = 1
                elif(i<=5):
                    self.__cube[i][j] = 2
                elif(i<=8):
                    self.__cube[i][j] = 3
                else:
                    self.__cube[i][j] = 4
        
        for i in range(3,6):
            for j in range(0,3):
                self.__cube[i][j] = 5
                self.__cube[i][j+6] = 6    

    # Desc: return the matrix of rubik cube
    def returnMatrix(self):
        return self.__cube

    # Desc: verify if two cube is equal( same matrix)
    def __eq__(self, value):
        cubeP = value.returnCube()
        for i in range(0,12):
            for j in range(3,6):
                if self.__cube[i][j] != cubeP[i][j]:
                    return False
        for i in range(3,6):
            for j in range(0,3):
                if (self.__cube[i][j] != cubeP[i][j]) or (self.__cube[i][j+6] != cubeP[i][j+6]):
                    return False
        return True

    def __str__(self):
        return self.__cube
    def __repr__(self):
        return self.__cube

#########################################################################################################

    def rotateFront(self):
        self.__cube = rotateMiddleShortPartClock(self.__cube,5)
        self.__cube = rotate3x3FaceClockInverse(self.__cube, 6,3)

    def rotateFrontInverse(self):
        self.__cube = rotateMiddleShortPartClockInverse(self.__cube,5)
        self.__cube = rotate3x3FaceClock(self.__cube,6,3)

    def rotateRight(self):
        self.__cube = rotateMiddleLongPartClock(self.__cube,5)
        self.__cube = rotate3x3FaceClockInverse(self.__cube,3,6)
    
    def rotateRightInverse(self):
        self.__cube = rotateMiddleLongPartClockInverse(self.__cube,5)
        self.__cube = rotate3x3FaceClock(self.__cube,3,6)

    def rotateLeft(self):
        self.__cube = rotateMiddleLongPartClockInverse(self.__cube,3)
        self.__cube = rotate3x3FaceClockInverse(self.__cube,3,0)
    
    def rotateLeftInverse(self):
        self.__cube = rotateMiddleLongPartClock(self.__cube,3)
        self.__cube = rotate3x3FaceClock(self.__cube,3,0)
    
    def rotateBack(self):
        self.__cube = rotateMiddleShortPartClockInverse(self.__cube,3)
        self.__cube = rotate3x3FaceClockInverse(self.__cube,0,3)
    
    def rotateBackInverse(self):
        self.__cube = rotateMiddleShortPartClock(self.__cube,3)
        self.__cube = rotate3x3FaceClock(self.__cube,0,3)
    
    def rotateUp(self):
        for i in range(0,3):
            self.__cube[0][i] = self.__cube[0][i+3]

        for i in range(0,3):
            self.__cube[0][i+3] = self.__cube[5-i][0] 
        for i in range(0,3):
            self.__cube[5-i][0] = self.__cube[8][5-i]
        for i in range(0,3):
            self.__cube[8][5-i] = self.__cube[i+3][8]
        for i in range(0,3):
            self.__cube[i+3][8] = self.__cube[0][i]

        self.__cube = rotate3x3FaceClockInverse(self.__cube,9,3)
    
    def rotateUpInverse(self):
        for i in range(0,3):
            self.__cube[0][i] = self.__cube[0][i+3]

        for i in range(0,3):
            self.__cube[0][i+3] = self.__cube[i+3][8]
        for i in range(0,3):
            self.__cube[i+3][8] = self.__cube[8][5-i]
        for i in range(0,3):
            self.__cube[8][5-i] = self.__cube[5-i][0]
        for i in range(0,3):
            self.__cube[5-i][0] = self.__cube[0][i]

        self.__cube = rotate3x3FaceClock(self.__cube,9,3)
    
    def rotateDown(self):
        for i in range(0,3):
            self.__cube[2][i] = self.__cube[2][i+3]

        for i in range(0,3):
            self.__cube[2][i+3] = self.__cube[i+3][6]
        for i in range(0,3):
            self.__cube[i+3][6] = self.__cube[6][5-i]
        for i in range(0,3):
            self.__cube[6][5-i] = self.__cube[5-i][2]
        for i in range(0,3):
            self.__cube[5-i][2] = self.__cube[2][i]

        self.__cube = rotate3x3FaceClockInverse(self.__cube,3,3)
    
    def rotateDownInverse(self):
        for i in range(0,3):
            self.__cube[2][i] = self.__cube[2][i+3]

        for i in range(0,3):
            self.__cube[2][i+3] = self.__cube[5-i][2]
        for i in range(0,3):
            self.__cube[5-i][2] = self.__cube[6][5-i]
        for i in range(0,3):
            self.__cube[6][5-i] = self.__cube[i+3][6]
        for i in range(0,3):
            self.__cube[i+3][6] = self.__cube[2][i]

        self.__cube = rotate3x3FaceClock(self.__cube,3,3)

#########################################################################################################
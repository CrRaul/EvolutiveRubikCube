from RubikCube import RubikCube


class ControllerRubikCube():
    def __init__(self, cube):
        self.__cube = cube

    def initCube(self):
        self.__cube.initColor()

    def returnCube(self):
        return self.__cube

    def moveFace(self, chose):
        if chose == 0:
            self.__cube.rotateFront()
        if chose == 1:
            self.__cube.rotateFrontInverse()
        if chose == 2:
            self.__cube.rotateRight()
        if chose == 3:
            self.__cube.rotateRightInverse()
        if chose == 4:
            self.__cube.rotateBack()
        if chose == 5:
            self.__cube.rotateBackInverse()
        if chose == 6:
            self.__cube.rotateLeft()
        if chose == 7:
            self.__cube.rotateLeftInverse()
        if chose == 8:
            self.__cube.rotateUp()
        if chose == 9:
            self.__cube.rotateUpInverse()
        if chose == 10:
            self.__cube.rotateDown()
        if chose == 11:
            self.__cube.rotateDownInverse()
    

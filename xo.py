class Token:
    def __init__(self, x=0, y=0):
        self._number = 0
        self._posX = x
        self._posY = y

    def getPos(self):
        return ((self._posX, self._posY))

    def setPos(self, x, y):
        self._posX = x
        self._posY = y

    def __str__(self):
        return f'{self._posX}, and {self._posY}'
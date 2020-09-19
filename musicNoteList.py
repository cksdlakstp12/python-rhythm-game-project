class Note:
    def __init__(self, x_pos, y_pos):
        self.__x_pos = x_pos
        self.__y_pos = y_pos

    def getXPos(self):
        return self.__x_pos

    def plusYPos(self, y_pos):
        self.__y_pos += y_pos
    
    def getYPos(self):
        return self.__y_pos

tmp_note_list = [
    3, 7, 10, 13, 16, 18, 20, 23, 25
]
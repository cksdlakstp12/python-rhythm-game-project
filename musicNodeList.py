import time


class Node:
    def __init__(self, x_pos, y_pos):
        self.__x_pos = x_pos
        self.__y_pos = y_pos

    def getXPos(self):
        return self.__x_pos

    def plusYPos(self, y_pos):
        self.__y_pos += y_pos
    
    def getYPos(self):
        return self.__y_pos

    
def delay(delay_time):
    return time.sleep(delay_time)


tmp_node_list = [
    delay(0), delay(3), delay(3), delay(3), delay(3), delay(5), delay(5), delay(5), delay(5), delay(5), delay(5)
]
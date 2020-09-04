import pygame as P

class Sound:
    def __init__(self, name, music_path):
        self.__name = name
        self.__music_path = music_path

    def getName(self):
        return self.__name

    def getMusicPath(self):
        return self.__music_path

class Music(Sound):
    def __init__(self, name, music_path, music_type, score, node_list):
        super().__init__(name, music_path)
        self.__music_type = music_type
        self.__score = score
        self.__node_list = node_list
 
    def getMusicType(self):
        return self.__music_type

    def getScore(self):
        return self.__score
    
    def getNodeList(self):
        return self.__node_list

class SoundList:
    def __init__(self):
        Rain_PualKim = Music("비 - 폴킴", "./sounds/비.wav", "비, 구름", 0, [])
        Snowman_JungSeungHwan = Music("눈사람 - 정승환", "./sounds/눈사람.wav", "눈", 0, [])
        SummerFlower_YoonDdanDdan = Music("여름꽃 - 윤딴딴", "./sounds/여름꽃.wav", "맑음", 0, [])

        self.__music_list = [Rain_PualKim, Snowman_JungSeungHwan, SummerFlower_YoonDdanDdan]

    def getMusiclist(self):
        return self.__music_list


soundList = SoundList()
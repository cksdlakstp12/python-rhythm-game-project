import pygame as P
import pandas as pd
import os

accuracy_correction = 13 # second * 10 단위

data = pd.read_excel("DataBase.xlsx")

data_name = data[:]["name"]
data_file_name = data[:]["file_name"]
data_cover_img_name = data[:]["cover_img_name"]
data_type_name = data[:]["type_name"]
data_best_score = data[:]["best_score"]
data_note_list = data[:]["note_list"]

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

class Sound:
    def __init__(self, name, music_path):
        self.__name = name
        self.__music_path = music_path

    def getName(self):
        return self.__name

    def getMusicPath(self):
        return self.__music_path

class Music(Sound):
    def __init__(self, name, music_path, cover_image, music_type, score, note_list):
        super().__init__(name, music_path)
        self.__music_type = music_type
        self.__cover_image = cover_image
        self.__score = score
        if note_list != "*":
            note_list = note_list.split(',')
            tmp_note_list = [(int(t) - accuracy_correction) for t in note_list if (int(t) - accuracy_correction) > 0]
            self.__note_list = tmp_note_list
        else: self.__note_list = note_list
 
    def getMusicType(self):
        return self.__music_type

    def getCoverImage(self):
        return self.__cover_image

    def getScore(self):
        return self.__score
    
    def getNoteList(self):
        return self.__note_list

class SoundList:
    def __init__(self):
        music_list = []

        for name, file_name, cover_img_name, type_name, best_score, note_list in zip(data_name, data_file_name, data_cover_img_name, data_type_name, data_best_score, data_note_list):
            music_list.append(Music(name, file_name, cover_img_name, type_name, best_score, note_list))
                
        self.__music_list = music_list

    def getMusiclist(self):
        return self.__music_list
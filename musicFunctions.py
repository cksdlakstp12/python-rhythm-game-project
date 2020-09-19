import pygame as P
import pandas as pd
import os, musicNoteList

data = pd.read_excel("DataBase.xlsx")

data_name = data[:]["name"]
data_file_name = data[:]["file_name"]
data_cover_img_name = data[:]["cover_img_name"]
data_type_name = data[:]["type_name"]
data_best_score = data[:]["best_score"]


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
        self.__note_list = note_list
 
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

        for name, file_name, cover_img_name, type_name, best_score in zip(data_name, data_file_name, data_cover_img_name, data_type_name, data_best_score):
            music_list.append(Music(name, file_name, cover_img_name, type_name, best_score, musicNoteList.tmp_note_list))
                
        self.__music_list = music_list

    def getMusiclist(self):
        return self.__music_list
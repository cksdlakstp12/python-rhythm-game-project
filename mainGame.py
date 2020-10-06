import pygame as P
import pandas as pd
import os, sys, musicFunctions, time, requests, random, musicNoteList, inputTextFunctions
from bs4 import BeautifulSoup

#####################################################################
# 기본 초기화 (반드시 해야하는 것들)

P.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 1080 # 가로 크기
screen_height = 720 # 세로 크기
screen = P.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
P.display.set_caption("2019102216 이찬")

# FPS
clock = P.time.Clock()

#####################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "img")
music_path = os.path.join(current_path, "sounds")
font_path = os.path.join(current_path, "font")

font_path = os.path.join(font_path, "FivoSans-Black-Oblique.otf")

title_font = P.font.Font(font_path, 80)
btn_font = P.font.Font(font_path, 60)
music_font = P.font.Font(font_path, 50)
default_font = P.font.Font(font_path, 32)
in_game_font = P.font.Font(font_path, 20)

background = P.image.load(os.path.join(image_path, "background.jpg")) 
background.set_alpha(100)
default_background = P.image.load(os.path.join(image_path, "default_background.png")) 

btn_click_sound = P.mixer.Sound(os.path.join(music_path, "other_btn.wav"))
btn_click_sound.set_volume(0.5)
select_music_sound = P.mixer.Sound(os.path.join(music_path, "game_start.wav"))
select_music_sound.set_volume(0.5)
music_volume = 1.0


# weather data crawling (맑음, 구름, 비, 눈, 흐림)
html = requests.get('https://search.naver.com/search.naver?query=날씨')
soup = BeautifulSoup(html.text, 'html.parser')
data = soup.find("div", {'class':'weather_box'})
weatherData = data.find('p', {'class':'cast_txt'}).text


# option window png files
option_window = P.image.load(os.path.join(image_path, "option_window.png"))
option_window_size = option_window.get_rect().size
option_window_width = option_window_size[0]
option_window_height = option_window_size[1]

volume_plus_btn = P.image.load(os.path.join(image_path, "volume_plus_btn.png"))
volume_plus_btn_size = volume_plus_btn.get_rect().size
volume_plus_btn_width = volume_plus_btn_size[0]
volume_plus_btn_height = volume_plus_btn_size[1]

volume_minus_btn = P.image.load(os.path.join(image_path, "volume_minus_btn.png"))
volume_minus_btn_size = volume_minus_btn.get_rect().size
volume_minus_btn_width = volume_minus_btn_size[0]
volume_minus_btn_height = volume_minus_btn_size[1]

cancel_btn = P.image.load(os.path.join(image_path, "btn.png"))
cancel_btn_size = cancel_btn.get_rect().size
cancel_btn_width = cancel_btn_size[0]
cancel_btn_height = cancel_btn_size[1]


# start menu png files
game_start_btn = P.image.load(os.path.join(image_path, "btn.png"))
game_start_btn_size = game_start_btn.get_rect().size
game_start_btn_width = game_start_btn_size[0]
game_start_btn_height = game_start_btn_size[1]

option_btn = P.image.load(os.path.join(image_path, "btn.png"))
option_btn_size = option_btn.get_rect().size
option_btn_width = option_btn_size[0]
option_btn_height = option_btn_size[1]

music_add_btn = P.image.load(os.path.join(image_path, "btn.png"))
music_add_btn_size = music_add_btn.get_rect().size
music_add_btn_width = music_add_btn_size[0]
music_add_btn_height = music_add_btn_size[1]

game_quit_btn = P.image.load(os.path.join(image_path, "btn.png"))
game_quit_btn_size = game_quit_btn.get_rect().size
game_quit_btn_width = game_quit_btn_size[0]
game_quit_btn_height = game_quit_btn_size[1]


# select music menu png files
back_arrow_btn = P.image.load(os.path.join(image_path, "back_arrow.png"))
back_arrow_btn_size = back_arrow_btn.get_rect().size
back_arrow_btn_width = back_arrow_btn_size[0]
back_arrow_btn_height = back_arrow_btn_size[1]

right_arrow_btn = P.image.load(os.path.join(image_path, "right_arrow.png"))
right_arrow_btn_size = right_arrow_btn.get_rect().size
right_arrow_btn_width = right_arrow_btn_size[0]
right_arrow_btn_height = right_arrow_btn_size[1]

left_arrow_btn = P.image.load(os.path.join(image_path, "left_arrow.png"))
left_arrow_btn_size = left_arrow_btn.get_rect().size
left_arrow_btn_width = left_arrow_btn_size[0]
left_arrow_btn_height = left_arrow_btn_size[1]

select_music_btn = P.image.load(os.path.join(image_path, "btn.png"))
select_music_btn_size = select_music_btn.get_rect().size
select_music_btn_width = select_music_btn_size[0]
select_music_btn_height = select_music_btn_size[1]


# in game option window
game_continue_btn = P.image.load(os.path.join(image_path, "btn.png"))
game_continue_btn_size = game_continue_btn.get_rect().size
game_continue_btn_width = game_continue_btn_size[0]
game_continue_btn_height = game_continue_btn_size[1]

in_game_option_btn = P.image.load(os.path.join(image_path, "btn.png"))
in_game_option_btn_size = in_game_option_btn.get_rect().size
in_game_option_btn_width = in_game_option_btn_size[0]
in_game_option_btn_height = in_game_option_btn_size[1]

game_restart_btn = P.image.load(os.path.join(image_path, "btn.png"))
game_restart_btn_size = game_restart_btn.get_rect().size
game_restart_btn_width = game_restart_btn_size[0]
game_restart_btn_height = game_restart_btn_size[1]

in_game_quit_btn = P.image.load(os.path.join(image_path, "btn.png"))
in_game_quit_btn_size = in_game_quit_btn.get_rect().size
in_game_quit_btn_width = in_game_quit_btn_size[0]
in_game_quit_btn_height = in_game_quit_btn_size[1]

option_btn_icon = P.image.load(os.path.join(image_path, "option_btn_icon.png"))
option_btn_icon_size = option_btn_icon.get_rect().size
option_btn_icon_width = option_btn_icon_size[0]
option_btn_icon_height = option_btn_icon_size[1]


# result game page files
restart_btn = P.image.load(os.path.join(image_path, "btn.png"))
restart_btn_size = restart_btn.get_rect().size
restart_btn_width = restart_btn_size[0]
restart_btn_height = restart_btn_size[1]

quit_game_btn = P.image.load(os.path.join(image_path, "btn.png"))
quit_game_btn_size = quit_game_btn.get_rect().size
quit_game_btn_width = quit_game_btn_size[0]
quit_game_btn_height = quit_game_btn_size[1]


# start game page files
note1 = P.image.load(os.path.join(image_path, "note.png"))
note2 = P.image.load(os.path.join(image_path, "note.png"))
note3 = P.image.load(os.path.join(image_path, "note.png"))
note4 = P.image.load(os.path.join(image_path, "note.png"))
note_size = note1.get_rect().size
note_height = note_size[1]
note_width = note_size[0]
notes = [note1, note2, note3, note4]

hit_effect = P.image.load(os.path.join(image_path, "hit_effect.png"))
hit_effect_size = hit_effect.get_rect().size
hit_effect_width = hit_effect_size[0]

ingame_line = P.image.load(os.path.join(image_path, "ingame_line.png"))
ingame_line_size = ingame_line.get_rect().size
ingame_line_width = ingame_line_size[0]

hit_note = P.image.load(os.path.join(image_path, "hit_note.png"))
hit_note_size = hit_note.get_rect().size
hit_note_width = hit_note_size[0]
hit_note_height = hit_note_size[1]

note_hit_chk = [False, False, False, False]

fade_img = P.image.load(os.path.join(image_path, "fade_img.png"))

total_time = 3

#####################################################################


def fade_out_img():
    for x in range(0, 255):
        fade_img.set_alpha(x)
        screen.blit(fade_img, (0, 0))
        P.display.update()


def btn_img_txt(text, height):
    btn_img = P.image.load(os.path.join(image_path, "btn.png"))
    btn = text
    btn_msg = default_font.render(btn, True, (255, 255, 255))
    btn_msg_rect = btn_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 + height)))

    screen.blit(btn_img, (screen_width/2, screen_height / 2 + height))    
    screen.blit(btn_msg, btn_msg_rect)


def count_down(start_ticks):
    elapsed_time = (P.time.get_ticks() - start_ticks) / 1000
    timer = default_font.render(str(int(total_time - elapsed_time + 1)), True, (255, 255, 255))
    if total_time - elapsed_time > 0: return timer


def option_window_open():
    global music_volume
    
    settings_title = "SETTINGS"
    settings_title_msg = title_font.render(settings_title, True, (0, 0, 0))
    settings_title_msg_rect = settings_title_msg.get_rect(center=(int((screen_width)/2), int((screen_height)/2 - 150)))

    music_volume_title = "Music Volume"
    music_volume_title_msg = default_font.render(music_volume_title, True, (0, 0, 0))
    music_volume_title_msg_rect = music_volume_title_msg.get_rect(center=(int((screen_width)/2), int((screen_height)/2 - 20)))

    cancel = "CANCEL"
    cancel_msg = btn_font.render(cancel, True, (0, 0, 0))
    cancel_msg_rect = cancel_msg.get_rect(center=(int((screen_width)/2), int((screen_height)/2 + 175)))

    volume_line_cnt = 0

    cancel = False

    option_window_rect = option_window.get_rect()
    option_window_rect.left = (screen_width - option_window_width)/2
    option_window_rect.top = (screen_height - option_window_height)/2

    
    volume_plus_btn_rect = volume_plus_btn.get_rect()
    volume_plus_btn_rect.left = (screen_width - volume_plus_btn_width) / 2 + 275
    volume_plus_btn_rect.top = (screen_height  - volume_plus_btn_height) / 2 + 60

    volume_minus_btn_rect = volume_minus_btn.get_rect()
    volume_minus_btn_rect.left = (screen_width - volume_minus_btn_width) / 2 - 275
    volume_minus_btn_rect.top = (screen_height - volume_minus_btn_height) / 2 + 60

    cancel_btn_rect = cancel_btn.get_rect()
    cancel_btn_rect.left = (screen_width - cancel_btn_width) / 2
    cancel_btn_rect.top = (screen_height - cancel_btn_height) / 2 + 175
    
    clicked_btn = []
    option_window_btn_list = [volume_plus_btn_rect, volume_minus_btn_rect, cancel_btn_rect]

    while not cancel:
        music_volume = P.mixer.music.get_volume()
        volume_line_cnt = int(round((music_volume * 10)))

        for event in P.event.get():
            if event.type == P.QUIT:
                cancel = True
            
            elif event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in option_window_btn_list if b.collidepoint(pos)]


        if volume_plus_btn_rect in clicked_btn:
            btn_click_sound.play()
            if music_volume < 1.0:
                music_volume += 0.1
                P.mixer.music.set_volume(music_volume)
            clicked_btn = []

        elif volume_minus_btn_rect in clicked_btn:
            btn_click_sound.play()
            if music_volume > 0.0:
                music_volume -= 0.1
                P.mixer.music.set_volume(music_volume)
            clicked_btn = []

        elif cancel_btn_rect in clicked_btn:
            btn_click_sound.play()
            return

        screen.blit(option_window, ((screen_width - option_window_width)/2, (screen_height - option_window_height)/2))
        screen.blit(music_volume_title_msg, music_volume_title_msg_rect)
        screen.blit(volume_plus_btn, ((screen_width- volume_plus_btn_width) / 2 + 275, (screen_height - volume_plus_btn_height) / 2 + 60))
        screen.blit(volume_minus_btn, ((screen_width - volume_minus_btn_width) / 2 - 275, (screen_height - volume_minus_btn_height) / 2 + 60))
        for space in range(0, volume_line_cnt): P.draw.rect(screen, (134, 240, 134), [((screen_width- volume_plus_btn_width) / 2 + volume_plus_btn_width - 250 + space * 46), ((screen_height - volume_plus_btn_height) / 2 + 60), 40, 50])
        screen.blit(cancel_btn, ((screen_width - cancel_btn_width) / 2, (screen_height - cancel_btn_height) / 2 + 175))
        screen.blit(settings_title_msg, settings_title_msg_rect)
        screen.blit(cancel_msg, cancel_msg_rect)

        P.display.update()

    P.quit()


def in_game_option_window_open():
    option_window_resize = P.transform.scale(option_window, (957, 680))
    option_window_resize_size = option_window_resize.get_rect().size
    option_window_resize_width = option_window_resize_size[0]
    option_window_resize_height = option_window_resize_size[1]

    game_continue_btn_rect = game_continue_btn.get_rect()
    game_continue_btn_rect.left = (screen_width - game_continue_btn_width)/2
    game_continue_btn_rect.top = (screen_height - game_continue_btn_height)/2 - 250

    in_game_option_btn_rect = in_game_option_btn.get_rect()
    in_game_option_btn_rect.left = (screen_width - in_game_option_btn_width)/2
    in_game_option_btn_rect.top = (screen_height - in_game_option_btn_height)/2 - 100

    game_restart_btn_rect = game_restart_btn.get_rect()
    game_restart_btn_rect.left = (screen_width - game_restart_btn_width)/2
    game_restart_btn_rect.top = (screen_height - game_restart_btn_height)/2 + 100

    in_game_quit_btn_rect = in_game_quit_btn.get_rect()
    in_game_quit_btn_rect.left = (screen_width - in_game_quit_btn_width)/2
    in_game_quit_btn_rect.top = (screen_height - in_game_quit_btn_height)/2 + 250
    
    in_game_continue = "Continue"
    in_game_continue_msg = default_font.render(in_game_continue, True, (255, 255, 255))
    in_game_continue_msg_rect = in_game_continue_msg.get_rect(center=(int(screen_width/2), int((screen_height - game_continue_btn_height)/2 - 200)))

    in_game_settings = "Settings"
    in_game_settings_msg = default_font.render(in_game_settings, True, (255, 255, 255))
    in_game_settings_msg_rect = in_game_settings_msg.get_rect(center=(int(screen_width/2), int((screen_height - game_restart_btn_height)/2 - 50)))

    in_game_start = "Game Restart"
    in_game_start_msg = default_font.render(in_game_start, True, (255, 255, 255))
    in_game_start_msg_rect = in_game_start_msg.get_rect(center=(int(screen_width/2), int((screen_height - in_game_option_btn_height)/2 +150)))

    in_game_quit = "Game Quit"
    in_game_quit_msg = default_font.render(in_game_quit, True, (255, 255, 255))
    in_game_quit_msg_rect = in_game_quit_msg.get_rect(center=(int(screen_width/2), int((screen_height - in_game_quit_btn_height)/2 + 300)))

    cancel = False

    clicked_btn = []
    option_window_btn_list = [game_continue_btn_rect, in_game_option_btn_rect, game_restart_btn_rect, in_game_quit_btn_rect]

    while not cancel:

        for event in P.event.get():
            if event.type == P.QUIT:
                cancel = True

            elif event.type == P.KEYDOWN:
                if event.key == P.K_ESCAPE: clicked_btn = [game_continue_btn_rect]
            
            elif event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in option_window_btn_list if b.collidepoint(pos)]
        

        if game_continue_btn_rect in clicked_btn:
            print("게임 진행")
            btn_click_sound.play()
            return "continue"

        elif in_game_option_btn_rect in clicked_btn:
            print("옵션 실행")
            btn_click_sound.play()
            option_window_open()
            clicked_btn = []

        elif game_restart_btn_rect in clicked_btn:
            print("게임 재시작")
            btn_click_sound.play()
            return "restart"

        elif in_game_quit_btn_rect in clicked_btn:
            print("게임 종료")
            btn_click_sound.play()
            return "quit"

        screen.blit(option_window_resize, ((screen_width - option_window_resize_width) / 2, (screen_height - option_window_resize_height) / 2))
        screen.blit(game_continue_btn, ((screen_width - game_continue_btn_width)/2, (screen_height - game_continue_btn_height)/2 - 250))
        screen.blit(in_game_option_btn, ((screen_width - in_game_option_btn_width)/2, (screen_height - in_game_option_btn_height)/2 - 100))
        screen.blit(game_restart_btn, ((screen_width - game_restart_btn_width)/2, (screen_height - game_restart_btn_height)/2 + 100))
        screen.blit(in_game_quit_btn, ((screen_width - in_game_quit_btn_width)/2, (screen_height - in_game_quit_btn_height)/2 + 250))
        screen.blit(in_game_continue_msg, in_game_continue_msg_rect)
        screen.blit(in_game_start_msg, in_game_start_msg_rect)
        screen.blit(in_game_settings_msg, in_game_settings_msg_rect)
        screen.blit(in_game_quit_msg, in_game_quit_msg_rect)

        P.display.update()

    P.quit()

"""
def music_add_option_window():
    

    input_box1 = inputTextFunctions.InputBox(100, 100, 140, 32)
    input_boxes = [input_box1]
    done = False

    while not done:
        for event in P.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        P.display.update()
        
    P.quit()
"""

def start_menu():
    global music_volume

    game_title = "Lee Chan's Rhythm Game"
    game_title_msg = title_font.render(game_title, True, (255, 255, 255))
    game_title_msg_rect = game_title_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 - 200)))

    game_start = "Game Start"
    game_start_msg = default_font.render(game_start, True, (255, 255, 255))
    game_start_msg_rect = game_start_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 - 50)))

    game_settings = "Game Settings"
    game_settings_msg = default_font.render(game_settings, True, (255, 255, 255))
    game_settings_msg_rect = game_settings_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 + 75)))

    add_music = "Add Music"
    add_music_msg = default_font.render(add_music, True, (255, 255, 255))
    add_music_msg_rect = add_music_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 + 200)))

    game_quit = "Game Quit"
    game_quit_msg = default_font.render(game_quit, True, (255, 255, 255))
    game_quit_msg_rect = game_quit_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 + 325)))

    P.mixer.music.load(os.path.join(music_path, "background_music.mp3"))
    P.mixer.music.play(-1)

    start_menu_quit_chk = False
    start_menu_select_chk = True

    game_start_btn_rect = game_start_btn.get_rect()
    game_start_btn_rect.left = (screen_width-game_start_btn_width)/2
    game_start_btn_rect.top = (screen_height - game_start_btn_height)/2 - 50

    option_btn_rect = option_btn.get_rect()
    option_btn_rect.left = (screen_width-option_btn_width)/2
    option_btn_rect.top = (screen_height - option_btn_height)/2 + 75

    music_add_btn_rect = music_add_btn.get_rect()
    music_add_btn_rect.left = (screen_width-music_add_btn_width)/2
    music_add_btn_rect.top = (screen_height - music_add_btn_height)/2 + 200

    game_quit_btn_rect = game_quit_btn.get_rect()
    game_quit_btn_rect.left = (screen_width-game_quit_btn_width)/2
    game_quit_btn_rect.top = (screen_height - game_quit_btn_height)/2 + 325
    

    clicked_btn = []
    start_menu_btn_list = [game_quit_btn_rect, game_start_btn_rect, option_btn_rect, music_add_btn_rect]


    while (not start_menu_quit_chk) and start_menu_select_chk:
        P.mixer.music.set_volume(music_volume)
                
        for event in P.event.get():
            if event.type == P.QUIT:
                start_menu_quit_chk = True
            
            elif event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in start_menu_btn_list if b.collidepoint(pos)]

            
        if game_start_btn_rect in clicked_btn:
            print("게임시작")
            btn_click_sound.play()
            select_music()
            clicked_btn = []
            P.mixer.music.load(os.path.join(music_path, "background_music.mp3"))
            P.mixer.music.play(-1)

        elif option_btn_rect in clicked_btn:
            btn_click_sound.play()
            option_window_open()
            clicked_btn = []

        elif music_add_btn_rect in clicked_btn:
            btn_click_sound.play()
            music_add_option_window()
            clicked_btn = []

        elif game_quit_btn_rect in clicked_btn: 
            btn_click_sound.play()
            print("종료 버튼 클릭")
            start_menu_select_chk = False
            
        
        screen.blit(background, (0, 0))
        screen.blit(game_title_msg, game_title_msg_rect)
        screen.blit(game_start_btn, ((screen_width-game_start_btn_width)/2, (screen_height - game_start_btn_height)/2 - 50))
        screen.blit(option_btn, ((screen_width-option_btn_width)/2, (screen_height - option_btn_height)/2 + 75))
        screen.blit(music_add_btn, ((screen_width - music_add_btn_width)/2, (screen_height - music_add_btn_height)/2 + 200))
        screen.blit(game_quit_btn, ((screen_width-game_quit_btn_width)/2, (screen_height - game_quit_btn_height)/2 + 325))
        screen.blit(game_start_msg, game_start_msg_rect)
        screen.blit(game_settings_msg, game_settings_msg_rect)
        screen.blit(add_music_msg, add_music_msg_rect)
        screen.blit(game_quit_msg, game_quit_msg_rect)

        P.display.update()

    P.quit()
    

def select_music():
    select_music_quit_chk = True

    game_start = "START!"
    game_start_msg = default_font.render(game_start, True, (255, 255, 255))
    game_start_msg_rect = game_start_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 + 300)))

    back_arrow_btn_rect = back_arrow_btn.get_rect()
    back_arrow_btn_rect.left = 10
    back_arrow_btn_rect.top = 10
    
    left_arrow_btn_rect = left_arrow_btn.get_rect() 
    left_arrow_btn_rect.left = left_arrow_btn_width
    left_arrow_btn_rect.top = (screen_height - left_arrow_btn_height) / 2

    right_arrow_btn_rect = right_arrow_btn.get_rect()    
    right_arrow_btn_rect.left = screen_width - right_arrow_btn_width * 2
    right_arrow_btn_rect.top = (screen_height - right_arrow_btn_height) / 2

    select_music_btn_rect = select_music_btn.get_rect()
    select_music_btn_rect.left = (screen_width - select_music_btn_width)/2
    select_music_btn_rect.top = (screen_height - select_music_btn_height)/2 + 300

    clicked_btn = []
    start_menu_btn_list = [back_arrow_btn_rect, left_arrow_btn_rect, right_arrow_btn_rect, select_music_btn_rect]

    soundList = musicFunctions.SoundList().getMusiclist()

    music_list_idx_chk = 0

    music_play_chk = True

    for music in soundList:
        if music.getMusicType() in weatherData:
            soundList.insert(0, music)
            break

    while select_music_quit_chk:
        P.mixer.music.set_volume(music_volume)

        for event in P.event.get():
            if event.type == P.QUIT:
                select_music_quit_chk = False
            
            elif event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in start_menu_btn_list if b.collidepoint(pos)]

        if back_arrow_btn_rect in clicked_btn:
            btn_click_sound.play()
            del soundList[0]
            return

        elif left_arrow_btn_rect in clicked_btn:
            btn_click_sound.play()
            
            if music_list_idx_chk > 0:
                music_list_idx_chk -= 1

            music_play_chk = True
            clicked_btn = []
        
        elif right_arrow_btn_rect in clicked_btn:
            btn_click_sound.play()

            if music_list_idx_chk < (len(soundList) - 1):
                music_list_idx_chk += 1

            music_play_chk = True
            clicked_btn = []
        
        elif select_music_btn_rect in clicked_btn:

            select_music_sound.play()
            P.mixer.music.stop()

            while 1:
                fade_out_img()
                
                tmp = start_game(music_list_idx_chk, soundList)
                
                if tmp == "quit": break

            del soundList[0]
            
            for music in soundList:
                if music.getMusicType() in weatherData:
                    soundList.insert(0, music)
                    break

            fade_out_img()

            P.mixer.music.play(-1)

            clicked_btn = []


        for chk in range(0, len(soundList)):
            if music_play_chk and music_list_idx_chk == chk:
                P.mixer.stop()
                P.mixer.music.load(os.path.join(music_path, soundList[chk].getMusicPath()))
                P.mixer.music.play() 
                music_play_chk = False
    
            
        screen.blit(background, (0, 0))


        if music_list_idx_chk == 0:
            first_img = P.image.load(os.path.join(image_path, soundList[music_list_idx_chk].getCoverImage()))
            first_img_size = first_img.get_rect().size
            first_img_width = first_img_size[0]
            first_img_height = first_img_size[1]
            second_img = P.image.load(os.path.join(image_path, soundList[music_list_idx_chk + 1].getCoverImage()))
            second_img_size = second_img.get_rect().size
            second_img_width = second_img_size[0]
            second_img_height = second_img_size[1]


            recomend_title = "Today's Recomend"
            recomend_title_msg = music_font.render(recomend_title, True, (0, 0, 0))
            recomend_title_msg_rect = recomend_title_msg.get_rect(center=(int((screen_width)/2), int(50)))  
            
            music_title = soundList[music_list_idx_chk].getName()
            music_title_msg = default_font.render(music_title, True, (0, 0, 0))
            music_title_msg_rect = music_title_msg.get_rect(center=(int((screen_width)/2), int(100))) 

            screen.blit(recomend_title_msg, recomend_title_msg_rect)
            screen.blit(music_title_msg, music_title_msg_rect)
            
            screen.blit(first_img, ((screen_width - first_img_width)/2, (screen_height - first_img_height)/ 2))
            screen.blit(second_img, ((screen_width - second_img_width)/2 + first_img_width + 100, (screen_height - second_img_height)/ 2))

        else:

            if music_list_idx_chk == (len(soundList) - 1):            
                first_img = P.image.load(os.path.join(image_path, soundList[music_list_idx_chk - 1].getCoverImage()))
                first_img_size = first_img.get_rect().size
                first_img_width = first_img_size[0]
                first_img_height = first_img_size[1]
                second_img = P.image.load(os.path.join(image_path, soundList[music_list_idx_chk].getCoverImage()))
                second_img_size = second_img.get_rect().size
                second_img_width = second_img_size[0]
                second_img_height = second_img_size[1]

                screen.blit(first_img, ((screen_width - first_img_width)/2 - second_img_width - 100, (screen_height - first_img_height)/ 2))
                screen.blit(second_img, ((screen_width - second_img_width)/2, (screen_height - second_img_height)/ 2))
                
            else:
                first_img = P.image.load(os.path.join(image_path, soundList[music_list_idx_chk - 1].getCoverImage()))
                first_img_size = first_img.get_rect().size
                first_img_width = first_img_size[0]
                first_img_height = first_img_size[1]
                second_img = P.image.load(os.path.join(image_path, soundList[music_list_idx_chk].getCoverImage()))
                second_img_size = second_img.get_rect().size
                second_img_width = second_img_size[0]
                second_img_height = second_img_size[1]
                third_img = P.image.load(os.path.join(image_path, soundList[music_list_idx_chk + 1].getCoverImage()))
                third_img_size = third_img.get_rect().size
                third_img_width = third_img_size[0]
                third_img_height = third_img_size[1]
                
                screen.blit(first_img, ((screen_width - first_img_width)/2 - second_img_width - 100, (screen_height - first_img_height)/ 2))
                screen.blit(second_img, ((screen_width - second_img_width)/2, (screen_height - second_img_height)/ 2))
                screen.blit(third_img, ((screen_width - third_img_width)/2 + second_img_width + 100, (screen_height - third_img_height)/ 2))

            music_title = soundList[music_list_idx_chk].getName()
            music_title_msg = music_font.render(music_title, True, (0, 0, 0))
            music_title_msg_rect = music_title_msg.get_rect(center=(int((screen_width)/2), int(50))) 

            music_score = "Score : " + str(soundList[music_list_idx_chk].getScore())
            music_score_msg = default_font.render(music_score, True, (0, 0, 0))
            music_score_msg_rect = music_score_msg.get_rect(center=(int((screen_width)/2), int(100)))  
            
            screen.blit(music_title_msg, music_title_msg_rect)
            screen.blit(music_score_msg, music_score_msg_rect)
        
        
        screen.blit(back_arrow_btn, (10, 10))
        screen.blit(left_arrow_btn, (left_arrow_btn_width, (screen_height - left_arrow_btn_height) / 2))
        screen.blit(right_arrow_btn, (screen_width - right_arrow_btn_width * 2, (screen_height - right_arrow_btn_height) / 2))
        screen.blit(select_music_btn, ((screen_width-select_music_btn_width)/2, (screen_height - select_music_btn_height)/2 + 300))
        screen.blit(game_start_msg, game_start_msg_rect)
        

        P.display.update()

    

    P.mixer.music.stop()

    P.quit()


def game_result(score, combo, music_index, soundList):
    
    background = P.image.load(os.path.join(image_path, "fade_img.png"))

    cover_img = P.image.load(os.path.join(image_path, soundList[music_index].getCoverImage()))
    cover_img_size = cover_img.get_rect().size
    cover_img_width = cover_img_size[0]
    cover_img_height = cover_img_size[1]
    
    restart = "RESTART"
    restart_msg = music_font.render(restart, True, (0, 0, 0))
    restart_msg_rect = restart_msg.get_rect(center=(screen_width / 2 - restart_btn_width / 2, screen_height - restart_btn_height + 50))

    quit_game = "QUIT"
    quit_game_msg = music_font.render(quit_game, True, (0, 0, 0))
    quit_game_msg_rect = quit_game_msg.get_rect(center=(screen_width / 2 + quit_game_btn_width / 2, screen_height - quit_game_btn_height + 50))

    restart_btn_rect = restart_btn.get_rect()
    restart_btn_rect.left = (screen_width - restart_btn_width) / 2 - restart_btn_width / 2
    restart_btn_rect.top = screen_height - restart_btn_height

    game_quit_rect = quit_game_btn.get_rect()
    game_quit_rect.left = (screen_width - quit_game_btn_width) / 2 + quit_game_btn_width / 2
    game_quit_rect.top = screen_height - quit_game_btn_height

    best_score_int = int(soundList[music_index].getScore())
    best_score_tmp = 0
    score_tmp = 0
    combo_tmp = 0

    game_result_chk = True

    clicked_btn = []
    start_menu_btn_list = [restart_btn_rect, game_quit_rect]

    best_combo_chk = len(soundList[music_index].getNoteList())

    recomend_music_chk = True

    not_recomend_music_chk = True

    recomend_music = soundList[0]

    while game_result_chk:

        dt = clock.tick(30)

        for event in P.event.get():
            if event.type == P.QUIT:
                game_result_chk = False
                
            elif event.type == P.KEYDOWN:
                if event.key == P.K_ESCAPE: clicked_btn = []

            elif event.type == P.MOUSEBUTTONDOWN:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in start_menu_btn_list if b.collidepoint(pos)]

        if restart_btn_rect in clicked_btn:
            select_music_sound.play()
            return "restart"

        elif game_quit_rect in clicked_btn: 
            btn_click_sound.play()
            return "quit"

        if score_tmp != score: score_tmp += 100
        elif best_score_tmp != best_score_int: best_score_tmp += 100
        elif combo_tmp != combo: combo_tmp += 1

        result_score = "SCORE : {}".format(score_tmp)
        result_score_msg = default_font.render(result_score, True, (0, 0, 0))
        result_score_msg_rect = result_score_msg.get_rect(center=(int(screen_width/2 +250), int(screen_height / 2 - 100)))

        result_best_score = "BEST SCORE : {}".format(best_score_tmp)
        result_best_score_msg = default_font.render(result_best_score, True, (0, 0, 0))
        result_best_score_msg_rect = result_best_score_msg.get_rect(center=(int(screen_width/2 +250), int(screen_height / 2)))

        result_combo = "COMBO : {0} / {1}".format(combo_tmp, best_combo_chk)
        result_combo_msg = default_font.render(result_combo, True, (0, 0, 0))
        result_combo_msg_rect = result_combo_msg.get_rect(center=(int(screen_width/2 + 250), int(screen_height / 2 + 100)))

        screen.blit(background, (0, 0))
        screen.blit(cover_img, (screen_width/2 - cover_img_width, (screen_height - cover_img_height) / 2))

        screen.blit(result_score_msg, result_score_msg_rect)
        screen.blit(result_best_score_msg, result_best_score_msg_rect)
        screen.blit(result_combo_msg, result_combo_msg_rect)

        screen.blit(restart_btn, ((screen_width - restart_btn_width) / 2 - restart_btn_width / 2, screen_height - restart_btn_height))
        screen.blit(quit_game_btn, ((screen_width - quit_game_btn_width) / 2 + quit_game_btn_width / 2, screen_height - quit_game_btn_height))
        screen.blit(restart_msg, restart_msg_rect)
        screen.blit(quit_game_msg, quit_game_msg_rect)

        if (score_tmp == score) and (best_score_tmp == best_score_int) and (combo_tmp == combo):

            if best_score_int < score:

                time.sleep(1)
                new_score = "NEW SCORE!!"
                new_score_msg = btn_font.render(new_score, True, (0, 0, 0))
                new_score_msg_rect = new_score_msg.get_rect(center=(int(screen_width/2 + 250), int(screen_height / 2 + 200)))

                if music_index == 0 and recomend_music_chk:
                    
                    recomend_music_idx = 0

                    for idx, sound in enumerate(soundList):
                        if idx == 0: continue
                        elif sound.getName() == recomend_music.getName():
                            recomend_music_idx = idx
                            break

                    musicFunctions.data_best_score[recomend_music_idx] = score
                    df = pd.DataFrame({"name":musicFunctions.data_name, "file_name":musicFunctions.data_file_name, 
                        "cover_img_name":musicFunctions.data_cover_img_name, "type_name":musicFunctions.data_type_name, 
                        "best_score":musicFunctions.data_best_score
                        })
                    write = pd.ExcelWriter("DataBase.xlsx", engine="xlsxwriter")
                    df.to_excel(write, sheet_name="Sheet1")
                    write.close()   

                    recomend_music_chk = False

                elif music_index != 0 and not_recomend_music_chk:
                    musicFunctions.data_best_score[music_index] = score
                    df = pd.DataFrame({"name":musicFunctions.data_name, "file_name":musicFunctions.data_file_name, 
                        "cover_img_name":musicFunctions.data_cover_img_name, "type_name":musicFunctions.data_type_name, 
                        "best_score":musicFunctions.data_best_score
                        })
                    write = pd.ExcelWriter("DataBase.xlsx", engine="xlsxwriter")
                    df.to_excel(write, sheet_name="Sheet1")
                    write.close()    

                    not_recomend_music_chk = False          

                screen.blit(new_score_msg, new_score_msg_rect)

        P.display.update()

    P.quit()


def start_game(music_index, soundList):
    background = P.image.load(os.path.join(image_path, soundList[music_index].getCoverImage()))
    background_size = background.get_rect().size
    background_height = background_size[1]

    background.set_alpha(125)
    background = P.transform.scale(background, (1080, 1080))

    option_btn_icon_rect = option_btn_icon.get_rect()
    option_btn_icon_rect.left = screen_width - option_btn_icon_width - 10
    option_btn_icon_rect.top = 10

    special_background = P.image.load(os.path.join(image_path, "special_img.jpeg"))
    
    note1_rect = notes[0].get_rect()
    note1_rect.left = (2*0 + 1) * 10 + 0 * note_width + 11
    note1_rect.top = screen_height - note_height - 5
    
    note2_rect = notes[0].get_rect()
    note2_rect.left = (2*1 + 1) * 10 + 1 * note_width + 11
    note2_rect.top = screen_height - note_height - 5
    
    note3_rect = notes[0].get_rect()
    note3_rect.left = (2*2 + 1) * 10 + 2 * note_width + 11
    note3_rect.top = screen_height - note_height - 5
    
    note4_rect = notes[0].get_rect()
    note4_rect.left = (2*3 + 1) * 10 + 3 * note_width + 11
    note4_rect.top = screen_height - note_height - 5

    perfect = "PERFECT!"
    perfect_msg = default_font.render(perfect, True, (122, 82, 182))
    perfect_msg_rect = perfect_msg.get_rect(center=(int(screen_width/2 - 110), int(screen_height / 2)))

    greate = "GREATE!"
    greate_msg = default_font.render(greate, True, (41, 123, 223))
    greate_msg_rect = greate_msg.get_rect(center=(int(screen_width/2 - 110), int(screen_height / 2)))

    nice = "NICE!"
    nice_msg = default_font.render(nice, True, (223, 84, 41))
    nice_msg_rect = nice_msg.get_rect(center=(int(screen_width/2 - 110), int(screen_height / 2)))

    good = "GOOD!"
    good_msg = default_font.render(good, True, (56, 107, 208))
    good_msg_rect = good_msg.get_rect(center=(int(screen_width/2 - 110), int(screen_height / 2)))

    bad = "BAD.."
    bad_msg = default_font.render(bad, True, (223, 84, 41))
    bad_msg_rect = bad_msg.get_rect(center=(int(screen_width/2 - 110), int(screen_height / 2)))

    perfect_chk = False
    greate_chk = False
    good_chk = False
    nice_chk = False
    bad_chk = False

    note_list = soundList[music_index].getNoteList()

    timer_chk = True

    game_started_chk = False

    music_chk = True

    start_ticks_chk = True

    tmp_time = 0
    
    clicked_btn = []

    start_menu_btn_list = [option_btn_icon_rect]

    hit_note_list = []

    start_game_chk = True

    note_speed = 0.5

    combo = 0

    total_score = 0

    elapsed_time_chk = False

    note_fin_chk = 0

    pushed_time = 0

    special_chk1 = False
    special_chk2 = False
    special_chk3 = False

    while start_game_chk:

        dt = clock.tick(30)

        for event in P.event.get():
            if event.type == P.QUIT:
                start_game_chk = False
                
            elif event.type == P.KEYDOWN:
                if event.key == P.K_a: note_hit_chk[0] = True
                elif event.key == P.K_s: note_hit_chk[1] = True
                elif event.key == P.K_d: 
                    note_hit_chk[2] = True
                    special_chk1 = True
                elif event.key == P.K_f: note_hit_chk[3] = True
                elif event.key == P.K_ESCAPE: clicked_btn = [option_btn_icon_rect]
                
                if special_chk1:
                    if event.key == P.K_j: special_chk2 = True
                if special_chk2:
                    if event.key == P.K_a: special_chk3 = True

            elif event.type == P.KEYUP:
                if event.key == P.K_a: note_hit_chk[0] = False
                elif event.key == P.K_s: note_hit_chk[1] = False
                elif event.key == P.K_d: note_hit_chk[2] = False
                elif event.key == P.K_f: note_hit_chk[3] = False

                pushed_time = 0


            elif event.type == P.MOUSEBUTTONDOWN:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in start_menu_btn_list if b.collidepoint(pos)]

        in_game_score = "SCORE : {}".format(total_score)
        in_game_score_msg = in_game_font.render(in_game_score, True, (255, 255, 255))
        in_game_score_msg_rect = in_game_score_msg.get_rect(center=(int(screen_width/2 + 400), int(screen_height / 2 - 100)))

        in_game_combo = "COMBO : {}".format(combo)
        in_game_combo_msg = in_game_font.render(in_game_combo, True, (255, 255, 255))
        in_game_combo_msg_rect = in_game_combo_msg.get_rect(center=(int(screen_width/2 + 400), int(screen_height / 2)))



        if option_btn_icon_rect in clicked_btn:
            print("게임 중지")
            start_ticks_chk = True
            btn_click_sound.play()
            P.mixer.music.pause()
            in_game_option_return = in_game_option_window_open()

            if in_game_option_return == "restart":
                select_music_sound.play()
                return "restart"

            elif in_game_option_return == "continue":
                timer_chk = True

            elif in_game_option_return == "quit":
                select_music_sound.play()
                return "quit"

            clicked_btn = []

        screen.blit(default_background, (0, 0))
        screen.blit(background, (0, -(screen_height - background_height) / 2))
        screen.blit(option_btn_icon, ((screen_width - option_btn_icon_width - 10), 10))
        if special_chk3: screen.blit(special_background, (0, -(screen_height - background_height) / 2))

        
        for i in range(0,4):

            temp_width = 0

            if note_hit_chk[i]: screen.blit(hit_effect, (10 + i*hit_effect_width, 0))
            width = (2*i + 1) * 10 + i * note_width + 1
            line_width = (2*(i + 1)) * 10 + (i+1) * note_width
            screen.blit(ingame_line, (10 + temp_width - 1, 0))
            screen.blit(notes[i], (10 + width, screen_height - note_height - 5))
            screen.blit(ingame_line, (10 + line_width, 0))
            temp_width = width

    
        if timer_chk:

            if start_ticks_chk:
                start_ticks = P.time.get_ticks()
                start_ticks_chk = False
            timer = count_down(start_ticks)


        if timer != None: 
            screen.blit(timer, (screen_width / 2, screen_height / 2))
            
        else:

            if game_started_chk:
                P.mixer.music.unpause()
                timer_chk = False
                music_chk = False

            elif music_chk:
                P.mixer.music.load(os.path.join(music_path, soundList[music_index].getMusicPath()))
                P.mixer.music.play()
                game_started_chk = True
                timer_chk = False
                music_chk = False
                start_ticks = P.time.get_ticks()

            if pushed_time < 1:
                for note in hit_note_list:
                    if note.getYPos() < (screen_height + note_height):
                        hit_note_rect = hit_note.get_rect()
                        hit_note_rect.left = note.getXPos()
                        hit_note_rect.top = note.getYPos()


                        if (abs(note1_rect.top - hit_note_rect.top) / note_height * 100 <= 10) and\
                           (note1_rect.left == hit_note_rect.left) and note_hit_chk[0]:
                            combo += 1
                            total_score += 1000
                            del hit_note_list[0]
                            perfect_chk = True
                            greate_chk = False
                            good_chk = False
                            nice_chk = False
                            bad_chk = False
                            pushed_time += 1

                        elif (abs(note2_rect.top - hit_note_rect.top) / note_height * 100 <= 30) and\
                             (note2_rect.left == hit_note_rect.left) and note_hit_chk[1]:
                            combo += 1
                            total_score += 800
                            del hit_note_list[0]
                            perfect_chk = False
                            greate_chk = True
                            good_chk = False
                            nice_chk = False
                            bad_chk = False
                            pushed_time += 1

                        elif (abs(note3_rect.top - hit_note_rect.top) / note_height * 100 <= 50) and\
                             (note3_rect.left == hit_note_rect.left) and note_hit_chk[2]:
                            combo += 1
                            total_score += 600
                            del hit_note_list[0]
                            perfect_chk = False
                            greate_chk = False
                            good_chk = False
                            nice_chk = True
                            bad_chk = False
                            pushed_time += 1

                        elif (abs(note4_rect.top - hit_note_rect.top) / note_height * 100 <= 70) and\
                             (note4_rect.left == hit_note_rect.left) and note_hit_chk[3]:
                            combo = 0
                            total_score += 200
                            del hit_note_list[0]
                            perfect_chk = False
                            greate_chk = False
                            good_chk = True
                            nice_chk = False
                            bad_chk = False
                            pushed_time += 1
                        
                        elif ((((note1_rect.top - hit_note_rect.top) / note_height * 100 <= -95) and\
                             (note1_rect.left == hit_note_rect.left)) or\
                            (((note2_rect.top - hit_note_rect.top) / note_height * 100 <= -95) and\
                             (note2_rect.left == hit_note_rect.left)) or\
                            (((note3_rect.top - hit_note_rect.top) / note_height * 100 <= -95) and\
                             (note3_rect.left == hit_note_rect.left)) or\
                            (((note4_rect.top - hit_note_rect.top) / note_height * 100 <= -95) and\
                             (note4_rect.left == hit_note_rect.left))):
                            combo = 0
                            del hit_note_list[0]
                            perfect_chk = False
                            greate_chk = False
                            good_chk = False
                            nice_chk = False
                            bad_chk = True

                        elif (note_hit_chk[0] or note_hit_chk[1] or note_hit_chk[2] or note_hit_chk[3]):
                            combo = 0
                            perfect_chk = False
                            greate_chk = False
                            good_chk = False
                            nice_chk = False
                            bad_chk = True
                            pushed_time += 1
                            

        elapsed_time = int((P.time.get_ticks() - start_ticks) / 100)
        if tmp_time != elapsed_time: elapsed_time_chk = True
        tmp_time = elapsed_time

        if elapsed_time_chk:
            if elapsed_time in note_list:
                r = random.randint(0, 3)
                x_pos = (2 * r + 1) * 10 + r * note_width + 11
                hit_note_list.append(musicNoteList.Note(x_pos, 0))
                elapsed_time_chk = False
                note_fin_chk += 1
                    
        if len(note_list) == note_fin_chk:
            time.sleep(3)
            P.mixer.music.stop()
            fade_out_img()
            result = game_result(total_score, combo, music_index, soundList)
            return result

        if perfect_chk: screen.blit(perfect_msg, perfect_msg_rect)
        elif greate_chk: screen.blit(greate_msg, greate_msg_rect)
        elif nice_chk: screen.blit(nice_msg, nice_msg_rect)
        elif good_chk: screen.blit(good_msg, good_msg_rect)
        elif bad_chk: screen.blit(bad_msg, bad_msg_rect)

        for note in hit_note_list:
            screen.blit(hit_note, (note.getXPos(), note.getYPos()))
            note.plusYPos(note_speed * dt)


        screen.blit(in_game_score_msg, in_game_score_msg_rect)
        screen.blit(in_game_combo_msg, in_game_combo_msg_rect)
        

        P.display.update()
        

    P.quit()


def run_game():
    start_menu()
    df = pd.DataFrame({"name":musicFunctions.data_name, "file_name":musicFunctions.data_file_name, 
                       "cover_img_name":musicFunctions.data_cover_img_name, "type_name":musicFunctions.data_type_name, 
                       "best_score":musicFunctions.data_best_score
                      })
    write = pd.ExcelWriter("DataBase.xlsx", engine="xlsxwriter")
    df.to_excel(write, sheet_name="Sheet1")
    write.close()


if __name__ == "__main__":
    run_game()
import pygame as P
import os, sys
import musicFunctions
import time
import requests
import random
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
title_font = P.font.Font(None, 100)
default_font = P.font.Font(None, 70)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "img")
music_path = os.path.join(current_path, "sounds")

start_menu_background = P.image.load(os.path.join(image_path, "start_menu_background.png")) 
select_music_menu_background = P.image.load(os.path.join(image_path, "select_music_menu_background.png")) 
background = P.image.load(os.path.join(image_path, "background.png"))


btn_click_sound = P.mixer.Sound(os.path.join(music_path, "other_btn.wav"))
btn_click_sound.set_volume(0.5)
select_music_sound = P.mixer.Sound(os.path.join(music_path, "game_start.wav")) #적당한 브금 찾아서 넣기
select_music_sound.set_volume(0.5)
music_volume = 1.0


# weather data crawling
html = requests.get('https://search.naver.com/search.naver?query=날씨')
soup = BeautifulSoup(html.text, 'html.parser')
data = soup.find("div", {'class':'weather_box'})
weatherData = data.find('p', {'class':'cast_txt'}).text
print(weatherData)


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

cancel_btn = P.image.load(os.path.join(image_path, "cancel_btn.png"))
cancel_btn_size = cancel_btn.get_rect().size
cancel_btn_width = cancel_btn_size[0]
cancel_btn_height = cancel_btn_size[1]


# start menu png files
game_start_btn = P.image.load(os.path.join(image_path, "game_start_btn.png"))
game_start_btn_size = game_start_btn.get_rect().size
game_start_btn_width = game_start_btn_size[0]
game_start_btn_height = game_start_btn_size[1]

option_btn = P.image.load(os.path.join(image_path, "option_btn.png"))
option_btn_size = option_btn.get_rect().size
option_btn_width = option_btn_size[0]
option_btn_height = option_btn_size[1]

game_quit_btn = P.image.load(os.path.join(image_path, "game_quit_btn.png"))
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

select_music_btn = P.image.load(os.path.join(image_path, "select_music_btn.png"))
select_music_btn_size = select_music_btn.get_rect().size
select_music_btn_width = select_music_btn_size[0]
select_music_btn_height = select_music_btn_size[1]


# start game files
node1 = P.image.load(os.path.join(image_path, "node.png"))
node2 = P.image.load(os.path.join(image_path, "node.png"))
node3 = P.image.load(os.path.join(image_path, "node.png"))
node4 = P.image.load(os.path.join(image_path, "node.png"))
node_size = node1.get_rect().size
node_height = node_size[1]
node_width = node_size[0]

hit_effect = P.image.load(os.path.join(image_path, "hit_effect.png"))

node_hit_chk = [False, False, False, False]

fade_img = P.image.load(os.path.join(image_path, "fade_img.png"))



total_time = 3


def fade_out_img():
    for x in range(0, 255):
        fade_img.set_alpha(x)
        screen.blit(fade_img, (0, 0))
        P.display.update()

def count_down(start_ticks):
    elapsed_time = (P.time.get_ticks() - start_ticks) / 1000
    timer = default_font.render(str(int(total_time - elapsed_time + 1)), True, (255, 255, 255))
    screen.blit(timer, (screen_width / 2, screen_height / 2))
    if total_time - elapsed_time <= 0: return
    P.display.update()
    

def option_window_open():
    # volume_line_cnt에 맞춰서 volume_line 만들기
    global music_volume

    music_volume_title = "Music Volume"
    music_volume_title_msg = default_font.render(music_volume_title, True, (0, 0, 0))
    music_volume_title_msg_rect = music_volume_title_msg.get_rect(center=(int((screen_width)/2), int((screen_height)/2 - 20)))

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
            
            if event.type == P.MOUSEBUTTONUP:
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
        for space in range(0, volume_line_cnt):
            P.draw.rect(screen, (134, 240, 134), [((screen_width- volume_plus_btn_width) / 2 + volume_plus_btn_width - 250 + space * 46), ((screen_height - volume_plus_btn_height) / 2 + 60), 40, 50])
        screen.blit(cancel_btn, ((screen_width - cancel_btn_width) / 2, (screen_height - cancel_btn_height) / 2 + 175))

        P.display.update()

    P.quit()


def start_menu():
    global music_volume

    game_title = "A S D F"
    game_title_msg = title_font.render(game_title, True, (255, 255, 255))
    game_title_msg_rect = game_title_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 - 200)))

    P.mixer.music.load(os.path.join(music_path, "비.wav")) #적당한 브금 찾아서 넣기
    P.mixer.music.play(-1)

    start_menu_quit_chk = False
    start_menu_select_chk = True

    game_start_btn_rect = game_start_btn.get_rect()
    game_start_btn_rect.left = (screen_width-game_start_btn_width)/2
    game_start_btn_rect.top = (screen_height - game_start_btn_height)/2 - 50

    option_btn_rect = option_btn.get_rect()
    option_btn_rect.left = (screen_width-option_btn_width)/2
    option_btn_rect.top = (screen_height - option_btn_height)/2 + 100

    game_quit_btn_rect = game_quit_btn.get_rect()
    game_quit_btn_rect.left = (screen_width-game_quit_btn_width)/2
    game_quit_btn_rect.top = (screen_height - game_quit_btn_height)/2 + 250
    

    clicked_btn = []
    start_menu_btn_list = [game_quit_btn_rect, game_start_btn_rect, option_btn_rect]

    

    while (not start_menu_quit_chk) and start_menu_select_chk:
        P.mixer.music.set_volume(music_volume)
                
        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in P.event.get():
            if event.type == P.QUIT:
                start_menu_quit_chk = True
            
            if event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in start_menu_btn_list if b.collidepoint(pos)]

            
        if game_start_btn_rect in clicked_btn:
            print("게임시작")
            btn_click_sound.play()
            select_music()
            clicked_btn = []

        elif option_btn_rect in clicked_btn:
            btn_click_sound.play()
            option_window_open()
            clicked_btn = []

        elif game_quit_btn_rect in clicked_btn: 
            btn_click_sound.play()
            print("종료 버튼 클릭")
            start_menu_select_chk = False
            
        
        screen.blit(start_menu_background, (0, 0))
        screen.blit(game_title_msg, game_title_msg_rect)
        screen.blit(game_start_btn, ((screen_width-game_start_btn_width)/2, (screen_height - game_start_btn_height)/2 - 50))
        screen.blit(option_btn, ((screen_width-option_btn_width)/2, (screen_height - option_btn_height)/2 + 100))
        screen.blit(game_quit_btn, ((screen_width-game_quit_btn_width)/2, (screen_height - game_quit_btn_height)/2 + 250))

        P.display.update()

    P.quit()
    
# 시작 화면 완성 이제 음악 선택 화면 만들기

def select_music():
    select_music_quit_chk = True

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

    music_list_idx_chk = 0

    recomend_music = []
    
    for music in musicFunctions.soundList:
        if music.getMusicType() in weatherData:
            recomend_music.append(music)

    random_recomend = random.randint(0, len(recomend_music)-1)

    recomend_music = [recomend_music[random_recomend]]

    musicFunctions.soundList.insert(0, recomend_music[0])


    while select_music_quit_chk:
        P.mixer.music.set_volume(music_volume)

        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in P.event.get():
            if event.type == P.QUIT:
                select_music_quit_chk = False
            
            if event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in start_menu_btn_list if b.collidepoint(pos)]

        if back_arrow_btn_rect in clicked_btn:
            btn_click_sound.play()
            return

        elif left_arrow_btn_rect in clicked_btn:
            btn_click_sound.play()
            if music_list_idx_chk > 0:
                music_list_idx_chk -= 1

            clicked_btn = []
        
        elif right_arrow_btn_rect in clicked_btn:
            btn_click_sound.play()
            if music_list_idx_chk < (len(musicFunctions.soundList) - 1):
                music_list_idx_chk += 1

            clicked_btn = []
        
        elif select_music_btn_rect in clicked_btn:
            select_music_sound.play()
            P.mixer.music.stop()
            fade_out_img()
            start_game(music_list_idx_chk)
            fade_out_img()
            P.mixer.music.play(-1)
            clicked_btn = []
    
        screen.blit(select_music_menu_background, (0, 0))

        if music_list_idx_chk == 0:
            first_img = P.image.load(os.path.join(image_path, musicFunctions.soundList[music_list_idx_chk].getCoverImage()))
            first_img_size = first_img.get_rect().size
            first_img_width = first_img_size[0]
            first_img_height = first_img_size[1]
            second_img = P.image.load(os.path.join(image_path, musicFunctions.soundList[music_list_idx_chk + 1].getCoverImage()))
            second_img_size = second_img.get_rect().size
            second_img_width = second_img_size[0]
            second_img_height = second_img_size[1]

            screen.blit(first_img, ((screen_width - first_img_width)/2, (screen_height - first_img_height)/ 2))
            screen.blit(second_img, ((screen_width - second_img_width)/2 + first_img_width + 100, (screen_height - second_img_height)/ 2))
            
        elif music_list_idx_chk == (len(musicFunctions.soundList) - 1):            
            first_img = P.image.load(os.path.join(image_path, musicFunctions.soundList[music_list_idx_chk - 1].getCoverImage()))
            first_img_size = first_img.get_rect().size
            first_img_width = first_img_size[0]
            first_img_height = first_img_size[1]
            second_img = P.image.load(os.path.join(image_path, musicFunctions.soundList[music_list_idx_chk].getCoverImage()))
            second_img_size = second_img.get_rect().size
            second_img_width = second_img_size[0]
            second_img_height = second_img_size[1]

            screen.blit(first_img, ((screen_width - first_img_width)/2 - second_img_width - 100, (screen_height - first_img_height)/ 2))
            screen.blit(second_img, ((screen_width - second_img_width)/2, (screen_height - second_img_height)/ 2))
            
        else:
            first_img = P.image.load(os.path.join(image_path, musicFunctions.soundList[music_list_idx_chk - 1].getCoverImage()))
            first_img_size = first_img.get_rect().size
            first_img_width = first_img_size[0]
            first_img_height = first_img_size[1]
            second_img = P.image.load(os.path.join(image_path, musicFunctions.soundList[music_list_idx_chk].getCoverImage()))
            second_img_size = second_img.get_rect().size
            second_img_width = second_img_size[0]
            second_img_height = second_img_size[1]
            third_img = P.image.load(os.path.join(image_path, musicFunctions.soundList[music_list_idx_chk + 1].getCoverImage()))
            third_img_size = third_img.get_rect().size
            third_img_width = third_img_size[0]
            third_img_height = third_img_size[1]
            
            screen.blit(first_img, ((screen_width - first_img_width)/2 - second_img_width - 100, (screen_height - first_img_height)/ 2))
            screen.blit(second_img, ((screen_width - second_img_width)/2, (screen_height - second_img_height)/ 2))
            screen.blit(third_img, ((screen_width - third_img_width)/2 + second_img_width + 100, (screen_height - third_img_height)/ 2))
        
        screen.blit(back_arrow_btn, (10, 10))
        screen.blit(left_arrow_btn, (left_arrow_btn_width, (screen_height - left_arrow_btn_height) / 2))
        screen.blit(right_arrow_btn, (screen_width - right_arrow_btn_width * 2, (screen_height - right_arrow_btn_height) / 2))
        screen.blit(select_music_btn, ((screen_width-select_music_btn_width)/2, (screen_height - select_music_btn_height)/2 + 300))
        

        P.display.update()

    

    P.mixer.music.stop()
    del musicFunctions.soundList[0]

    P.quit()


def start_game(music_index):
    start_ticks = P.time.get_ticks()
    

    start_game_chk = True

    while start_game_chk:
        dt = clock.tick(30)
        count_down(start_ticks)
        
        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in P.event.get():
            if event.type == P.QUIT:
                start_game_chk = False
                
            if event.type == P.KEYDOWN:
                if event.key == P.K_a:
                    node_hit_chk[0] = True
                elif event.key == P.K_s:
                    node_hit_chk[1] = True
                elif event.key == P.K_d:
                    node_hit_chk[2] = True
                elif event.key == P.K_f:
                    node_hit_chk[3] = True

            if event.type == P.KEYUP:
                if event.key == P.K_a:
                    node_hit_chk[0] = False
                elif event.key == P.K_s:
                    node_hit_chk[1] = False
                elif event.key == P.K_d:
                    node_hit_chk[2] = False
                elif event.key == P.K_f:
                    node_hit_chk[3] = False



        # 3. 게임 캐릭터 위치 정의
    
        # 4. 충돌 처리

        # 5. 화면에 그리기

        screen.blit(background, (0,0))

        if node_hit_chk[0]: screen.blit(hit_effect, (0, 0))
        if node_hit_chk[1]: screen.blit(hit_effect, (270, 0))
        if node_hit_chk[2]: screen.blit(hit_effect, (540, 0))
        if node_hit_chk[3]: screen.blit(hit_effect, (810, 0))

        screen.blit(node1, (10, screen_height - node_height))
        screen.blit(node2, (280, screen_height - node_height))
        screen.blit(node3, (550, screen_height - node_height))
        screen.blit(node4, (820, screen_height - node_height))

        P.display.update()

    P.quit()

def run_game():
    start_menu()

run_game()
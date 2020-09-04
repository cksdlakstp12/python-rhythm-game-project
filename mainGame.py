import pygame as P
import os, sys
import musicFunctions
import time

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
title_font = P.font.Font(None, 80)

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "img")

start_menu_background = P.image.load(os.path.join(image_path, "start_menu_background.png")) 
select_music_menu_background = P.image.load(os.path.join(image_path, "select_music_menu_background.png")) 
background = P.image.load(os.path.join(image_path, "background.png"))


select_menu_sound = P.mixer.music.load("./sounds/눈사람.wav") #적당한 브금 찾아서 넣기
music_volume = 1.0


option_window = P.image.load(os.path.join(image_path, "option_window.png"))
option_window_size = option_window.get_rect().size
option_window_width = option_window_size[0]
option_window_height = option_window_size[1]




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

back_arrow = P.image.load(os.path.join(image_path, "back_arrow.png"))
back_arrow_size = back_arrow.get_rect().size
back_arrow_width = back_arrow_size[0]
back_arrow_height = back_arrow_size[1]

right_arrow = P.image.load(os.path.join(image_path, "right_arrow.png"))
right_arrow_size = right_arrow.get_rect().size
right_arrow_width = right_arrow_size[0]
right_arrow_height = right_arrow_size[1]

left_arrow = P.image.load(os.path.join(image_path, "left_arrow.png"))
left_arrow_size = left_arrow.get_rect().size
left_arrow_width = left_arrow_size[0]
left_arrow_height = left_arrow_size[1]


node1 = P.image.load(os.path.join(image_path, "node.png"))
node2 = P.image.load(os.path.join(image_path, "node.png"))
node3 = P.image.load(os.path.join(image_path, "node.png"))
node4 = P.image.load(os.path.join(image_path, "node.png"))
node_size = node1.get_rect().size
node_height = node_size[1]
node_width = node_size[0]

hit_effect = P.image.load(os.path.join(image_path, "hit_effect.png"))

node_hit_chk = [False, False, False, False]

def option_window_open():
    global music_volume

    cancel = False

    option_window_rect = option_window.get_rect()
    option_window_rect.left = (screen_width - option_window_width)/2
    option_window_rect.top = (screen_height - option_window_height)/2

    # + - 버튼 위치 조정 하기
    # pygmae volume 참고 : https://jbmpa.com/pygame/10
    volume_plus_btn_rect = volume_plus_btn.get_rect()
    volume_plus_btn_rect.left = ((screen_width - option_window_width)/2 - volume_plus_btn_width) / 2 + 275
    volume_plus_btn_rect.top = ((screen_height - option_window_height)/2 - volume_plus_btn_height) / 2 + 100

    volume_minus_btn_rect = volume_minus_btn.get_rect()
    volume_minus_btn_rect.left = ((screen_width - option_window_width)/2 - volume_minus_btn_width) / 2 - 275
    volume_minus_btn_rect.top = ((screen_height - option_window_height)/2 - volume_minus_btn_height) / 2 + 100

    cancel_btn_rect = cancel_btn.get_rect()
    cancel_btn_rect.left = ((screen_width - option_window_width)/2 - cancel_btn_width) / 2
    cancel_btn_rect.top = ((screen_height - option_window_height)/2 - cancel_btn_height) / 2 + 175
    
    clicked_btn = []
    option_window_btn_list = [volume_plus_btn_rect, volume_minus_btn_rect, cancel_btn_rect]

    while not cancel:
        for event in P.event.get():
            if event.type == P.QUIT:
                cancel = True
            
            if event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in option_window_btn_list if b.collidepoint(pos)]


        if volume_plus_btn_rect in clicked_btn:
            if music_volume < 1.0:
                music_volume = music_volume + 0.1

        elif volume_minus_btn_rect in clicked_btn:
            if music_volume > 0.0:
                music_volume = music_volume - 0.1

        elif cancel_btn_rect in clicked_btn:
            return

        screen.blit(option_window, ((screen_width - option_window_width)/2, (screen_height - option_window_height)/2))
        screen.blit(volume_plus_btn, (((screen_width - option_window_width)/2 - volume_plus_btn_width) / 2 + 275, ((screen_height - option_window_height)/2 - volume_plus_btn_height) / 2 + 100))
        screen.blit(volume_minus_btn, (((screen_width - option_window_width)/2 - volume_minus_btn_width) / 2 - 275, ((screen_height - option_window_height)/2 - volume_minus_btn_height) / 2 + 100))

        P.display.update()

    P.quit()

    


def start_menu():
    global music_volume

    game_title = "A S D F"
    game_title_msg = title_font.render(game_title, True, (255, 255, 255))
    game_title_msg_rect = game_title_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 - 200)))

    P.mixer.music.load("./sounds/비.wav") #적당한 브금 찾아서 넣기
    P.mixer.music.set_volume(music_volume)
    P.mixer.music.play(-1)

    start_menu_quit_chk = False
    start_menu_select_chk = True

    game_start_btn_rect = game_start_btn.get_rect()
    game_start_btn_rect.left = (screen_width - game_quit_btn_width)/2
    game_start_btn_rect.top = (screen_height - game_quit_btn_height)/2  - 50

    option_btn_rect = option_btn.get_rect()
    option_btn_rect.left = (screen_width - option_btn_width)/2
    option_btn_rect.top = (screen_height - option_btn_height)/2 + 100

    game_quit_btn_rect = game_quit_btn.get_rect()
    game_quit_btn_rect.left = (screen_width - game_start_btn_width)/2
    game_quit_btn_rect.top = (screen_height - game_start_btn_height)/2 + 250

    clicked_btn = []
    start_menu_btn_list = [game_quit_btn_rect, game_start_btn_rect, option_btn_rect]


    while (not start_menu_quit_chk) and start_menu_select_chk:
        
        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in P.event.get():
            if event.type == P.QUIT:
                start_menu_quit_chk = True
            
            if event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()

                clicked_btn = [b for b in start_menu_btn_list if b.collidepoint(pos)]

            
        if game_start_btn_rect in clicked_btn:
            print("게임시작")
            P.mixer.music.stop()
            select_music()

        elif option_btn_rect in clicked_btn:
            option_window_open()

        elif game_quit_btn_rect in clicked_btn: 
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
    P.mixer.music.load("./sounds/눈사람.wav") #적당한 브금 찾아서 넣기
    P.mixer.music.set_volume(music_volume)
    P.mixer.music.play(-1)
    select_music_quit_chk = True

    while select_music_quit_chk:
        
        # 2. 이벤트 처리 (키보드, 마우스 등)
        for event in P.event.get():
            if event.type == P.QUIT:
                select_music_quit_chk = False
            
            if event.type == P.MOUSEBUTTONUP:
                pos = P.mouse.get_pos()


        
            


        screen.blit(select_music_menu_background, (0, 0))
        screen.blit(back_arrow, (10, 10))
        screen.blit(left_arrow, (left_arrow_width, (screen_height - left_arrow_height) / 2))
        screen.blit(right_arrow, (screen_width - right_arrow_width * 2, (screen_height - right_arrow_height) / 2))
        

        P.display.update()

    

    P.mixer.music.stop()
    
    P.quit()


def start_game():
    start_game_chk = True

    while start_game_chk:
        dt = clock.tick(30)
        
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
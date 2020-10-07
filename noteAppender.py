import pygame as P
import pandas as pd
import time as T

music_name_input = str(input("음악의 이름을 입력하면 Note Appender가 실행됩니다. : "))


#####################################################################
# 기본 초기화 (반드시 해야하는 것들)

P.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 1080 # 가로 크기
screen_height = 720 # 세로 크기
screen = P.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
P.display.set_caption("Note Appender")

# FPS
clock = P.time.Clock()

#####################################################################
# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
total_time = 3

def count_down(start_ticks):
    elapsed_time = (P.time.get_ticks() - start_ticks) / 1000
    timer = default_font.render(str(int(total_time - elapsed_time + 1)), True, (255, 255, 255))
    if total_time - elapsed_time > 0: return timer

font_path = "C:\\Users\\cksdl\\Desktop\\termProject\\font\\FivoSans-Black-Oblique.otf"

default_background = P.image.load("C:\\Users\\cksdl\\Desktop\\termProject\\img\\default_background.png")

default_font = P.font.Font(font_path, 60)
time_font = P.font.Font(font_path, 30)

music_note_name = music_name_input[:music_name_input.find(".")] + "_note_added"

note_added_list = ""

music_path = "C:\\Users\\cksdl\\Desktop\\termProject\\sounds\\" + music_name_input

P.mixer.music.load(music_path)

append = "APPENDED"
append_msg = default_font.render(append, True, (255, 255, 255))
append_msg_rect = append_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2)))
append_chk = False

stop_append = "STOP APPENDING"
stop_append_msg = default_font.render(stop_append, True, (255, 255, 255))
stop_append_msg_rect = stop_append_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2)))
stop_append_chk = False

append_guidance = "PRESS SPACE TO APPEND"
append_guidance_msg = default_font.render(append_guidance, True, (255, 255, 255))
append_guidance_msg_rect = append_guidance_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 - 300)))
append_guidance_chk = False

restart_adding_guidance = "PRESS R KEY TO RESTART APPEND"
restart_adding_guidance_msg = default_font.render(restart_adding_guidance, True, (255, 255, 255))
restart_adding_guidance_msg_rect = restart_adding_guidance_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 - 150)))
restart_adding_guidance_chk = False

escape_guidance = "PRESS ESCAPE TO STOP APPEND"
escape_guidance_msg = default_font.render(escape_guidance, True, (255, 255, 255))
escape_guidance_msg_rect = escape_guidance_msg.get_rect(center=(int(screen_width/2), int(screen_height / 2 + 150)))
escape_guidance_chk = False

start_ticks = 0
timer_chk = True
timer = None
music_chk = True
first_append_chk = True
start_ticks_chk = True

space_pushed_time_chk = 0
space_pushed_chk = False
escape_pushed_chk = False

running = True
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in P.event.get():
        if event.type == P.QUIT:
            running = False

        if event.type == P.KEYDOWN:
            if event.key == P.K_SPACE:
                space_pushed_time_chk += 1

            elif event.key == P.K_r:
                timer_chk = True
                first_append_chk = True
                music_chk = True
                note_added_list = ""
                space_pushed_time_chk = 0
                space_pushed_chk = True

            elif event.key == P.K_ESCAPE:
                escape_pushed_chk = True

        if event.type == P.KEYUP:
            if event.key == P.K_SPACE:
                space_pushed_chk = True
                space_pushed_time_chk = 0
                
    elapsed_time = int((P.time.get_ticks() - start_ticks) / 100)
    elapsed_time_text = str(elapsed_time / 10)
    elapsed_time_guidance = elapsed_time_text
    elapsed_time_guidance_msg = default_font.render(elapsed_time_guidance, True, (255, 255, 255))
    elapsed_time_guidance_msg_rect = elapsed_time_guidance_msg.get_rect(center=(int(screen_width/2 - 400), int(screen_height / 2)))
    screen.blit(default_background, (0, 0))

    if timer_chk:
        if start_ticks_chk:
            start_ticks = P.time.get_ticks()
            start_ticks_chk = False
        timer = count_down(start_ticks)

    if timer != None: 
        screen.blit(timer, (screen_width / 2, screen_height / 2))
            
    else:
        if music_chk:
            P.mixer.music.load(music_path)
            pushed_chk = 0
            P.mixer.music.play()
            music_chk = False
            timer_chk = False
            start_ticks = P.time.get_ticks()

        screen.blit(elapsed_time_guidance_msg, elapsed_time_guidance_msg_rect)

        if space_pushed_time_chk > 0:
            if space_pushed_chk:
                if first_append_chk:
                    note_added_list += str(elapsed_time)
                    first_append_chk = False
                else:
                    note_added_list += ("," + str(elapsed_time))

                space_pushed_chk = False

            screen.blit(append_msg, append_msg_rect)
    
    if escape_pushed_chk:
        screen.blit(stop_append_msg, stop_append_msg_rect)
        P.display.update()
        T.sleep(3)
        running = False
        
    screen.blit(append_guidance_msg, append_guidance_msg_rect)
    screen.blit(escape_guidance_msg, escape_guidance_msg_rect)

    P.display.update()


P.quit()

print("노트가 찍힌 시간 : " + note_added_list)

data = pd.read_excel("DataBase.xlsx")

data_name = data[:]["name"]
data_file_name = data[:]["file_name"]
data_cover_img_name = data[:]["cover_img_name"]
data_type_name = data[:]["type_name"]
data_best_score = data[:]["best_score"]
data_note_list = data[:]["note_list"]

note_list_idx = -1

for idx, file_name in enumerate(data_file_name):
    if file_name != music_name_input:
        data_note_list[idx] = "*"
    else:
        data_note_list[idx] = note_added_list


df = pd.DataFrame({"name":data_name, "file_name":data_file_name, 
                    "cover_img_name":data_cover_img_name, "type_name":data_type_name, 
                    "best_score":data_best_score, "note_list":data_note_list
                    })
write = pd.ExcelWriter("DataBase.xlsx", engine="xlsxwriter")
df.to_excel(write, sheet_name="Sheet1")
write.close()

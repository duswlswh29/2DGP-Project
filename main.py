from pico2d import *


def handle_events():
   global running
   events=get_events()
   for event in events:
       if event.type==SDL_QUIT:
           running=False
       elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
           running=False
pass



def reset_world():
  global running
  running=True

pass

def update_world():

    pass

def render_world():

    clear_canvas()
    # .draw() 호출하고 클래스에 드로우 정의
    update_canvas()
pass
open_canvas()
reset_world()

while running:
    handle_events() #입력 처리
    update_world() #게임 로직 업데이트
    render_world() #렌더링
    delay(0.05) #프레임 제어
close_canvas()
from pico2d import *


#Game object class here
class Background:
   def __init__(self):
       self.image=load_image('background.png') #배경이미지 로드



   def draw(self):

       self.image.draw(400,300,800,600)
   def update(self):

       pass

class Chunli:
   #캐릭터가 위치할 캔버스 좌표 설정
    def __init__(self,x,y):
        self.x=90
        self.y=100
        self.frame=0
        self.image=load_image('chunli-idle1.png')

        self.w=120 #캔버스에 그릴 너비
        self.h=200 #캔버스에 그릴 높이

    def update(self):
        self.frame=(self.frame+1) % 4
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 90, 0, 90,180, self.x, self.y)


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
  global background1
  background1=Background() #Background 도장을 이용해서 background1 객체생성
  global chunli
  chunli=Chunli(90,100)#Chunli 도장을 이용해서 chunli 객체생성
pass

def update_world():
    chunli.update()
    pass

def render_world():

    clear_canvas()
    background1.draw()# .draw() 호출하고 클래스에 드로우 정의
    chunli.draw()
    update_canvas()
pass
open_canvas()
reset_world()

while running:
    handle_events() #입력 처리
    update_world() #게임 로직 업데이트
    render_world() #렌더링
    delay(0.1) #프레임 제어
close_canvas()
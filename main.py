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
        self.state='idle'
        self.dir=1
        self.frame=0

        self.idle_image=load_image('chunli-idle1.png')
        self.walk_image=load_image('chunli-walk.png')
        self.jump_image=load_image('chunli-jump.png')
        self.crouch_image=load_image('chunli-crouch.png')

        self.w=120 #캔버스에 그릴 너비
        self.h=200 #캔버스에 그릴 높이

    def update(self):
     if self.state=='idle':
        self.frame=(self.frame+1) % 4
     elif self.state=='walk':
          self.frame=(self.frame+1)%8
          self.x+=self.dir*5
     elif self.state=='jump':
         self.frame=(self.frame+1)%4
     elif self.state=='crouch':
         self.frame=(self.frame+1)%2

    def draw(self):
      if self.state=='idle':
          self.idle_image.clip_draw(self.frame * 90, 0, 90,180, self.x, self.y)
      elif self.state=='walk':
          self.walk_image.clip_draw(self.frame*125,0,125,250,self.x,self.y,97,187)
      elif self.state=='jump':
          self.jump_image.clip_draw(self.frame*118,0,118,266,self.x,self.y,80,164)
      elif self.state=='crouch':
          self.crouch_image.clip_draw(self.frame*237,0,237,368,self.x,80,82,171)

def handle_events():
   global running
   events=get_events()
   for event in events:
       if event.type==SDL_QUIT:
           running=False
       elif event.type==SDL_KEYDOWN:
           if event.key==SDLK_ESCAPE:
            running=False
           elif event.key==SDLK_d:
            chunli.state='walk'
            chunli.dir=1
           elif event.key==SDLK_a:
            chunli.state='walk'
            chunli.dir=-1
           elif event.key==SDLK_w:
             chunli.state='jump'
           elif event.key==SDLK_s:
             chunli.state='crouch'
       elif event.type==SDL_KEYUP:
           chunli.state='idle'

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
open_canvas()#800 600
reset_world()

while running:
    handle_events() #입력 처리
    update_world() #게임 로직 업데이트
    render_world() #렌더링
    if chunli.state == 'idle':
        delay(0.1)
    elif chunli.state=='walk':
        delay(0.05)
    elif chunli.state=='jump':
        delay(0.19)
    elif chunli.state=='crouch':
        delay(0.1)
    #delay(0.05) #프레임 제어

close_canvas()
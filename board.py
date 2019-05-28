import pygame
import time
def get_wire_status():
    with open('terse_absence.txt','r')as f:
        status=f.read()
    return status

pygame.init()
x=pygame.FULLSCREEN
x=1
screen=pygame.display.set_mode((480,320),x,24)


background=pygame.image.load('背景.png')
show_pic_black=pygame.image.load('black.png')
show_pic_white=pygame.image.load('white.png')

done=False


while not done:
    screen.blit(background,(0,0))
    pygame.display.update() 

    status=get_wire_status()
    for i,s in enumerate(status):
        if i<int(len(status)/2)+1:
            print(int(len(status)/2)+1)
            if s=='0':
                screen.blit(show_pic_white,(33+i*44,135))
            elif s=='1':
                screen.blit(show_pic_black,(33+i*44,135))
        if i>=int(len(status)/2)+1:
            if s=='0':
                screen.blit(show_pic_white,(33+(i-(int(len(status)/2)+1))*44,225))
            elif s=='1':
                screen.blit(show_pic_black,(33+(i-(int(len(status)/2)+1))*44,225))
            
    pygame.display.update() 

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    time.sleep(6)
pygame.quit()
import pygame
import time
def get_wire_status():
    with open('terse_absence.txt','r')as f:
        status=f.read()
    return status

pygame.init()
screen=pygame.display.set_mode((480,320),pygame.FULLSCREEN,24)


background=pygame.image.load('背景.png')
show_pic_black=pygame.image.load('black.png')
show_pic_white=pygame.image.load('white.png')

done=False


while not done:
    screen.blit(background,(0,0))
    pygame.display.update() 

    status=get_wire_status()
    for i,s in enumerate(status):
        if i<len(status)/2:
            if s=='0':
                screen.blit(show_pic_white,(44+i*53,135))
            elif s=='1':
                screen.blit(show_pic_black,(44+i*53,135))
        if i>=len(status)/2:
            if s=='0':
                screen.blit(show_pic_white,(44+(i-len(status)/2)*53,215))
            elif s=='1':
                screen.blit(show_pic_black,(44+(i-len(status)/2)*53,215))
            
    pygame.display.update() 

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    time.sleep(6)
pygame.quit()
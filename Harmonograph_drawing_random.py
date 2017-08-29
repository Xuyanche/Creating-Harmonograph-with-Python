#与harmonograph_drawing.py相同，不调用serial，但是所有参数都随机设定。可以用来找好看的图形。
#和其他的一样，完成图会自动保存在运行目录里，文件名就是参数。
import pygame
import math
from pygame.locals import *
from sys import exit
import random

screen_width = 1000
screen_height = 1000
color = (0, 0, 0)

#参数随机设定，但是随机的范围可以在这里修改
space = 1
A1 = random.randint(80, 200)
f1 = 0.1 * random.randint(10,19)
d1 = 0.0001 * random.randint(1,9)
A2 = random.randint(80, 200)
f2 = 0.1 * random.randint(10,19)
d2 = 0.0001 * random.randint(1,9)
A3 = random.randint(80, 200)
f3 = 0.1 * random.randint(10,19)
d3 = 0.0001 * random.randint(1,9)
A4 = random.randint(80, 200)
f4 = 0.1 * random.randint(10,19)
d4 = 0.0001 * random.randint(1,9)
p1 = 0.1 * random.randint(1,9)
p2 = 0.1 * random.randint(1,9)
p3 = 0.1 * random.randint(1,9)
p4 = 0.1 * random.randint(1,9)

pygame.init()

fname = 'DL' +str(A1) +'-' +str(A2)+'-' +str(A3)+'-' +str(A4)+'-'\
        +str(f1)[:3]+'-' +str(f2)[:3]+'-' +str(f3)[:3]+'-' +str(f4)[:3]+'-' \
        +str(d1)[:6]+'-' +str(d2)[:6]+'-' +str(d3)[:6]+'-' +str(d4)[:6]+'-' \
        +str(p1)[:3]+'-' +str(p2)[:3]+'-' +str(p3)[:3]+'-' +str(p4)[:3]+'-' \
        +str(space) + '.png'

my_font=pygame.font.SysFont('arial',15)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Harmonograph_drawing_random')

t = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))
    while True:
        start_x = screen_width/2 + A1 * math.sin(t * f1*math.pi/180 + p1) * math.exp(-1* d1* t) +\
                A2 * math.sin(t * f2*math.pi/180 + p2) * math.exp(-1* d2* t)
        start_y = screen_height/2 + A3 * math.sin(t * f3*math.pi/180 +p3) * math.exp(-1* d3* t) +\
                A4 * math.sin(t * f4 * math.pi/180 + p4) * math.exp(-1* d4* t)

        end_x = screen_width/2 + A1 * math.sin((t+space) * f1 * math.pi/180 + p1) * math.exp(-1* d1* (t+space)) +\
                A2 * math.sin((t+space) * f2 * math.pi/180 + p2) * math.exp(-1* d2* (t+space))
        end_y = screen_height/2 + A3 * math.sin((t+space) * f3*math.pi/180 + p3) * math.exp(-1* d3* (t+space)) +\
                A4 * math.sin((t+space) * f4 * math.pi/180 + p4) * math.exp(-1* d4* (t+space))
        t += space
        pygame.draw.line(screen, color, (start_x,start_y), (end_x, end_y),2)
        if t >= 10000:
            pygame.image.save(screen, fname)
            exit()
        text_screen=my_font.render(fname, True, (255, 0, 0))
        screen.blit(text_screen, (50,50))
        pygame.display.update()

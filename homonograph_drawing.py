import pygame
import math
from pygame.locals import *
from sys import exit

#屏幕设置
screen_width = 1000
screen_height = 1000
color = (0, 0, 0)

#所有的数据可以在这里设定
space = 1
A1 = 200
f1 = 7.04
d1 = 1.85
A2 = 200
f2 = 7.04
d2 = 0.0001
A3 = 200
f3 = 7.04
d3 = 1.85
A4 = 200
f4 = 7.04
d4 = 1.85
p1 = 3.0788
p2 = 3.0788
p3 = 3.0788
p4 = 3.0788


pygame.init()
fname = 'DL' +str(A1) +'-' +str(A2)+'-' +str(A3)+'-' +str(A4)+'-'\
        +str(f1)[:3]+'-' +str(f2)[:3]+'-' +str(f3)[:3]+'-' +str(f4)[:3]+'-' \
        +str(d1)[:6]+'-' +str(d2)[:6]+'-' +str(d3)[:6]+'-' +str(d4)[:6]+'-' \
        +str(p1)[:3]+'-' +str(p2)[:3]+'-' +str(p3)[:3]+'-' +str(p4)[:3]+'-' \
        +str(space) + '.png'
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Homonograph Drawing')

t = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))
    while True:
        start_x = 300+ A1 * math.sin(t * f1*math.pi/180 + p1) * math.exp(-1* d1* t) +\
                A2 * math.sin(t * f2*math.pi/180 + p2) * math.exp(-1* d2* t)
        start_y = 200+ A3 * math.sin(t * f3*math.pi/180 +p3) * math.exp(-1* d3* t) +\
                A4 * math.sin(t * f4 * math.pi/180 + p4) * math.exp(-1* d4* t)

        end_x = 300+ A1 * math.sin((t+space) * f1 * math.pi/180 + p1) * math.exp(-1* d1* (t+space)) +\
                A2 * math.sin((t+space) * f2 * math.pi/180 + p2) * math.exp(-1* d2* (t+space))
        end_y = 200+ A3 * math.sin((t+space) * f3*math.pi/180 + p3) * math.exp(-1* d3* (t+space)) +\
                A4 * math.sin((t+space) * f4 * math.pi/180 + p4) * math.exp(-1* d4* (t+space))
        t += space
        pygame.draw.line(screen, color, (start_x,start_y), (end_x, end_y),2)
        if t >= 10000:
            pygame.image.save(screen, fname)
            exit()
        pygame.display.update()

#这个程序主要比上一个添加了serial的功能，可以控制硬件
import pygame
import serial
import math
from pygame.locals import *
from sys import exit
import random

#pygame屏幕设置与绘图板的实际尺寸（单位：mm）
screen_width = 1000
screen_height = 1000
color = (0, 0, 0)
board_length = 595
board_height = 200
addtional_height = 20
step_length = 0.628

#参数设置（这里全部用随机数了）
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

#serail相关设定
ser = serial.Serial('com3', 57600)
def ready():
    while True:
        m = ser.read()
        if m == b'R':
            m = ser.read(4)
            if m == b'EADY':
                return True

#pygame屏幕尺寸与实际尺寸的换算，可以合并成一个函数
def trans_left(a, b):
    x_b = board_length/2 + (a - screen_width/2)/5
    y_b = board_height + addtional_height + (b - screen_height/2)/5
    step_left = int(math.sqrt(math.pow(x_b, 2) + math.pow(y_b , 2))/ step_length)
    return step_left

def trans_right(a, b):
    x_b = board_length/2 - (a - screen_width/2)/5
    y_b = board_height + addtional_height + (b - screen_height/2)/5
    step_right = int(math.sqrt(math.pow(x_b, 2) + math.pow(y_b , 2))/ step_length)
    return step_right


pygame.init()

fname = 'DL' +str(A1) +'-' +str(A2)+'-' +str(A3)+'-' +str(A4)+'-'\
        +str(f1)[:3]+'-' +str(f2)[:3]+'-' +str(f3)[:3]+'-' +str(f4)[:3]+'-' \
        +str(d1)[:6]+'-' +str(d2)[:6]+'-' +str(d3)[:6]+'-' +str(d4)[:6]+'-' \
        +str(p1)[:3]+'-' +str(p2)[:3]+'-' +str(p3)[:3]+'-' +str(p4)[:3]+'-' \
        +str(space) + '.png'
print(fname)
my_font=pygame.font.SysFont('arial',15)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Homonograph Drawing Full')




t = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((255, 255, 255))

    step_left = trans_left(screen_width/2, screen_height/2)
    step_right = trans_right(screen_width/2, screen_height/2)
    message = 'C09' + ',' + str(step_left)+ ',' + str(step_right) + ',END\n'
    if ready():
        ser.write(message.encode('utf-8'))

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

        if ready():
            step_left = trans_left(end_x, end_y)
            step_right = trans_right(end_x, end_y)
            message = 'C01' + ',' + str(step_left)+ ',' + str(step_right) + ',END\n'
            ser.write(message.encode('utf-8'))
        
        
        pygame.draw.line(screen, color, (start_x,start_y), (end_x, end_y),2)
        if t >= 10000:
            pygame.image.save(screen, fname)
            exit()
        text_screen=my_font.render(fname, True, (255, 0, 0))
        screen.blit(text_screen, (50,50))#保存截图
        pygame.display.update()

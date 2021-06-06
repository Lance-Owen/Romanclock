"""
# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 0025 20:45
# @Author  : 源来很巧
# @FileName: 罗马钟5.py
# @Software: PyCharm
# @Blog    ：https://blog.csdn.net/qq_44793283
"""
from datetime import datetime,date,time
from pygame.locals import QUIT
from sys import exit
import pygame.freetype
import math
pygame.init()#初始化init()及设置
size=width,height=800,800
black=0,0,0
screen=pygame.display.set_mode(size)#窗口大小
pygame.display.set_caption("罗马时钟")#窗口名字
fps=100
font = pygame.font.SysFont("kaiti", 20)  # 30:font size
f1=pygame.freetype.Font('C:\Windows\Fonts\simkai.ttf',size=45)
fclock=pygame.time.Clock()#创建一个Clock对象用于操作时间

while True:
    t=datetime.today()
    # print(t.microsecond)
    screen.fill((t.hour*(255/24), t.minute*(255/60), t.second*(255/60)))    #t.hour*(255/24), t.minute*(255/60), t.second*(255/60)
    f1.render_to(screen, [358, 380], str(t.year)+'年', fgcolor=(255,255,255), bgcolor=None)
    # print(t)

    y1 = [str(i)+'月' for i in range(t.month, 13)]
    y2 = [str(i)+'月' for i in range(1, t.month)]
    y1.extend(y2)
    for i in range(0, 12):
        text = font.render(str(y1[i]), True, (255, 255, 255), 1)
        new_text = pygame.transform.rotozoom(text, 360-30*i, 1)
        screen.blit(new_text,
                    (400 + 100 * math.cos((2 * math.pi / 12) * i), 390 + 100 * math.sin((2 * math.pi / 12) * i)))
    # text = font.render("月", True, (255, 255, 255), 1)
    # new_text = pygame.transform.rotozoom(text, 0, 1)
    # screen.blit(new_text, (525, 390))

    d1 = [str(i)+'日' for i in range(t.day, 32)]
    d2 = [str(i)+'日' for i in range(1, t.day)]
    d1.extend(d2)
    for i in range(0, 31):
        text = font.render(str(d1[i]), True, (255, 255, 255), 1)
        new_text = pygame.transform.rotozoom(text, 360-(360/31)*i, 1)
        screen.blit(new_text,
                    (400 + 150 * math.cos((2 * math.pi / 31) * i), 390 + 150 * math.sin((2 * math.pi / 31) * i)))
    # text = font.render("日", True, (255, 255, 255), 1)
    # new_text = pygame.transform.rotozoom(text, 0, 1)
    # screen.blit(new_text, (575, 390))

    h1 = [str(i)+'时' for i in range(t.hour, 24)]
    h2 = [str(i)+'时' for i in range(0, t.hour)]
    h1.extend(h2)
    for i in range(0,24):
        text = font.render(str(h1[i]), True, (255, 255, 255), 1)
        new_text = pygame.transform.rotozoom(text, 360-15*i, 1)
        screen.blit(new_text, (400 + 200*math.cos((2*math.pi/24) * i), 390 + 200*math.sin((2*math.pi/24) * i)))
    # text = font.render("时", True, (255, 255, 255), 1)
    # new_text = pygame.transform.rotozoom(text, 0, 1)
    # screen.blit(new_text, (625, 390))

    m1 = [str(i)+'分' for i in range(t.minute, 60)]
    m2 = [str(i)+'分' for i in range(0, t.minute)]
    m1.extend(m2)
    for i in range(0, 60):
        text = font.render(str(m1[i]), True, (255, 255, 255), 1)
        new_text = pygame.transform.rotozoom(text, 360-6*i, 1)
        screen.blit(new_text, (400 + 250 * math.cos((2*math.pi/60) * i), 390 + 250 * math.sin((2*math.pi/60) * i)))
    # text = font.render("分", True, (255, 255, 255), 1)
    # new_text = pygame.transform.rotozoom(text, 0, 1)
    # screen.blit(new_text, (675, 390))

    s1 = [str(i)+"秒" for i in range(t.second, 60)]
    s2 = [str(i)+"秒" for i in range(0, t.second)]
    s1.extend(s2)
    for i in range(0, 60):
        text = font.render(str(s1[i]), True, (255, 255, 255), 1)
        new_text = pygame.transform.rotozoom(text, 360 - 6 * i, 1)
        screen.blit(new_text, (400 + 300 * math.cos((2*math.pi/60) * i), 390 + 300 * math.sin((2*math.pi/60) * i)))

    # text = font.render("秒", True, (255, 255, 255), 1)
    # new_text = pygame.transform.rotozoom(text, 0, 1)
    # screen.blit(new_text, (725, 390))

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()
    fclock.tick(fps)  # 窗口刷新速度，每秒次


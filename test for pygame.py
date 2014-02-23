#-*- coding:utf-8 -*-
import pygame
from sys import exit
pygame.init()
screen=pygame.display.set_mode((1366,768),0,32)
pygame.display.set_caption('hello,world!')
background=pygame.image.load('Wudipohuaiwang11.jpg').convert()
plane=pygame.image.load('1104131.gif').convert()
#加载飞机图像
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        screen.blit(background,(0,0))
        x,y=pygame.mouse.get_pos()
        #获取鼠标位置
        x-=plane.get_width()/2
        y-=plane.get_height()/2
        #计算飞机的左上角位置
        screen.blit(plane,(x,y))
        #把飞机画到屏幕上
        pygame.display.update()

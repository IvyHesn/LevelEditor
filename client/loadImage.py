import pygame
from pygame.locals import *
from readXML import *
from config import *

# 屏幕界面
screen_size = (screen_width, screen_height) = (1570, 649)
screen = pygame.display.set_mode(screen_size)

# 底层
bg_board = pygame.image.load("res/scene/bg_board.png")
bg_ele = pygame.image.load("res/scene/bg_ele.png")
chooseframe = pygame.image.load("res/scene/chooseframe.png")
bg_board_rect = [130, 0, bg_board.get_width(), bg_board.get_height()]
bg_ele_rect = [726, 0, bg_ele.get_width(), bg_ele.get_height()]


# 元素


def getPic(ele, path='res/element/'):
    '''根据elementID和路径，获取ele对应的图片'''
    if ele != None:
        pic = pygame.image.load(path + str(ele) + '.png')
    if ele == None:
        pic = pygame.image.load(path + '999' + '.png')
    return pic


def getChoose_ele(iX, iY):
    '''输入点选的格子
    返回点选到的元素'''
    choose_ele = grid_ele[iY][iX]
    return choose_ele


def getChooseArea(posX, posY):
    '''根据坐标判断处于哪个区域'''
    if posX >= bg_ele_rect[0]:  # 点选的是元素区域
        choose_area = 3
        return choose_area
    if bg_board_rect[0] <= posX < bg_ele_rect[0]:  # 点选的是盘面区域
        choose_area = 2
        return choose_area
    if posX < 65:  # 点选的是翻页区域
        pass


def Index_to_iXY(i):
    iX, iY = i % 9, i // 9
    return iX, iY


def Index_to_GridXY_board(i):
    '''根据index获取格子的坐标(盘面区域)'''
    gridX = i % 9 * 65 + bg_board_rect[0]
    gridY = i // 9 * 65 + bg_board_rect[1]
    return gridX, gridY


def Index_to_GridXY_ele(i):
    '''根据index获取格子的坐标(元素区域)'''
    gridX = i % 13 * 65 + bg_ele_rect[0]
    gridY = i // 13 * 65 + bg_ele_rect[1]
    return gridX, gridY

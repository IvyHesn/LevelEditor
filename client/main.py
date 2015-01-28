# 1 - Import library
import pygame
from pygame.locals import *
from loadImage import *
from config import *
import profile

pygame.init()
pygame.display.set_caption('LevelEditor!')

while 1:
    screen.fill((255, 255, 255))
    screen.blit(bg_board, bg_board_rect[0:2])
    screen.blit(bg_ele, bg_ele_rect[0:2])
    # 绘制盘面区域
    for eachlayer in range(0, 10):
        for y in range(0, 9):
            for x in range(0, 9):
                gridX, gridY = Index_to_GridXY_board(x + 9 * y)
                screen.blit(
                    getPic(level_ele[y][x][eachlayer]), (gridX, gridY))
    # 绘制元素选择区域
    for y in range(0, len(grid_ele)):
        for x in range(0, len(grid_ele[0])):
            gridX, gridY = Index_to_GridXY_ele(x + 13 * y)
            screen.blit(getPic(grid_ele[y][x]), (gridX, gridY))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            choose_area = getChooseArea(posX, posY)
            if choose_area == 3:  # 点选的是元素区域
                ele_iX = (posX - bg_ele_rect[0]) // 65
                ele_iY = (posY - bg_ele_rect[1]) // 65
                chooseframe_xy = (
                    Index_to_GridXY_ele(ele_iX + 13 * ele_iY))
                choose_ele = getChoose_ele(ele_iX, ele_iY)
            if choose_area == 2:  # 点选的是盘面区域
                board_iX = (posX - bg_board_rect[0]) // 65
                board_iY = (posY - bg_board_rect[1]) // 65
                board_gridX, board_gridY = Index_to_GridXY_board(
                    board_iX + 9 * board_iY)
                if choose_ele != None:
                    if level_ele[board_iY][board_iX][ele_layer['%s' % (choose_ele)]] == choose_ele:
                        level_ele[board_iY][board_iX][
                            ele_layer['%s' % (choose_ele)]] = None
                        dirty_rects.append(
                            (board_gridX, board_gridY, 65, 65))
                    else:
                        level_ele[board_iY][board_iX][
                            ele_layer['%s' % (choose_ele)]] = choose_ele
                        dirty_rects.append(
                            (board_gridX, board_gridY, 65, 65))
    if chooseframe_xy != (0, 0):
        screen.blit(chooseframe, chooseframe_xy)
        dirty_rects.append(chooseframe_xy + (65, 65))
    pygame.display.update(dirty_rects)
    # pygame.display.update()
    dirty_rects = []

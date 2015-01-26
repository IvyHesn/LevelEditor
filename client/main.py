# 1 - Import library
import pygame
from pygame.locals import *
from loadImage import *
from config import *

pygame.init()
pygame.display.set_caption('LevelEditor!')

while 1:
    screen.fill((255, 255, 255))
    screen.blit(bg_board, bg_board_rect[0:2])
    screen.blit(bg_ele, bg_ele_rect[0:2])
    # pygame.display.flip()
    # 绘制盘面区域
    for eachlayer in range(0, 10):
        for y in range(0, 9):
            for x in range(0, 9):
                gridX, gridY = Index_to_GridXY2(x + 9 * y)
                screen.blit(getPic(level_ele[y][x][eachlayer]), (gridX, gridY))
    # 绘制元素选择区域
    for y in range(0, len(grid_ele)):
        for x in range(0, len(grid_ele[0])):
            gridX, gridY = Index_to_GridXY3(x + 13 * y)
            screen.blit(getPic(grid_ele[y][x]), (gridX, gridY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            getChooseArea(posX, posY)
            if choose_area == 3:  # 点选的是元素区域
                ele_iX = (posX - bg_ele_rect[0]) // 65
                ele_iY = (posY - bg_ele_rect[1]) // 65
                choose_ele_grid = [ele_iX, ele_iY]
                getChoose_ele(choose_ele_grid)
            if choose_area == 2:  # 点选的是盘面区域
                board_iX = (posX - bg_board_rect[0]) // 65
                board_iY = (posY - bg_board_rect[1]) // 65
                choose_board = [board_iX, board_iY]
                if choose_ele != None:
                    nodelist = find_nodes(
                        tree_lc, './level[%s]/grid[%s]/basic' % (levelId, board_iX + 9 * board_iY))
                    change_node_properties(
                        nodelist, kv_map['%s'], False % (choose_ele))

    pygame.display.update()

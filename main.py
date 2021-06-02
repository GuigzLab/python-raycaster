import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing

pygame.init()
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
pygame.display.set_caption('Raycaster')
icon = pygame.image.load('./img/icon.png')
pygame.display.set_icon(icon)
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)



    pygame.display.flip()
    clock.tick(FPS)
    # print(clock.get_fps())
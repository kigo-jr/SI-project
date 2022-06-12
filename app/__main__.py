import pygame
from pygame.surface import Surface
from app.functions_and_structures.grid import Grid
from app.functions_and_structures.window import Window

if __name__ == "__main__":

    #  init SDL
    pygame.init()

    grid = Grid(40, 30)
    window = Window(grid)
    window.main_loop()

import pygame
from pygame.surface import Surface
from app.functions_and_structures.grid import Grid
from app.functions_and_structures.window import Window

if __name__ == "__main__":

    #  init SDL
    pygame.init()

    #  screen size
    WIDTH, HEIGHT = 800, 600

    #  window initialization

    grid = Grid()

    window = Window(grid)
    window.draw()
    window.main_loop()

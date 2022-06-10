import pygame
from pygame.surface import Surface
from app.functions_and_structures.grid import Grid

if __name__ == "__main__":

    #  init SDL
    pygame.init()

    #  screen size
    WIDTH, HEIGHT = 800, 600

    #  window initialization
    window: Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Search algorithms visualization")

    run: bool = True

    #  main loop
    while run:
        # event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

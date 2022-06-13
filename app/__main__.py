import pygame
from app.functions_and_structures.grid import Grid
from app.functions_and_structures.window import Window

if __name__ == "__main__":

    #  init SDL
    pygame.init()
    width = int(input("Enter width of the maze: "))
    height = int(input("Enter height of the maze: "))
    grid = Grid(80, 60)
    window = Window(grid)
    window.main_loop()

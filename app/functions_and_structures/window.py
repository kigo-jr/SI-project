from cmath import exp
from telnetlib import RCP
from typing import Tuple
from pygame.surface import Surface
from pygame.rect import Rect
import pygame
from app.functions_and_structures.grid import Grid

class Window:

    colours = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "purple": (128, 0, 128),
        "orange": (255, 168, 0),
        "gray": (128, 128, 128),
        "turquoise": (64, 224, 208)
    }

    def __init__(self, grid: Grid, width: int = 800, height: int = 600, grid_width: float = .7) -> None:
        self.grid_width = grid_width
        self.width = width
        self.height = height
        self.grid = grid
        self.surface = pygame.display.set_mode((self.width, self.height))

    @property
    def width(self) -> int:
        """Width of the window."""
        return self.__width

    @width.setter
    def width(self, width: int) -> None:
        if isinstance(width, int) and width > 0:
            self.__width = width
        else:
            raise Exception(f"Width must be a non-negative integer\nProvided value: {width}.")

    @property
    def height(self) -> int:
        """Height of the window."""
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        if isinstance(height, int) and height > 0:
            self.__height = height
        else:
            raise Exception(f"Height must be a non-negative integer\nProvided value: {height}.")

    @property
    def grid(self) -> Grid:
        """Object representing a grid of cells."""
        return self.__grid

    @grid.setter
    def grid(self, grid: Grid) -> None:
        if isinstance(grid, Grid):
            self.__grid = grid
        else:
            raise Exception(f"Grid field must of type of Grid\nProvided value {grid} (of type: {type(grid)}.")

    @property
    def grid_width(self) -> float:
        """Percentage of horizontal space that grid will take up to in window."""
        return self.__grid_width

    @grid_width.setter
    def grid_width(self, grid_width: float) -> None:
        if isinstance(grid_width, float) and grid_width > 0 and grid_width < 1:
            self.__grid_width = grid_width
        else:
            raise Exception(f"Grid width must be a value between 0 and 1\nProvidev value {grid_width}.")

    @property
    def surface(self) -> Surface:
        """Pygame window object."""
        return self.__surface


    @surface.setter
    def surface(self, surface: Surface) -> None:
        if isinstance(surface, Surface):
            self.__surface = surface
        else:
            raise Exception(f"Surface must be of type Surface!\nProvided value of type {type(surface)}.")

    @property
    def cell_size(self) -> Tuple[int, int]:
        cell_width: int = self.render_grid_width // self.grid.width
        cell_height: int = self.height // self.grid.height
        if cell_height == 0 or cell_width == 0:
            raise Exception(f"Whoopsie!")
        return (cell_width, cell_height)

    @property
    def render_grid_width(self) -> int:
        return int(self.grid_width * self.width)

    @property
    def render_toolbox_width(self) -> int:
        return self.width - self.render_grid_width

    def node_position_to_rectangle(self, x: int, y: int) -> Rect:
        return Rect(x * self.cell_size[0], y * self.cell_size[1], self.cell_size[0], self.cell_size[1])

    def draw(self):
        self.surface.fill(Window.colours["white"], Rect(0, 0, self.render_grid_width, self.height))
        self.surface.fill(Window.colours["gray"], Rect(self.render_grid_width, 0, self.render_toolbox_width, self.height))
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                pygame.draw.rect(self.surface, self.grid.grid[y][x].colour,
                self.node_position_to_rectangle(x, y))

        for x in range(self.grid.width + 1):
            pygame.draw.line(self.surface, Window.colours["black"], (x*self.cell_size[0], 0), (x*self.cell_size[0], self.height))

        for y in range(self.grid.height):
            pygame.draw.line(self.surface, Window.colours["black"], (0, y*self.cell_size[1]), (self.render_grid_width, y*self.cell_size[1]))

        pygame.display.update()

    def main_loop(self):
        # TODO: implement event handling and stuff

        run: bool = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

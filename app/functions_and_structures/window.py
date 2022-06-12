import imp
from typing import Tuple
from pygame.surface import Surface
from pygame.rect import Rect
import pygame
from app.functions_and_structures.grid import Grid
from app.functions_and_structures.algorithms.A_star import a_star
from app.functions_and_structures.algorithms.BFS import search as bfs
from app.functions_and_structures.algorithms.DFS import search as dfs
from app.functions_and_structures.algorithms.Dijkstra import search as dijkstra

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

    algorithms = ["DFS", "BFS", "DIJKSTRA", "A_STAR"]

    def __init__(self, grid: Grid, width: int = 800, height: int = 600, grid_width: float = .8) -> None:
        self.grid_width = grid_width
        self.width = width
        self.height = height
        self.grid = grid
        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("SUS")
        self.algorithm = Window.algorithms[0]


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
    def algorithm(self) -> str:
        return self.__algorithm

    @algorithm.setter
    def algorithm(self, algorithm: str) -> None:
        self.__algorithm = algorithm

    def set_next_algorithm(self) -> None:
        algorithm_index = Window.algorithms.index(self.algorithm)
        self.algorithm = Window.algorithms[(algorithm_index + 1) % len(Window.algorithms)]
        return

    def set_previous_algorithm(self) -> None:
        algorithm_index = Window.algorithms.index(self.algorithm)
        self.algorithm = Window.algorithms[(algorithm_index - 1) % len(Window.algorithms)]
        return

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

    def get_grid_position(self, pos) -> Tuple[int, int]:
        x, y = pos
        cell_width, cell_height = self.cell_size
        col = x // cell_width
        row = y // cell_height
        if col >= self.grid.width:
            return (None, None)
        else:
            return row, col


    def draw(self):
        # area for grid and toolbox
        self.surface.fill(Window.colours["white"])
        self.surface.fill(Window.colours["white"], Rect(0, 0, self.render_grid_width, self.height))
        self.surface.fill(Window.colours["gray"], Rect(self.render_grid_width, 0, self.render_toolbox_width, self.height))

        font = pygame.font.SysFont(None, 20)
        img = font.render("toolbox", True, Window.colours["black"])
        self.surface.blit(img, (self.render_grid_width + 5, 45))
        img = font.render("start", True, Window.colours["green" if self.grid.has_start else "red"])
        self.surface.blit(img, (self.render_grid_width + 5, 65))
        img = font.render("end", True, Window.colours["green" if self.grid.has_end else "red"])
        self.surface.blit(img, (self.render_grid_width + 5, 85))
        img = font.render("change algorithm: ([,])", True, Window.colours["black"])
        self.surface.blit(img, (self.render_grid_width + 5, 105))
        img = font.render(self.algorithm, True, Window.colours["purple"])
        self.surface.blit(img, (self.render_grid_width + 5, 125))

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
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_grid_position(pos)
                    if row is None and col is None:
                        pass
                    elif not self.grid.has_start and not self.grid.grid[row][col].end:
                        self.grid.grid[row][col].start = True
                    elif not self.grid.has_end and not self.grid.grid[row][col].start:
                        self.grid.grid[row][col].end = True
                    elif not self.grid.grid[row][col].barrier and not self.grid.grid[row][col].start and not self.grid.grid[row][col].end:
                        self.grid.grid[row][col].barrier = True

                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_grid_position(pos)
                    if row is None and col is None:
                        pass
                    else:
                        self.grid.grid[row][col].traversable = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and self.grid.has_start and self.grid.has_end:
                        self.grid.update_neighbours()
                        if self.algorithm == "DFS":
                            dfs(self, self.grid)
                        elif self.algorithm == "BFS":
                            bfs(self, self.grid)
                        elif self.algorithm == "DIJKSTRA":
                            dijkstra(self, self.grid)
                        elif self.algorithm == "A_STAR":
                            a_star(self, self.grid)

                    # TODO: implement changing an algorithm
                    if event.key == pygame.K_r:
                        self.grid.reset()
                    if event.key == pygame.K_s:
                        path = input("please enter path to save the maze: ")
                        self.grid.save(path)
                    if event.key == pygame.K_l:
                        path = input("please enter path to load the maze: ")
                        self.grid.load(path)
                    if event.key == pygame.K_LEFTBRACKET:
                        self.set_previous_algorithm()
                    if event.key == pygame.K_RIGHTBRACKET:
                        self.set_next_algorithm()


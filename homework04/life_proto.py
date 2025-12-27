import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cols = self.width // self.cell_size
        self.rows = self.height // self.cell_size
        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)
        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        self.grid = self.create_grid(randomize=True)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.draw_lines()
            self.draw_grid()
            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        grid: Grid = []
        for _ in range(self.cell_height):
            if randomize:
                row = [random.randint(0, 1) for _ in range(self.cell_width)]
            else:
                row = [0 for _ in range(self.cell_width)]
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                color = pygame.Color("green") if self.grid[y][x] == 1 else pygame.Color("white")
                rect = (
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.screen, color, rect)

    def get_neighbours(self, cell: Cell) -> Cells:
        x, y = cell
        neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x, y) != (x + i, y + j):
                    new_x, new_y = x + i, y + j
                    if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                        neighbours.append(self.grid[new_x][new_y])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = self.create_grid(False)
        for x in range(0, self.cell_height):
            for y in range(0, self.cell_width):
                neighbours = self.get_neighbours((x, y))

                if self.grid[x][y] and 2 <= sum(neighbours) <= 3:
                    new_grid[x][y] = 1
                elif not self.grid[x][y] and sum(neighbours) == 3:
                    new_grid[x][y] = 1
        return new_grid

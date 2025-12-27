import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid: Grid = []

        for _ in range(self.rows):
            if randomize:
                row = [random.randint(0, 1) for _ in range(self.cols)]
            else:
                row = [0 for _ in range(self.cols)]
            grid.append(row)

        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        x, y = cell
        neighbours = []

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                nx, ny = x + dx, y + dy

                if 0 <= nx < self.rows and 0 <= ny < self.cols:
                    neighbours.append(self.curr_generation[nx][ny])

        return neighbours

    def get_next_generation(self) -> Grid:
        new_grid = self.create_grid()

        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = self.get_neighbours((i, j))
                alive = self.curr_generation[i][j]
                count = sum(neighbours)

                if alive == 1 and count in (2, 3):
                    new_grid[i][j] = 1
                elif alive == 0 and count == 3:
                    new_grid[i][j] = 1
                else:
                    new_grid[i][j] = 0

        return new_grid

    def step(self) -> None:
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        return self.generations > self.max_generations

    @property
    def is_changing(self) -> bool:
        return self.curr_generation != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        with open(filename, "r") as f:
            lines = [line.strip() for line in f.readlines()]

        rows = len(lines)
        cols = len(lines[0])

        life = GameOfLife((rows, cols), randomize=False)
        life.curr_generation = [[int(char) for char in line] for line in lines]
        life.prev_generation = life.create_grid()
        life.generations = 1

        return life

    def save(self, filename: pathlib.Path) -> None:
        with open(filename, "w") as f:
            for row in self.curr_generation:
                f.write("".join(map(str, row)) + "\n")

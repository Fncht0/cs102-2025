import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        rows, cols = self.life.rows, self.life.cols

        for x in range(cols + 2):
            screen.addch(0, x, "#")
            screen.addch(rows + 1, x, "#")

        for y in range(1, rows + 1):
            screen.addch(y, 0, "#")
            screen.addch(y, cols + 1, "#")

    def draw_grid(self, screen) -> None:
        for i in range(self.life.rows):
            for j in range(self.life.cols):
                char = "█" if self.life.curr_generation[i][j] == 1 else " "
                screen.addch(i + 1, j + 1, char)

    def run(self) -> None:
        screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        screen.nodelay(True)
        screen.keypad(True)

        try:
            while self.life.is_changing and not self.life.is_max_generations_exceeded:
                screen.clear()
                self.draw_borders(screen)
                self.draw_grid(screen)
                screen.refresh()

                key = screen.getch()
                if key == ord("q"):
                    break

                self.life.step()
                curses.napms(100)

        finally:
            curses.nocbreak()
            screen.keypad(False)
            curses.echo()
            curses.endwin()


if __name__ == "__main__":
    game = GameOfLife(size=(20, 20), randomize=True)
    console = Console(life=game)
    console.run()

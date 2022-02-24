import random
from PIL import Image, ImageDraw
from Cell import Cell


class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = []

    def get_grid(self):
        return self.grid

    def generate_maze_sidewinder(self):
        # start_cell - это значение, отслеживающее стартовую ячейку в коридоре и обеспечивает случайный верез наверх
        # когда мы вырезаем путь наверх, значение start_cell изменяется, это позволяет избегать петель
        for row in range(self.height):
            start_cell = 0
            new_line = []
            for c in range(self.width):
                new_line.append(Cell())
            self.grid.append(new_line)
            for col in range(self.width):
                if row > 0 and (col+1 == self.width or random.random() > 0.5):
                    cell = start_cell + random.randint(0, col - start_cell)
                    self.grid[row-1][cell].bot = self.grid[row][cell]
                    self.grid[row][cell].top = self.grid[row-1][cell]
                    start_cell = col + 1
                elif col+1 < self.width:
                    self.grid[row][col].right = self.grid[row][col+1]
                    self.grid[row][col+1].left = self.grid[row][col]

    # Инициализация для алгоритма Hunt and Kill
    def initialization_hunt_and_kill(self):
        for h in range(self.height):
            line = []
            for w in range(self.width):
                line.append(Cell())
            self.grid.append(line)

    # Выбор случайного направления
    def direction_choice(self, x, y):
        direction = []
        if y > 0 and self.grid[y - 1][x].is_visited == 0:
            direction.append(0)
        if y < self.height - 1 and self.grid[y + 1][x].is_visited == 0:
            direction.append(1)
        if x > 0 and self.grid[y][x - 1].is_visited == 0:
            direction.append(2)
        if x < self.width - 1 and self.grid[y][x + 1].is_visited == 0:
            direction.append(3)
        size = len(direction)
        if size > 0:
            return direction[random.randint(0, size - 1)]
        else:
            return None

    # Функция, осуществляющая вырезание проходов в случайном направлении
    def kill(self, x, y):
        cell = self.grid[y][x]
        diff = self.direction_choice(x, y)
        while diff is not None:
            cell.is_visited = 1
            if diff == 0:
                y -= 1
                cell.top = self.grid[y][x]
                self.grid[y][x].bot = cell
            elif diff == 1:
                y += 1
                cell.bot = self.grid[y][x]
                self.grid[y][x].top = cell
            elif diff == 2:
                x -= 1
                cell.left = self.grid[y][x]
                self.grid[y][x].right = cell
            else:
                x += 1
                cell.right = self.grid[y][x]
                self.grid[y][x].left = cell

            cell = self.grid[y][x]
            diff = self.direction_choice(x, y)
        cell.is_visited = 1

    # Функция, осуществляющая поиск непосещенной ячейки рядом с посященной
    def hunt(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col].is_visited == 0:
                    if col > 0 and self.grid[row][col - 1].is_visited == 1:
                        self.grid[row][col].left = self.grid[row][col - 1]
                        self.grid[row][col - 1].right = self.grid[row][col]
                        return row, col
                    if row < self.height - 1 and self.grid[row + 1][col].is_visited == 1:
                        self.grid[row][col].bot = self.grid[row + 1][col]
                        self.grid[row + 1][col].top = self.grid[row][col]
                        return row, col
                    if col < self.width - 1 and self.grid[row][col + 1].is_visited == 1:
                        self.grid[row][col].right = self.grid[row][col + 1]
                        self.grid[row][col + 1].left = self.grid[row][col]
                        return row, col
                    if row > 0 and self.grid[row - 1][col].is_visited == 1:
                        self.grid[row][col].top = self.grid[row - 1][col]
                        self.grid[row - 1][col].bot = self.grid[row][col]
                        return row, col
        return None

    def generate_maze_hunt_and_kill(self):
        i = 0
        self.initialization_hunt_and_kill()
        fy = random.randint(0, self.height-1)
        fx = random.randint(0, self.width-1)
        self.kill(fx, fy)
        hunt = self.hunt()
        while hunt is not None:
            i += 1
            self.kill(hunt[1], hunt[0])
            hunt = self.hunt()

    # Функция, снимающая все посещения для того, чтобы можно было решить лабиринт, созданный алгоритмом Hunt and Kill
    def unvisit_all(self):
        for row in range(self.height):
            for col in range(self.width):
                self.grid[row][col].is_visited = 0

    # Функция для выбора следующего узла в solve
    def direction_choice_solve(self, cell):
        if cell.right is not None and cell.right.is_visited < 1:
            return cell.right
        if cell.bot is not None and cell.bot.is_visited < 1:
            return cell.bot
        if cell.left is not None and cell.left.is_visited < 1:
            return cell.left
        if cell.top is not None and cell.top.is_visited < 1:
            return cell.top
        return None

    # Функция, осуществляющая поиск выхода
    def solve(self):
        if self.grid[0][0].is_visited == 1:
            self.unvisit_all()
        stack = []
        s_cell = self.grid[0][0]
        f_cell = self.grid[self.height-1][self.width-1]
        curr_cell = s_cell
        while curr_cell != f_cell:
            curr_cell.is_visited += 1
            neb_cell = self.direction_choice_solve(curr_cell)
            if neb_cell is not None:
                stack.append(curr_cell)
                curr_cell = neb_cell
            elif len(stack) > 0:
                curr_cell.is_visited += 1
                curr_cell = stack.pop()
                curr_cell.is_visited -= 1
            else:
                return False
        curr_cell.is_visited += 1
        return curr_cell == f_cell

    # Функция-проверка, реализовання на основе solve, но проходащая через все клетки
    # Проверяет отсутствие закрытых областей и циклов, если все точки оказались посещены дважды, проверка прошла
    def check(self):
        if self.grid[0][0].is_visited == 1:
            self.unvisit_all()
        stack = []
        s_cell = self.grid[0][0]
        curr_cell = s_cell
        while True:
            curr_cell.is_visited += 1
            neb_cell = self.direction_choice_solve(curr_cell)
            if neb_cell is not None:
                stack.append(curr_cell)
                curr_cell = neb_cell
            elif len(stack) > 0:
                curr_cell.is_visited += 1
                curr_cell = stack.pop()
                curr_cell.is_visited -= 1
            else:
                break
        curr_cell.is_visited += 1
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j].is_visited != 2:
                    return False
        return True

    # Функция, создающая изображение лабиринта
    def draw_maze(self):
        height = self.height
        width = self.width
        image = Image.new('RGBA', (5 + width * 5, 5 + height * 5), (255, 255, 255, 255))
        draw = ImageDraw.Draw(image)
        sp = 2
        draw.line(((7, sp), (sp + width * 5, sp)), fill="black", width=1)
        draw.line(((sp, sp), (sp, sp + height * 5)), fill="black", width=1)
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                cell = self.grid[row][col]
                if cell.right is not None and cell.bot is not None:
                    pass
                elif cell.right is not None:
                    draw.line(((sp + col * 5, sp + row * 5 + 5), (sp + col * 5 + 5, sp + row * 5 + 5)), fill="black",
                              width=1)
                elif cell.bot is not None:
                    draw.line(((sp + col * 5 + 5, sp + row * 5), (sp + col * 5 + 5, sp + row * 5 + 5)), fill="black",
                              width=1)
                else:
                    draw.line(((sp + col * 5, sp + row * 5 + 5), (sp + col * 5 + 5, sp + row * 5 + 5)), fill="black",
                              width=1)
                    draw.line(((sp + col * 5 + 5, sp + row * 5), (sp + col * 5 + 5, sp + row * 5 + 5)), fill="black",
                              width=1)

        draw.line(((sp + width * 5 - 4, sp + height * 5), (sp + width * 5 - 1, sp + height * 5)), fill="white", width=1)
        del draw
        image.save("Maze.png")

    # Отрисовка маршрута решения лабиринта функцией solve
    def solve_draw(self):
        try:
            image = Image.open("Maze.png")
            draw = ImageDraw.Draw(image)
            self.solve()
            for row in range(self.height):
                for col in range(self.width):
                    cell = self.grid[row][col]
                    if cell.is_visited == 1:
                        draw.point((2 + col * 5 + 2, 4 + row * 5), fill="blue")
                    # elif cell.is_visited == 2:
                        # draw.point((2 + col * 5 + 2, 4 + row * 5), fill="red")
            image.save("Solve_Maze.png")
        except FileNotFoundError:
            print("Лабиринт не создан")


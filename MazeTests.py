# Модуль для тестирования класса Maze
from Maze import Maze
from Cell import Cell


class MazeTests:
    def _test_cells_visited(self, maze):
        for line in maze.get_grid():
            for cell in line:
                if cell.is_visited != 0:
                    return False
        return True

    def _test_generation_maze(self, maze):
        for line in maze.get_grid():
            for cell in line:
                if cell.left is None and cell.right is None and cell.top is None and cell.bot is None:
                    return False
        return True

    def _visit_all(self, maze):
        grid = maze.get_grid()
        for line in grid:
            for cell in line:
                cell.is_visited = 1
        
    def _test_generate_hunt_and_kill(self, width, height):
        maze = Maze (width, height)
        maze.generate_maze_hunt_and_kill()
        return self._test_generation_maze(maze)
 
    def _test_generate_sidewinder(self, width, height):
        maze = Maze (width, height)
        maze.generate_maze_sidewinder()
        return self._test_generation_maze(maze)

    def _test_unvisited_all(self, width, height):
        maze = Maze(width, height)
        maze.generate_maze_hunt_and_kill()
        maze.unvisit_all()
        return self._test_cells_visited(maze)

    def _test_initialization_hunt_and_kill(self, width, height):
        maze = Maze(width, height)
        maze.initialization_hunt_and_kill()
        for line in maze.get_grid():
            for cell in line:
                if not isinstance(cell, Cell):
                    return False
        return True

    def _create_right_maze(self):
        maze = Maze(4, 4)
        grid = maze.get_grid()
        for h in range(4):
            line = []
            for w in range(4):
                line.append(Cell())
            grid.append(line)
        grid[0][0].right = grid[0][1]
        grid[0][1].left = grid[0][0]
        grid[0][1].right = grid[0][2]
        grid[0][2].left = grid[0][1]
        grid[0][2].bot = grid[1][2]
        grid[1][2].top = grid[0][2]
        grid[1][2].right = grid[1][3]
        grid[1][3].left = grid[1][2]
        grid[1][3].top = grid[0][3]
        grid[0][3].bot = grid[1][3]
        grid[0][0].bot = grid[1][0]
        grid[1][0].top = grid[0][0]
        grid[1][0].right = grid[1][1]
        grid[1][1].left = grid[1][0]
        grid[1][1].bot = grid[2][1]
        grid[2][1].top = grid[1][1]
        grid[2][1].left = grid[2][0]
        grid[2][0].right = grid[2][1]
        grid[2][0].bot = grid[3][0]
        grid[3][0].top = grid[2][0]
        grid[3][0].right = grid[3][1]
        grid[3][1].left = grid[3][0]
        grid[3][1].right = grid[3][2]
        grid[3][2].left = grid[3][1]
        grid[3][2].right = grid[3][3]
        grid[3][3].left = grid[3][2]
        grid[3][3].top = grid[2][3]
        grid[2][3].bot = grid[3][3]
        grid[2][3].left = grid[2][2]
        grid[2][2].right = grid[2][3]
        return maze

    def _create_wrong_maze(self):
        maze = Maze(4, 4)
        grid = maze.get_grid()
        for h in range(4):
            line = []
            for w in range(4):
                line.append(Cell())
            grid.append(line)
        grid[0][0].right = grid[0][1]
        grid[0][1].left = grid[0][0]
        grid[0][1].right = grid[0][2]
        grid[0][2].left = grid[0][1]
        grid[0][2].bot = grid[1][2]
        grid[1][2].top = grid[0][2]
        grid[1][2].right = grid[1][3]
        grid[1][3].left = grid[1][2]
        grid[1][3].top = grid[0][3]
        grid[0][3].bot = grid[1][3]
        grid[0][0].bot = grid[1][0]
        grid[1][0].top = grid[0][0]
        grid[1][1].left = grid[1][0]
        grid[1][1].bot = grid[2][1]
        grid[2][1].top = grid[1][1]
        grid[2][1].left = grid[2][0]
        grid[2][0].right = grid[2][1]
        grid[2][0].bot = grid[3][0]
        grid[3][0].right = grid[3][1]
        grid[3][1].left = grid[3][0]
        grid[3][1].right = grid[3][2]
        grid[3][2].left = grid[3][1]
        grid[3][2].right = grid[3][3]
        grid[3][3].left = grid[3][2]
        grid[3][3].top = grid[2][3]
        grid[2][3].bot = grid[3][3]
        grid[2][3].left = grid[2][2]
        grid[2][2].right = grid[2][3]
        return maze
        
    def _test_solve_hunt_and_kill(self, height, width):
        maze = Maze(height, width)
        maze.generate_hunt_and_kill()
        if not self._test_generation_maze(maze):
            return False

    def test_hunt_1_1(self):
        maze = self._create_right_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        grid[1][1].is_visited = 0
        x, y = maze.hunt()
        if x == 1 and y == 1:
            return "Test hunt_1_1: Pass"
        return "Test hunt_1_1: Failed" 

    def test_hunt_none(self):
        maze = self._create_right_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        if maze.hunt() is None:
            return "Test hunt_none: Pass"
        return "Test hunt_none: Failed" 

    def test_direction_choice_0(self):
        maze = self._create_right_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        grid[0][0].is_visited = 0
        if maze.direction_choice(0, 1) == 0:
            return "Test direction_choice_0: Pass"
        return "Test direction_choice_0: Failed"

    def test_direction_choice_1(self):
        maze = self._create_right_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        grid[1][0].is_visited = 0
        if maze.direction_choice(0, 0) == 1:
            return "Test direction_choice_1: Pass"
        return "Test direction_choice_1: Failed"

    def test_direction_choice_2(self):
        maze = self._create_right_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        grid[0][0].is_visited = 0
        if maze.direction_choice(1, 0) == 2:
            return "Test direction_choice_2: Pass"
        return "Test direction_choice_2: Failed"

    def test_direction_choice_3(self):
        maze = self._create_right_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        grid[0][1].is_visited = 0
        if maze.direction_choice(0, 0) == 3:
            return "Test direction_choice_3: Pass"
        return "Test direction_choice_3: Failed"

    def test_direction_choice_none(self):
        maze = self._create_right_maze()
        self._visit_all(maze)
        if maze.direction_choice(0, 0) is None:
            return "Test direction_choice_none: Pass"
        return "Test direction_choice_none: Failed"

    def test_kill_3_1(self):
        maze = self._create_wrong_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        grid[2][3].is_visited = 0
        maze.kill(3, 1)
        if grid[1][3].bot == grid[2][3] and grid[2][3].top == grid[1][3]:
            return "Test kill_3_1: Pass"
        return "Test kill_3_1: Failed"

    def test_kill_0_1(self):
        maze = self._create_wrong_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        grid[1][1].is_visited = 0
        maze.kill(0, 1)
        if grid[1][0].right == grid[1][1] and grid[1][1].left == grid[1][0]:
           return "Test kill_0_1: Pass"
        return "Test kill_0_1: Failed"

    def test_direction_choice_solve_0_1(self):
        maze = self._create_wrong_maze()
        grid = maze.get_grid()
        if maze.direction_choice_solve(grid[0][0]) == grid[0][1]:
            return "Test direction_choice_solve_0_1: Pass"
        return "direction_choice_solve_0_1: Failed"

    def test_direction_choice_solve_none(self):
        maze = self._create_wrong_maze()
        self._visit_all(maze)
        grid = maze.get_grid()
        if maze.direction_choice_solve(grid[0][0]) is None:
            return "Test direction_choice_solve_node: Pass"
        return "Test direction_choice_solve_node: Failed"
    

    def test_solve_right(self):
        maze = self._create_right_maze()
        if maze.solve():
            return "Test solve right: Pass"
        return "Test solve right: Failed"

    def test_solve_wrong(self):
        maze = self._create_wrong_maze()
        if not maze.solve():
            return "Test solve wrong: Pass"
        return "Test solve wrong: Failed"        

    def test_initializaiton_hunt_and_kill_5_5(self):
        if self._test_initialization_hunt_and_kill(5, 5):
            return "Test initialization hunt_and_kill_5_5: Pass"
        return "Test initialization hunt_and_kill_5_5: Failed"

    def test_initializaiton_hunt_and_kill_10_5(self):
        if self._test_initialization_hunt_and_kill(10, 5):
            return "Test initialization hunt_and_kill_10_5: Pass"
        return "Test initialization hunt_and_kill_10_5: Failed"

    def test_initializaiton_hunt_and_kill_5_10(self):
        if self._test_initialization_hunt_and_kill(5, 10):
            return "Test initialization hunt_and_kill_5_10: Pass"
        return "Test initialization hunt_and_kill_5_10: Failed"

    def test_unvisited_all_5_5(self):
        if self._test_unvisited_all(5, 5):
            return "Test unvisited_all_5_5: Pass"
        return "Test unvisited_all_5_5: Failed"

    def test_unvisited_all_5_10(self):
        if self._test_unvisited_all(5, 10):
            return "Test unvisited_all_5_10: Pass"
        return "Test unvisited_all_5_10: Failed"

    def test_unvisited_all_10_5(self):
        if self._test_unvisited_all(10, 5):
            return "Test unvisited_all_10_5: Pass"
        return "Test unvisited_all_10_5: Failed"

    def test_generate_hunt_and_kill_5_5(self):
        if self._test_generate_hunt_and_kill(5, 5):
            return "Test generate_hunt_and_kill_5_5: Pass"
        return "Test generate_hunt_and_kill_5_5: Failed"

    def test_generate_hunt_and_kill_10_5(self):
        if self._test_generate_hunt_and_kill(10, 5):
            return "Test generate_hunt_and_kill_10_5: Pass"
        return "Test generate_hunt_and_kill_10_5: Failed"

    def test_generate_hunt_and_kill_5_10(self):
        if self._test_generate_hunt_and_kill(5, 10):
            return "Test generate_hunt_and_kill_5_10: Pass"
        return "Test generate_hunt_and_kill_5_10: Failed"

    def test_generate_sidewinder_5_5(self):
        if self._test_generate_sidewinder(5, 5):
            return "Test generate_sidewinder_5_5: Pass"
        return "Test generate_sidewinder_5_5: Failed"

    def test_generate_sidewinder_10_5(self):
        if self._test_generate_sidewinder(10, 5):
            return "Test generate_sidewinder_10_5: Pass"
        return "Test generate_sidewinder_10_5: Failed"

    def test_generate_sidewinder_5_10(self):
        if self._test_generate_sidewinder(5, 10):
            return "Test generate_sidewinder_5_10: Pass"
        return "Test generate_sidewinder_5_10: Failed"

        
maze_tests = MazeTests()
print(maze_tests.test_initializaiton_hunt_and_kill_5_5())
print(maze_tests.test_initializaiton_hunt_and_kill_5_10())
print(maze_tests.test_initializaiton_hunt_and_kill_10_5())

print(maze_tests.test_hunt_1_1())
print(maze_tests.test_hunt_none())

print(maze_tests.test_direction_choice_0())
print(maze_tests.test_direction_choice_1())
print(maze_tests.test_direction_choice_2())
print(maze_tests.test_direction_choice_3())
print(maze_tests.test_direction_choice_none())

print(maze_tests.test_kill_3_1())
print(maze_tests.test_kill_0_1())

print(maze_tests.test_generate_hunt_and_kill_5_5())
print(maze_tests.test_generate_hunt_and_kill_5_10())
print(maze_tests.test_generate_hunt_and_kill_10_5())

print(maze_tests.test_unvisited_all_5_5())
print(maze_tests.test_unvisited_all_5_10())
print(maze_tests.test_unvisited_all_10_5())

print(maze_tests.test_generate_sidewinder_5_5())
print(maze_tests.test_generate_sidewinder_5_10())
print(maze_tests.test_generate_sidewinder_10_5())

print(maze_tests.test_direction_choice_solve_0_1())
print(maze_tests.test_direction_choice_solve_none())

print(maze_tests.test_solve_right())
print(maze_tests.test_solve_wrong())
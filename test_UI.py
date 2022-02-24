from Maze import Maze


def test():
    for i in range(1, 50):
        for j in range(1, 50):
            m = Maze(i, j)
            m.generate_maze_eller()
            if m.check() is False:
                return False
            m = Maze(i, j)
            m.generate_maze_sidewinder()
            if m.check() is False:
                return False
            m = Maze(i, j)
            m.generate_maze_kruskal()
            if m.check() is False:
                return False
    for i in range(1, 25):
        for j in range(1, 25):
            m = Maze(i, j)
            m.generate_maze_hunt_and_kill()
            if m.check() is False:
                return False
    return True


print(test())

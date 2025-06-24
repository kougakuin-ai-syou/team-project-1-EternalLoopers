# maze_oop.py

class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.start = self.find_position("S")
        self.goal = self.find_position("G")
        self.path = []

    def find_position(self, symbol):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == symbol:
                    return (i, j)
        return None

    def is_valid(self, x, y):
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            return self.grid[x][y] != 1
        return False

    def is_goal(self, x, y):
        return self.grid[x][y] == "G"

    def explore(self, x, y, visited):
        if not self.is_valid(x, y) or (x, y) in visited:
            return False

        visited.append((x, y))

        if self.is_goal(x, y):
            self.path = visited.copy()
            return True

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            if self.explore(x + dx, y + dy, visited):
                return True

        visited.pop()
        return False

    def run(self):
        if self.start is None or self.goal is None:
            print("スタートまたはゴール地点が見つかりません。")
            return

        success = self.explore(self.start[0], self.start[1], [])

        if success:
            print("ゴールに到達しました！経路:")
            print(self.path)
        else:
            print("ゴールに到達できませんでした。")


def main():
    maze_map = [
        ["S", 0,  1,  0,  0],
        [1,  0,  1,  0,  1],
        [0,  0,  0,  0,  1],
        [0,  1,  1,  0,  0],
        [0,  0,  0,  1, "G"]
    ]

    maze = Maze(maze_map)
    maze.run()


if __name__ == "__main__":
    main()

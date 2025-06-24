# maze_func.py

# 迷路マップ（0：通路、1：壁、S：スタート、G：ゴール）
maze = [
    ["S", 0,  1,  0,  0],
    [1,  0,  1,  0,  1],
    [0,  0,  0,  0,  1],
    [0,  1,  1,  0,  0],
    [0,  0,  0,  1, "G"]
]

# スタート位置を探す
def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return (i, j)
    return None

# 現在位置がゴールか判定
def is_goal(pos):
    x, y = pos
    return maze[x][y] == "G"

# 移動可能かどうかを判定
def can_move(x, y):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        return maze[x][y] != 1
    return False

# 探索処理（シンプルな深さ優先探索）
def explore(x, y, path):
    if not can_move(x, y) or (x, y) in path:
        return False

    path.append((x, y))

    if is_goal((x, y)):
        return True

    # 上下左右に探索
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        if explore(x + dx, y + dy, path):
            return True

    path.pop()
    return False

# 実行用関数
def main():
    start = find_start(maze)
    if not start:
        print("スタート地点が見つかりません。")
        return

    path = []
    success = explore(start[0], start[1], path)

    if success:
        print("ゴールに到達しました！経路:")
        print(path)
    else:
        print("ゴールに到達できませんでした。")

if __name__ == "__main__":
    main()

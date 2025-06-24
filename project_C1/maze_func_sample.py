# maze_graphic_advanced.py

import matplotlib.pyplot as plt
import numpy as np

# 폰트 설정 (일본어 깨짐 방지)
plt.rcParams['font.family'] = 'MS Gothic'  # 또는 'Meiryo'로 변경 가능

# 수정된 20x20 미로 배열 ('S': 시작, 'G': 골, 0: 길, 1: 벽)
maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,'S',0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,'G',1]
]

player_pos = [1, 1]  # 시작 위치
rows, cols = len(maze), len(maze[0])

# 미로 그리기 함수
def draw_maze():
    color_map = {
        0: 1.0,
        1: 0.0,
        'S': 0.6,
        'G': 0.3
    }
    grid = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = color_map.get(maze[i][j], 1.0)
    ax.clear()
    ax.imshow(grid, cmap='gray')
    ax.scatter(player_pos[1], player_pos[0], c='red', s=200, edgecolors='black', label='プレイヤー')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("赤い点をゴールまで導こう！", fontsize=14)
    ax.legend(loc='upper right')
    plt.draw()

# 키 입력 처리 함수
def on_key(event):
    dx, dy = 0, 0
    if event.key == "up": dx = -1
    elif event.key == "down": dx = 1
    elif event.key == "left": dy = -1
    elif event.key == "right": dy = 1

    nx, ny = player_pos[0] + dx, player_pos[1] + dy
    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != 1:
        player_pos[0], player_pos[1] = nx, ny
        draw_maze()
    if maze[nx][ny] == 'G':
        print("🎉 ゴールに到達しました！")

fig, ax = plt.subplots(figsize=(8, 8))
draw_maze()
fig.canvas.mpl_connect("key_press_event", on_key)
plt.show()

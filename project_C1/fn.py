import tkinter as tk
import random

# === グローバル変数 ===
maze = [
    ["S", 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, "G"]
]

obstacles = [(2, 5), (6, 1), (7, 13), (4, 12), (3, 9)]
TILE_SIZE = 30
WIDTH = len(maze[0]) * TILE_SIZE
HEIGHT = len(maze) * TILE_SIZE

player_pos = (0, 0)
remaining_time = 60
game_over = False

# tkinter要素
root = None
canvas = None
timer_label = None

# === ロジック用関数 ===
def find_start():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return (i, j)
    return (0, 0)

def is_goal(x, y):
    return maze[x][y] == "G"

def can_move(x, y):
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        return maze[x][y] != 1 and (x, y) not in obstacles
    return False

# === 描画関数 ===
def draw_maze():
    canvas.delete("all")
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            x1, y1 = j * TILE_SIZE, i * TILE_SIZE
            x2, y2 = x1 + TILE_SIZE, y1 + TILE_SIZE
            val = maze[i][j]
            color = "white"
            if val == 1:
                color = "black"
            elif val == "S":
                color = "gray"
            elif val == "G":
                color = "lightblue"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    for ox, oy in obstacles:
        x1, y1 = oy * TILE_SIZE, ox * TILE_SIZE
        x2, y2 = x1 + TILE_SIZE, y1 + TILE_SIZE
        canvas.create_rectangle(x1, y1, x2, y2, fill="orange", outline="gray")

    px, py = player_pos
    cx1 = py * TILE_SIZE + 6
    cy1 = px * TILE_SIZE + 6
    cx2 = cx1 + TILE_SIZE - 12
    cy2 = cy1 + TILE_SIZE - 12
    canvas.create_oval(cx1, cy1, cx2, cy2, fill="red")

# === ゲームロジック ===
def on_key_press(event):
    global player_pos, game_over

    if game_over:
        return

    dx, dy = 0, 0
    if event.keysym == "Up": dx = -1
    elif event.keysym == "Down": dx = 1
    elif event.keysym == "Left": dy = -1
    elif event.keysym == "Right": dy = 1

    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy

    if (new_x, new_y) in obstacles:
        canvas.create_text(WIDTH//2, HEIGHT//2, text="障害物にぶつかった！", font=("Arial", 24), fill="red")
        game_over = True
        root.unbind("<KeyPress>")
        return

    if can_move(new_x, new_y):
        player_pos = (new_x, new_y)
        draw_maze()
        if is_goal(new_x, new_y):
            canvas.create_text(WIDTH//2, HEIGHT//2, text="ゴール成功！", font=("Arial", 24), fill="green")
            game_over = True
            root.unbind("<KeyPress>")

def update_timer():
    global remaining_time, game_over

    timer_label.config(text=f"制限時間: {remaining_time}")
    if remaining_time > 0 and not game_over:
        remaining_time -= 1
        root.after(1000, update_timer)
    elif not game_over:
        canvas.create_text(WIDTH//2, HEIGHT//2, text="時間切れ！", font=("Arial", 24), fill="red")
        game_over = True
        root.unbind("<KeyPress>")

def move_obstacles():
    global obstacles, game_over

    if game_over:
        return

    new_obstacles = []
    for x, y in obstacles:
        options = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        random.shuffle(options)
        for nx, ny in options:
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) != player_pos:
                new_obstacles.append((nx, ny))
                break
        else:
            new_obstacles.append((x, y))

    obstacles[:] = new_obstacles
    draw_maze()
    root.after(1500, move_obstacles)

# === 初期化・起動 ===
def main():
    global root, canvas, timer_label, player_pos
    root = tk.Tk()
    root.title("迷路ゲーム（関数だけ構成）")

    canvas_frame = tk.Frame(root)
    canvas_frame.pack()
    canvas_widget = tk.Canvas(canvas_frame, width=WIDTH, height=HEIGHT)
    canvas_widget.pack()
    timer = tk.Label(root, text="制限時間: 60", font=("Arial", 14))
    timer.pack()

    canvas_widget.focus_set()
    canvas_widget.bind("<KeyPress>", on_key_press)

    # グローバル登録
    globals()['canvas'] = canvas_widget
    globals()['timer_label'] = timer

    # ゲーム開始
    player_pos = find_start()
    draw_maze()
    update_timer()
    move_obstacles()

    root.mainloop()

if __name__ == "__main__":
    main()

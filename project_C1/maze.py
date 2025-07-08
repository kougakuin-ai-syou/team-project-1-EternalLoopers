# maze_graphical_game.py（Tkinterベースの視覚的迷路ゲーム + 複雑な障害物＆タイマー＋エフェクト）

import tkinter as tk
import random

# 迷路マップ（0：通路、1：壁、S：スタート、G：ゴール）
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

class MazeGame:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.timer_label = tk.Label(root, text="制限時間: 60", font=("Arial", 14))
        self.timer_label.pack()

        self.player_pos = self.find_start()
        self.remaining_time = 60
        self.root.bind("<KeyPress>", self.on_key_press)
        self.game_over = False
        self.draw_maze()
        self.update_timer()
        self.move_obstacles()

    def find_start(self):
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "S":
                    return (i, j)
        return (0, 0)

    def is_goal(self, x, y):
        return maze[x][y] == "G"

    def can_move(self, x, y):
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
            return maze[x][y] != 1 and (x, y) not in obstacles
        return False

    def draw_maze(self):
        self.canvas.delete("all")
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                x1 = j * TILE_SIZE
                y1 = i * TILE_SIZE
                x2 = x1 + TILE_SIZE
                y2 = y1 + TILE_SIZE
                val = maze[i][j]
                color = "white"
                if val == 1:
                    color = "black"
                elif val == "S":
                    color = "gray"
                elif val == "G":
                    color = "lightblue"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

        for ox, oy in obstacles:
            x1 = oy * TILE_SIZE
            y1 = ox * TILE_SIZE
            x2 = x1 + TILE_SIZE
            y2 = y1 + TILE_SIZE
            self.canvas.create_rectangle(x1, y1, x2, y2, fill="orange", outline="gray")

        px, py = self.player_pos
        cx1 = py * TILE_SIZE + 6
        cy1 = px * TILE_SIZE + 6
        cx2 = cx1 + TILE_SIZE - 12
        cy2 = cy1 + TILE_SIZE - 12
        self.canvas.create_oval(cx1, cy1, cx2, cy2, fill="red")

    def on_key_press(self, event):
        if self.game_over:
            return

        dx, dy = 0, 0
        if event.keysym == "Up": dx = -1
        elif event.keysym == "Down": dx = 1
        elif event.keysym == "Left": dy = -1
        elif event.keysym == "Right": dy = 1

        new_x = self.player_pos[0] + dx
        new_y = self.player_pos[1] + dy

        if (new_x, new_y) in obstacles:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="障害物にぶつかった！", font=("Arial", 24), fill="red")
            self.game_over = True
            self.root.unbind("<KeyPress>")
            return

        if self.can_move(new_x, new_y):
            self.player_pos = (new_x, new_y)
            self.draw_maze()
            if self.is_goal(new_x, new_y):
                self.canvas.create_text(WIDTH//2, HEIGHT//2, text="ゴール成功！", font=("Arial", 24), fill="green")
                self.game_over = True
                self.root.unbind("<KeyPress>")

    def update_timer(self):
        self.timer_label.config(text=f"制限時間: {self.remaining_time}")
        if self.remaining_time > 0 and not self.game_over:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        elif not self.game_over:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="時間切れ！", font=("Arial", 24), fill="red")
            self.game_over = True
            self.root.unbind("<KeyPress>")

    def move_obstacles(self):
        if self.game_over:
            return

        new_obstacles = []
        for x, y in obstacles:
            options = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            random.shuffle(options)
            for nx, ny in options:
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == 0 and (nx, ny) != self.player_pos:
                    new_obstacles.append((nx, ny))
                    break
            else:
                new_obstacles.append((x, y))
        globals()['obstacles'][:] = new_obstacles
        self.draw_maze()
        self.root.after(1500, self.move_obstacles)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷路ゲーム（障害物 + タイマー + エフェクト + 拡張難易度）")
    game = MazeGame(root)
    root.mainloop()


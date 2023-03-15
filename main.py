import tkinter as tk


class Pong(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pong")
        self.canvas = tk.Canvas(self, width=800, height=400, bg="black")
        self.canvas.pack()
        self.bind("<KeyPress>", self.key_press)
        self.paddle_speed = 20
        self.ball_speed = 2
        self.create_objects()
        self.mainloop()

    def create_objects(self):
        self.left_paddle = self.canvas.create_rectangle(30, 150, 40, 250, fill="white")
        self.right_paddle = self.canvas.create_rectangle(770, 150, 780, 250, fill="white")
        self.ball = self.canvas.create_oval(390, 190, 410, 210, fill="white")
        self.dx = self.ball_speed
        self.dy = self.ball_speed
        self.animate()

    def key_press(self, event):
        if event.keysym == "Up":
            self.canvas.move(self.right_paddle, 0, -self.paddle_speed)
        elif event.keysym == "Down":
            self.canvas.move(self.right_paddle, 0, self.paddle_speed)
        elif event.keysym == "w":
            self.canvas.move(self.left_paddle, 0, -self.paddle_speed)
        elif event.keysym == "s":
            self.canvas.move(self.left_paddle, 0, self.paddle_speed)

    def animate(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        x1, y1, x2, y2 = self.canvas.coords(self.ball)
        lp_x1, lp_y1, lp_x2, lp_y2 = self.canvas.coords(self.left_paddle)
        rp_x1, rp_y1, rp_x2, rp_y2 = self.canvas.coords(self.right_paddle)

        if y1 <= 0 or y2 >= 400:
            self.dy = -self.dy

        if (x1 <= lp_x2 and y1 >= lp_y1 and y2 <= lp_y2) or (x2 >= rp_x1 and y1 >= rp_y1 and y2 <= rp_y2):
            self.dx = -self.dx

        if x1 < 0 or x2 > 800:
            self.canvas.move(self.ball, 390 - x1, 190 - y1)
            self.dx = -self.dx

        self.after(10, self.animate)


if __name__ == "__main__":
    Pong()



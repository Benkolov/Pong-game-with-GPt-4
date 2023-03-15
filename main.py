import tkinter as tk
import random

# Create the main window
window = tk.Tk()
window.title("Pong Game")

# Set the size of the window
window.geometry("600x400")

# Create the canvas
canvas = tk.Canvas(window, bg="black", width=600, height=400)
canvas.pack()

# Create the ball
ball = canvas.create_oval(290, 190, 310, 210, fill="white")

# Create the paddles
left_paddle = canvas.create_rectangle(10, 150, 30, 250, fill="white")
right_paddle = canvas.create_rectangle(570, 150, 590, 250, fill="white")

# Set the initial speed of the ball
speed_x = random.randint(2, 5)
speed_y = random.randint(2, 5)

# Define the function to move the ball
def move_ball():
    global speed_x, speed_y
    canvas.move(ball, speed_x, speed_y)
    ball_pos = canvas.coords(ball)
    if ball_pos[1] <= 0 or ball_pos[3] >= 400:
        speed_y = -speed_y
    if ball_pos[0] <= 0:
        canvas.create_text(300, 200, text="Game Over - Left Wins!", font=("Arial", 20), fill="white")
        window.after(3000, window.destroy)
    elif ball_pos[2] >= 600:
        canvas.create_text(300, 200, text="Game Over - Right Wins!", font=("Arial", 20), fill="white")
        window.after(3000, window.destroy)
    elif canvas.coords(left_paddle)[2] >= ball_pos[0] >= canvas.coords(left_paddle)[0] and canvas.coords(left_paddle)[3] >= ball_pos[1] >= canvas.coords(left_paddle)[1]:
        speed_x = -speed_x
    elif canvas.coords(right_paddle)[0] <= ball_pos[2] <= canvas.coords(right_paddle)[2] and canvas.coords(right_paddle)[3] >= ball_pos[1] >= canvas.coords(right_paddle)[1]:
        speed_x = -speed_x
    window.after(20, move_ball)

# Define the function to move the left paddle
def move_left_paddle(event):
    if event.keysym == "Up":
        canvas.move(left_paddle, 0, -20)
    elif event.keysym == "Down":
        canvas.move(left_paddle, 0, 20)

# Define the function to move the right paddle
def move_right_paddle(event):
    if event.keysym == "w":
        canvas.move(right_paddle, 0, -20)
    elif event.keysym == "s":
        canvas.move(right_paddle, 0, 20)

# Bind the arrow keys to move the left paddle
canvas.bind_all("<Up>", move_left_paddle)
canvas.bind_all("<Down>", move_left_paddle)

# Bind the "w" and "s" keys to move the right paddle
canvas.bind_all("<w>", move_right_paddle)
canvas.bind_all("<s>", move_right_paddle)

# Move the ball
move_ball()

# Start the main loop
window.mainloop()

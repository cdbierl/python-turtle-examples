import turtle

#  Set up screen and turtle
screen = turtle.Screen()
screen.setup(600, 600)
turtle = turtle.Turtle()
turtle.speed(0)  # Set speed to fastest
turtle.hideturtle()

# Maze definition (1=wall, 0=path)
maze = [
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


# Function to draw a cell
def draw_cell(x, y, size, type):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    if type == 1:  # Wall
        turtle.fillcolor("black")
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()
    else:  # Path
        for _ in range(4):
            turtle.forward(size)
            turtle.left(90)


# Draw the maze
start_x = -280
start_y = 260
cell_size = 50

for row_index, row in enumerate(maze):
    for col_index, cell in enumerate(row):
        draw_cell(
            start_x + col_index * cell_size,
            start_y - row_index * cell_size,
            cell_size,
            cell,
        )

screen.mainloop()

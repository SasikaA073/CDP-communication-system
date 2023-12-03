import turtle

# Create a turtle screen and a turtle
screen = turtle.Screen()
pen = turtle.Turtle()

# Function to draw a rectangle
def draw_rectangle():
    for _ in range(4):
        pen.forward(100)  # Adjust the length of the sides as needed
        pen.right(90)

# Set the speed of the turtle
pen.speed(1)  # You can adjust the speed if needed

# Draw a rectangle
draw_rectangle()

# Keep the window open until closed by the user
turtle.done()

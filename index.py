import turtle as t

# Create a turtle object
my_turtle = t.Turtle()

# Move the turtle and draw
my_turtle.pendown()
# maroon yellow
for i in range(4):
    my_turtle.pencolor("maroon")
    my_turtle.forward(5)


# Print the position of the turtle
print(my_turtle.position())

# Set up the screen to exit on click
sc = t.Screen()
sc.exitonclick()

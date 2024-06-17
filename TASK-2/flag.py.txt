import turtle

# Function to draw rectangle
def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

# Function to draw the Ashoka Chakra
def draw_chakra(x, y, radius):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("#000080")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Main function to draw the Indian flag
def draw_indian_flag():
    turtle.setup(600, 400)
    turtle.speed(0)
    turtle.title("Indian Flag")
    turtle.bgcolor("#FFFFFF")
    
    # Green Rectangle
    draw_rectangle("#138808", -300, 100, 600, 100)
    
    # White Rectangle
    draw_rectangle("#FFFFFF", -300, 0, 600, 100)
    
    # Saffron Rectangle
    draw_rectangle("#FF9933", -300, -100, 600, 100)
    
    # Ashoka Chakra
    draw_chakra(0, 50, 30)

    turtle.hideturtle()
    turtle.done()

# Call the main function
draw_indian_flag()
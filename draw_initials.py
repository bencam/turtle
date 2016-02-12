import turtle

def draw_initials():
    #Set up screen, etc.
    window = turtle.Screen()
    window.bgcolor('gray')

    ###THE LETTER B###
    letter = turtle.Turtle()
    letter.shape('turtle')
    letter.color('white', 'gray')
    letter.speed(8)
    
    #Move pen into place
    letter.penup()
    letter.left(180)
    letter.forward(200)
    letter.pendown()

    #Draw the letter B
    letter.right(90)
    letter.forward(240)
    letter.right(90)
    letter.forward(65)
    letter.circle(-55,180)
    letter.forward(65)
    letter.left(180)
    letter.forward(75)
    letter.circle(-65, 180)
    letter.forward(75)

    #Move pen into place
    letter.penup()
    letter.right(180)
    letter.forward(150)
    letter.left(90)
    letter.forward(240)
    letter.right(90)
    letter.forward(190)
    letter.right(90)
    letter.forward(80)
    letter.pendown()

    #Draw the letter C
    letter.circle(-80,-180)
    letter.right(180)
    letter.forward(81)
    letter.circle(80,180)

    #Hide turtle and exit drawing window
    letter.hideturtle()
    window.exitonclick()

draw_initials()

#!/usr/bin/env python

import turtle


def draw_square(some_turtle):
    """Draw one square using Python Turtle"""
    for n in range(0, 4):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_multiple_squares():
    """
    Draw 1,181 squares using Python Turtle.
    Each square starts from the same point; the
    result is a circle made up of squares.
    """
    # Set up screen, etc.
    window = turtle.Screen()
    window.bgcolor('black')

    # Brad
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('white', 'gray')
    brad.speed(20)
    for i in range(1, 181):
        draw_square(brad)
        brad.right(2)
    brad.hideturtle()

    window.exitonclick()


draw_multiple_squares()

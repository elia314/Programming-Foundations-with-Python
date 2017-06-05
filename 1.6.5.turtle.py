import turtle
from turtle import *
 
def draw_square(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(1,4):
           some_turtle.forward(100)
           some_turtle.left(120)
          

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    # create turtle brad and draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.setpos(0,100)
    brad.speed(2)
    draw_square(brad)
    #create turtle joe and draw a circle
    joe = turtle.Turtle()
    joe.shape("arrow")
    joe.color("blue")
 #   joe.setpos(100,0)
    joe.speed(2)
    draw_triangle(joe)

    #create turtle rufio and draw a triangle
    rufio = turtle.Turtle()
    rufio.shape("triangle")
    rufio.color("green")
    rufio.setpos(50,0)
    rufio.circle(50)

 

    window.exitonclick()

draw_art()

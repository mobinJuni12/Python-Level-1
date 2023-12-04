#IMPORTANT - Make sure you display the turtle 
import turtle
import random
juni = turtle.Turtle()

juni.goto(0,0)


screen = turtle.Screen()

def drawSquare(x,y):
  for i in range(4):
    juni.forward(100)
    juni.right(90)
    


screen.onclick(drawSquare)
screen.listen()

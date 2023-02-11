import turtle
 
turtlePen = turtle.Turtle()
window = turtle.Screen()
 
 def house():
    """
    Функция рисует дом
    """
    turtle.shape("turtle")
    turtle.color("brown")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()
    
    turtle.color("green")
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(35)
    
    turtle.right(90)
    turtle.forward(35)
    turtle.end_fill()
    
    input()
    

def sun():
    turtlePen.color("blue")
    for i in range(0, n):
        turtlePen.forward(150)
        turtlePen.left(90)
        turtlePen.forward(50)
        turtlePen.left(90)
        turtlePen.forward(50)
        turtlePen.right(90)
        turtlePen.forward(50)
        turtlePen.left(90)
        turtlePen.forward(50)
        turtlePen.left(90)
        turtlePen.forward(50)
        turtlePen.right(90)
        turtlePen.forward(50)
        turtlePen.left(90)
        turtlePen.forward(50)

turtlePen.speed(10)
 
turtlePen.color("white")
turtlePen.right(90)
turtlePen.forward(250)
turtlePen.right(180)

window.mainloop() 


def draw_pic():
    sun(1)
    house()
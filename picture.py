import turtle
 

def house():
    """
    Функция рисует дом
    """
    turtle.penup()
    turtle.setpos(-100,-100)
    turtle.pendown()
    
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
    

def sun(n):

    turtle.penup()
    turtle.setpos(-100,-100)
    turtle.pendown()
    
    turtlePen = turtle.Turtle()
    window = turtle.Screen()
    
    turtlePen.color("blue")
    turtlePen.speed(2)
 
    
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

    window.mainloop() 

def draw_pic():
    house()
    sun(1)

draw_pic()
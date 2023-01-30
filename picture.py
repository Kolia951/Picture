import turtle

def sun():
    """
    Функция рисует солнце и тучи
    """
 
  
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
    
house()

def draw_pic():
    sun()
    house()
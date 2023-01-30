import turtle
 
turtlePen = turtle.Turtle()
window = turtle.Screen()
 
 
def clouds(n):
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


clouds(1)   # &lt;- вызов функции
 
turtlePen.color("white")
turtlePen.right(90)
turtlePen.forward(250)
turtlePen.right(180)

clouds(1)

window.mainloop() 
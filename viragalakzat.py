


import turtle

def viragalakzat():
    turtle.hideturtle()
    turtle.clear()
    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, 60)
    turtle.pendown()
    for _ in range(20):
        turtle.forward(120)
        turtle.right(100)
        turtle.forward(120)





ablak = turtle.Screen()

turtle.listen()
turtle.onkey(viragalakzat,key="h")
turtle.onkey(turtle.bye,key="q")
turtle.mainloop()
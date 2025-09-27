"""Rajzol egy 150 pontos egyenlőszárú háromszöget a képernyő közepére
színe legyen piros
a rajzolás induljon a h betűre
kilépés legyen q betűre
"""

import turtle

def haromszog():
    turtle.hideturtle()
    turtle.clear()
    turtle.pencolor("red")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, 75)
    turtle.pendown()
    turtle.goto(-50, 0)
    turtle.goto(0, 75)
    turtle.goto(50,0)
    turtle.goto(-50, 0)



ablak = turtle.Screen()

turtle.listen()
turtle.onkey(haromszog,key="h")
turtle.onkey(turtle.bye,key="q")
turtle.mainloop()
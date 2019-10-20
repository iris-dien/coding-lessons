import turtle 



window = turtle.Screen() 

window.bgcolor("#2e3266") 


window.title("iris' black window")

turtle_pen = turtle.Pen() 
turtle_pen.pencolor("#c41a1a")


for counter in range(160):

    turtle_pen.forward(counter)

    turtle_pen.left(145)

    if(counter > 50):
        turtle_pen.pensize(1)

        window.bgcolor("pink")
else:
    turtle_pen.pensize(2)


    window.bgcolor("red") 
    

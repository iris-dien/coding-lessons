import turtle 

turtle.speed(8)

window = turtle.Screen() 

window.bgcolor("#2e3266") 


window.title("iris' black window")

turtle_pen = turtle.Pen() 

COLORS = ["red", "blue", "green", "pink"]
for counter in range(160):
        color = COLORS[counter % 4] 

        turtle_pen.pencolor(color)

        turtle_pen.forward(counter)

        turtle_pen.left(145)

#     if(counter > 50):
#         turtle_pen.pensize(1)

#         window.bgcolor("pink")
# else:
#     turtle_pen.pensize(2)


#     window.bgcolor("red") 

#     COLORS = ["pink", "purple", "#ff003c", "blue"] 


    

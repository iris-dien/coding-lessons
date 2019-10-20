import turtle 

turtle.speed(8)

window = turtle.Screen() 

window.bgcolor("#2e3266") 


window.title("iris' black window")

turtle_pen = turtle.Pen() 

COLORS = ["red", "blue", "green", "pink"]
your_name = turtle.textinput("enter your name", "what is your name?")
for counter in range(160):
        color = COLORS[counter % 4] 

        turtle_pen.pencolor(color)

        turtle_pen.penup()
        turtle_pen.forward(counter*4)
        turtle_pen.write(your_name, font=("georgia", int((counter+4)/4), "bold"))
        turtle_pen.left(90)


#     if(counter > 50):
#         turtle_pen.pensize(1)

#         window.bgcolor("pink")
# else:
#     turtle_pen.pensize(2)


#     window.bgcolor("red") 

#     COLORS = ["pink", "purple", "#ff003c", "blue"] 


    

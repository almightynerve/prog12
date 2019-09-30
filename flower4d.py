import turtle

tina = turtle.Turtle()
tina.speed(12)
tina.hideturtle()
background = turtle.Screen()

##tina_background = input("What color should the background be?")
##tina_color = input("What color should Tina use to draw?")

tina_color = "gold"
tina_background = "silver"

def cFlower(x, y, l1, f1, size,):
    for flowz in range(6):
        background.bgcolor(tina_background)

        tina.color("green")
        tina.pu()
        tina.goto(x + f1, y)
        tina.pd()
        
        tina.seth(270)
        tina.pensize(f1)
        tina.fd(500)
        tina.pensize(2)
        tina.pu()
        tina.goto(x, y)
        tina.pd()
        tina.color(tina_color, "pink")
        tina.pu()
        turtle.up()
        turtle.goto(x,y)
        turtle.down()
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.circle(300,70)
        turtle.left(110)
        turtle.circle(300,70)
        turtle.end_fill()
        tina.pd()

        for pedalY in range(10):
            turtle.up()
            turtle.goto(x+20,y)
            turtle.down()
            turtle.speed(40)
            
            turtle.fillcolor('yellow')
            turtle.begin_fill()
            turtle.circle(300,70)
            turtle.left(110)
            turtle.circle(300,70)
            turtle.end_fill()
            tina.pd()

        for pedal in range(10):
            tina.begin_fill()    
            tina.left(l1)
            tina.forward(f1)
            tina.circle(size)
            tina.end_fill()
 
            

        tina.pu()
        tina.color("black", "gold")

        tina.begin_fill()
        tina.goto(x+30, y-40)
        tina.pd()
        tina.circle(size/1.5)
        tina.end_fill()
        
        

                   
        
        x = x + 400
        y = y -2




cFlower(-623, 100, 46, 20, 75)
cFlower(-800, 0, 46, 20, 100)





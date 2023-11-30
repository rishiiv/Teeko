import turtle as t

def reset():
    t.color("black")
    t.setheading(0)
    t.penup()
    t.goto(0,0)
    t.pendown()

def gamestate(array): #Currently hardcoded, will fix later
    return 2

def drawendscreen():
    
    reset()    #Previously defined function that returns to pos (0, 0)
    t.penup()
    t.lt(90)
    t.fd(100)
    t.right(90)
    
    #Uses a different function to tell how the game ended, displays outcome
    if gamestate(array) == -1:
        t.write("GAME TERMINATED", align="Center", font=("Courier", 60, "normal"))
        t.width(15)
        t.pendown()
        t.fd(450)
        t.left(90)
        t.fd(100)
        t.left(90)
        t.fd(900)
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(450)
        t.penup()
        t.rt(90)
        t.fd(100)
        t.lt(90)
        
    elif gamestate(array) == 1:
        t.write("PLAYER 1 WON", align="Center", font=("Courier", 60, "normal"))
        t.width(15)
        t.pendown()
        t.fd(360)
        t.left(90)
        t.fd(100)
        t.left(90)
        t.fd(720)
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(360)
        t.penup()
        t.rt(90)
        t.fd(100)
        t.lt(90)
        
    elif gamestate(array) == 2:
        t.write("PLAYER 2 WON", align="Center", font=("Courier", 60, "normal"))
        t.width(15)
        t.pendown()
        t.fd(360)
        t.left(90)
        t.fd(100)
        t.left(90)
        t.fd(720)
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(360)
        t.penup()
        t.rt(90)
        t.fd(100)
        t.lt(90)
        
    #Now displays a play again button
    t.write("PLAY AGAIN?", align="center", font=("Courier", 60, "normal"))
    t.pendown()
    t.fd(330)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(660)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(330)
    t.penup()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    
    #And finally creates a close button
    t.write("CLOSE", align="center", font=("Courier", 60, "normal"))
    t.pendown()
    t.fd(150)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(300)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(150)
    t.penup()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    
def playagainbutton(x, y):
    if x>-330 and x<330 and y>0 and y<100:
        print("howdy")
        
def closebutton(x, y):
    if x>-150 and x<150 and y>-100 and y<0:
        print("whoop")

################# FUNCTION LAND GONE ##################

array = []
drawendscreen()
t.onscreenclick(playagainbutton, add=True)
t.onscreenclick(closebutton, add=True)
t.listen()
t.mainloop()
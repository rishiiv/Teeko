# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Ashmit Thakur
# Kai Buckingham
# Parker Price
# Rishii Vijay
# Section: 503
# Assignment: 2.8
# Date: 1 12 2023

import turtle as t
import numpy as np

with open("teeko_winstates.txt", "w") as winstates:
    winstates.write("1,1,1,1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,1,1,1,1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[1,1,1,1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,1,1,1,1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[1,1,1,1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,1,1,1,1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[1,1,1,1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,1,1,1,1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[1,1,1,1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,1,1,1,1\n"
+"1,-1,-1,-1,-1],[1,-1,-1,-1,-1],[1,-1,-1,-1,-1],[1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[1,-1,-1,-1,-1],[1,-1,-1,-1,-1],[1,-1,-1,-1,-1],[1,-1,-1,-1,-1\n"
+"-1,1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,1,-1,-1,-1\n"
+"-1,-1,1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,1,-1,-1\n"
+"-1,-1,-1,1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,1,-1\n"
+"-1,-1,-1,-1,1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,1\n"
+"1,-1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,-1,1\n"
+"-1,-1,-1,-1,1],[-1,-1,-1,1,-1],[-1,-1,1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,1,-1],[-1,-1,1,-1,-1],[-1,1,-1,-1,-1],[1,-1,-1,-1,-1\n"
+"-1,-1,-1,1,-1],[-1,-1,1,-1,-1],[-1,1,-1,-1,-1],[1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,1],[-1,-1,-1,1,-1],[-1,-1,1,-1,-1],[-1,1,-1,-1,-1\n"
+"-1,1,-1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,-1,1,-1],[-1,-1,-1,-1,1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[1,-1,-1,-1,-1],[-1,1,-1,-1,-1],[-1,-1,1,-1,-1],[-1,-1,-1,1,-1\n"
+"1,1,-1,-1,-1],[1,1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,1,1,-1,-1],[-1,1,1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,1,1,-1],[-1,-1,1,1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,1,1],[-1,-1,-1,1,1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[1,1,-1,-1,-1],[1,1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,1,1,-1,-1],[-1,1,1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,1,1,-1],[-1,-1,1,1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,1,1],[-1,-1,-1,1,1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[1,1,-1,-1,-1],[1,1,-1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,1,1,-1,-1],[-1,1,1,-1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,1,1,-1],[-1,-1,1,1,-1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,1,1],[-1,-1,-1,1,1],[-1,-1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[1,1,-1,-1,-1],[1,1,-1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,1,1,-1,-1],[-1,1,1,-1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,1,1,-1],[-1,-1,1,1,-1\n"
+"-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,1,1],[-1,-1,-1,1,1\n")


def toint(list):
    retlist = []
    for i in list:
        retlist.append(int(i[-1]))
    return retlist

#handles win conditions



class Teeko:

    def __init__(self):
        
        #private variables
        self.gamerunning = False
        self.boardarray = np.array([[-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1],
                                    [-1,-1,-1,-1,-1]])
        
        self.tilecount = [0]
        self.alltilesplaced = False
        
        self.rulesshowing = False
        self.rulebuttontext = 'SHOW RULES'
        
        self.isblack = True
        
        self.movingpiece = False
        self.piecetomove = None
        self.adjacentarray = None
        
       


        #initiates window
        self.screen = t.Screen()
        self.screen.setup(1000,700,10,10)
        self.screen.clear()
        self.screen.bgcolor('sea green')
        self.screen.tracer(0, 0)
        t.ht()
        self.draw_board()
        self.screen.onscreenclick(self.buttonClick,1)
        self.screen.listen()
    
    def createrulesbutton(self):
        #creates rules button
        #Dimensions: 200-300 x 250-270
        t.penup()
        t.goto(200,250)
        t.pendown()
        t.setheading(0)
        t.color('sea green')
        t.fillcolor('sea green')
        t.begin_fill()
        for i in range(2):
            t.forward(100)
            t.left(90)
            t.forward(20)
            t.left(90)
        t.end_fill()

        t.penup()
        t.goto(200,250)
        t.pendown()
        t.setheading(0)
        t.color('black')
        for i in range(2):
            t.forward(100)
            t.left(90)
            t.forward(20)
            t.left(90)
        t.penup()
        t.goto(200,250)
        t.write(self.rulebuttontext, font=('Courier',12,'normal'))
        t.update()

    def draw_board(self):
        self.gamerunning = True
        #Game Board
        #Dimensions: -450--50 x 300--100
        y = 300
        x = -450
        t.width(3)
        t.penup()
        t.setx(x)
        t.sety(y)
        t.pendown()

        #creates grid
        for i in range(4):
            t.forward(400)
            t.right(90)
        for j in range(2):
            for i in range(2):
                t.forward(80)
                t.right(90)
                t.forward(400)
                t.left(90)
                t.forward(80)
                t.left(90)
                t.forward(400)
                t.right(90)
            t.penup()
            t.setx(x+400)
            t.sety(y)
            t.right(90)
            t.pendown()
        
        self.createrulesbutton()

        #shows starting player (black)
        t.penup()
        t.goto(-355,-150)
        t.pendown()
        t.color('black')
        t.write("BLACK TO PLAY.",font=("Courier",20,"bold"))
        t.update()
        
    def draw_circle(self,xcoord,ycoord,c, fc = 'black'):
        t.setheading(0)
        if c == '0':
            colour = 'red'
        elif c == '1':
            colour = 'black'
        else:
            colour = c
        t.penup()
        t.setx(xcoord+40)
        t.sety(ycoord+68)
        t.pendown()
        t.color(fc)
        t.fillcolor(colour)

        t.begin_fill()
        for i in range(400):
            t.forward(.5)
            t.right(1)
        t.end_fill()
        for i in range(40):
            t.back(.5)
            t.left(1)
    
    def draw_square(self, xcoord,ycoord,c='cyan'):
        t.penup()
        t.setx(-450 + 80*(ycoord)+5)
        t.sety(-100 + 80*(5-xcoord)-5)
        t.pendown()
        t.color(c)
        t.width(4)
        t.setheading(0)
        for i in range(4):
            t.forward(70)
            t.right(90)
        t.width(3)
        t.update()

    def showrules(self):
        t.penup()
        t.goto(20,-160)
        t.pendown()
        t.write("The Teeko board consists of twenty-five \nspaces arranged in a five-by-five grid. \n"
                    +"There are eight markers in a Teeko game, \nfour black and four red. One player,\n"
                    +" Black plays the black markers, and the \nother, Red, plays the red. Black moves \n"
                    +"first and places one marker on any space \non the board. Red then places a marker \n"
                    +"on any unoccupied space; black does the \nsame; and so on until all eight markers \n"
                    +"are on the board. The object of the game \nis for either player to win by having all \n"
                    +"four of their markers in a straight line \n(vertical, horizontal, or diagonal) or on a \n"
                    +"square of four adjacent spaces. (Adjacency \nis horizontal, vertical, or diagonal, but \n"
                    +"does not wrap around the edges of the board.)\n If neither player has won after the drop \n"
                    +"(when all eight pieces are on the board), \nthen they move their pieces one at a time, \n"
                    +"with Black playing first. A piece may be \nmoved only to an adjacent space",font=('Courier',12,'normal'))
        
        self.changerulebutton()
        self.rulesshowing = True
        t.update()

    def hiderules(self):
        t.penup()
        t.goto(10,-170)
        t.setheading(0)
        t.pendown
        t.color('sea green')
        t.fillcolor('sea green')
        t.begin_fill()
        for i in range(2):
            t.forward(500)
            t.left(90)
            t.forward(405)
            t.left(90)
        t.end_fill()
        
        self.changerulebutton()
        self.rulesshowing = False
        t.update()

    def changerulebutton(self):
        if self.rulesshowing:
            self.rulebuttontext = 'SHOW RULES'
            
        else:
            self.rulebuttontext = 'HIDE RULES'
        self.createrulesbutton()
        t.update()

    def getadjacent(self,x,y):
        adjacents = np.array([[x-1,y-1],[x-1,y],[x-1,y+1],[x,y+1],[x+1,y+1],[x+1,y],[x+1,y-1],[x,y-1]])
        
        return adjacents
    
    def pickuppiece(self,x,y):
        #picking up a piece
            if self.isblack:
                turn = 1
            else:
                turn = 0

            thispiececolor = self.boardarray[(x,y)]
            if thispiececolor != -1:
                if thispiececolor == turn:
                    self.draw_square(x,y)
                    self.adjacentarray = self.getadjacent(x,y)
                    self.movingpiece = True
                    self.piecetomove = [x,y,self.boardarray[(x,y)]]    
                
    def movepiece(self,xwin,ywin,x,y,color):
        #placing a piece
        if not self.alltilesplaced:
            if self.boardarray[(x,y)] == -1:
                self.draw_circle(xwin,ywin,color)
                self.tilecount[0] += 1
                self.boardarray[(x,y)] = self.isblack
                self.isblack = not self.isblack
                self.gamecheck(self.boardarray)
                
        #moving a piece
        elif self.movingpiece:
            #checks if the moving position is adjacent
            isadjacent = False
            for i in self.adjacentarray:
                if i[0] == x and i[1] == y:
                    isadjacent = True

            #if player wants to move a different piece        
            if self.boardarray[(x,y)] == self.piecetomove[2]:
                oldx = self.piecetomove[0]
                oldy = self.piecetomove[1]
                #removes old square
                self.draw_square(oldx,oldy,'sea green')

                self.movingpiece = False
                self.adjacentarray = None
                self.piecetomove = None
                self.pickuppiece(x,y)
            
            #moves the piece
            elif isadjacent and self.boardarray[(x,y)] == -1:
                #draws new circle
                self.draw_circle(-450 + y*80, -100 + (4-x)*80, str(self.piecetomove[2]))
                self.boardarray[(x,y)] = self.piecetomove[2]
                        
                #removes old circle
                oldx = self.piecetomove[0]
                oldy = self.piecetomove[1]
                self.draw_circle(-450 + oldy*80, -100 + (4-oldx)*80,'sea green','sea green')
                self.boardarray[(oldx,oldy)] = -1
                
                #removes old square
                self.draw_square(oldx,oldy,'sea green')
                
                #Checks for victory / sets up next turn
                self.gamecheck(self.boardarray)
                self.movingpiece = False
                self.adjacentarray = None
                self.piecetomove = None
                self.isblack = not self.isblack
            
            
        else:
            thisx = x
            thisy = y
            self.pickuppiece(thisx,thisy)
    
    def gamecheck(self,game):
        '''
        

        Parameters
        ----------
        game : NumPy Array
        
        Checks the current gamestate array to see if it matches a win condition

        '''
        
        try:
                
            #Finds the current positions of Black and converts them to a form we check
            self.gameRed = game.copy()
            self.gameRed[self.gameRed == 1] = -1
            self.gameRed[self.gameRed == 0] = 1
            
            #Finds the current positions of Red and converts them to a form we check
            self.gameBlack = game.copy()
            self.gameBlack[self.gameBlack == 0] = -1
            
            
            with open("teeko_winstates.txt") as winstates:
                
                for line in winstates.readlines():
                    line = line.strip().split("],[")
                    for i in range(5):
                        line[i] = [int(j) for j in line[i].split(",")]
                    
                    statearray = np.array(line)
                    
                    if np.array_equal(self.gameBlack, statearray):
                        t.clear()
                        t.bgcolor("sea green")
                        self.drawendscreen(1)
                    
                    if np.array_equal(self.gameRed, statearray):
                        t.clear()
                        t.bgcolor("sea green")
                        self.drawendscreen(2)
        except:
            #Crashes if input is unexpected or winstates are wrong
            t.bye()

    def buttonClick(self,x,y):
        
        if self.gamerunning:

            if self.tilecount[0] < 8:
                if self.isblack == True:
                    color_local = 'black'
                else:
                    color_local = 'red'
            else:
                self.alltilesplaced = True
                color_local = None
        

    #Each of 25 squares
    #########################################################################################
            if x > -450 and x < -370:
                if y > -100 and y < -20:
                    self.movepiece(-450,-100,4,0,color_local)
                    
                #############################################################################        
                if y > -20 and y < 60:
                    self.movepiece(-450,-20,3,0,color_local)

                #############################################################################
                if y > 60 and y < 140:
                    self.movepiece(-450,60,2,0,color_local)
                
                #############################################################################        
                if y > 140 and y < 220:
                    self.movepiece(-450,140,1,0,color_local)
                
                #############################################################################        
                if y > 220 and y < 300:
                    self.movepiece(-450,220,0,0,color_local)

    #########################################################################################    
            if x > -370 and x < -290:
                if y > -100 and y < -20:
                    self.movepiece(-370,-100,4,1,color_local)
                #############################################################################        
                if y > -20 and y < 60:
                    self.movepiece(-370,-20,3,1,color_local)

                #############################################################################        
                if y > 60 and y < 140:
                    self.movepiece(-370,60,2,1,color_local)
                    
                #############################################################################
                if y > 140 and y < 220:
                    self.movepiece(-370,140,1,1,color_local)

                #############################################################################        
                if y > 220 and y < 300:
                    self.movepiece(-370,220,0,1,color_local)

    #########################################################################################                    
            if x > -290 and x < -210:
                if y > -100 and y < -20:
                    self.movepiece(-290,-100,4,2,color_local)

                #############################################################################        
                if y > -20 and y < 60:
                    self.movepiece(-290,-20,3,2,color_local)

                #############################################################################        
                if y > 60 and y < 140:
                    self.movepiece(-290,60,2,2,color_local)

                #############################################################################        
                if y > 140 and y < 220:
                    self.movepiece(-290,140,1,2,color_local)
                        
                #############################################################################
                if y > 220 and y < 300:
                    self.movepiece(-290,220,0,2,color_local)
            
    #########################################################################################                    
            if x > -210 and x < -130:
                if y > -100 and y < -20:
                    self.movepiece(-210,-100,4,3,color_local)

                #############################################################################        
                if y > -20 and y < 60:
                    self.movepiece(-210,-20,3,3,color_local)

                #############################################################################        
                if y > 60 and y < 140:
                    self.movepiece(-210,60,2,3,color_local)

                #############################################################################        
                if y > 140 and y < 220:
                    self.movepiece(-210,140,1,3,color_local)

                #############################################################################        
                if y > 220 and y < 300:
                    self.movepiece(-210,220,0,3,color_local)

    #########################################################################################                    
            if x > -130 and x < -50:
                if y > -100 and y < -20:
                    self.movepiece(-130,-100,4,4,color_local)

                #############################################################################        
                if y > -20 and y < 60:
                    self.movepiece(-130,-20,3,4,color_local)

                #############################################################################        
                if y > 60 and y < 140:
                    self.movepiece(-130,60,2,4,color_local)

                #############################################################################        
                if y > 140 and y < 220:
                    self.movepiece(-130,140,1,4,color_local)

                #############################################################################        
                if y > 220 and y < 300:
                    self.movepiece(-130,220,0,4,color_local)

#########################################################################################
        if self.isblack:
            #clears old text
            t.penup()
            t.goto(-355,-155)
            t.pendown
            t.color('sea green')
            t.fillcolor('sea green')
            t.begin_fill()
            for i in range(2):
                t.forward(230)
                t.left(90)
                t.forward(40)
                t.left(90)
            t.end_fill()

            #writes new text
            if self.gamerunning:
                t.penup()
                t.goto(-355,-150)
                t.pendown()
                t.color('black')
                t.write("BLACK TO PLAY.",font=("Courier",20,"bold"))
                t.update()
        elif self.isblack == False:
             #clears old text
            t.penup()
            t.goto(-355,-155)
            t.pendown
            t.color('sea green')
            t.fillcolor('sea green')
            t.begin_fill()
            for i in range(2):
                t.forward(230)
                t.left(90)
                t.forward(40)
                t.left(90)
            t.end_fill()
            
            #writes new text
            if self.gamerunning:
                t.penup()
                t.goto(-355,-150)
                t.pendown()
                t.color('black')
                t.write("RED TO PLAY.",font=("Courier",20,"bold"))
                t.update()
        
        #Show rules
        if x > 200 and x < 300 and y > 250 and y < 270:
            if not self.rulesshowing:
                self.showrules()
            
            else:
                self.hiderules()

    def stop(self):
        t.done()
    
    def drawendscreen(self, vic):
        self.isblack = None
        self.gamerunning = False
        reset()    #Previously defined function that returns to pos (0, 0)
        t.penup()
        t.lt(90)
        t.fd(100)
        t.right(90)
        
        

        #Uses a different function to tell how the game ended, displays outcome
            
        if vic == 1:
            t.tracer(0,0)
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
            
        elif vic == 2:
            t.tracer(0,0)
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
        
        t.onscreenclick(self.playagainbutton, add=True)
        t.onscreenclick(self.closebutton, add=True)
        t.listen()
        
    def playagainbutton(self,x, y):
        if x>-330 and x<330 and y>0 and y<100:
            game = Teeko()
            game.stop()
            
    def closebutton(self,x, y):
        if x>-150 and x<150 and y>-100 and y<0:
            t.bye()

#############################################################################################

def drawtitle():
    '''
    

    Returns
    -------
    A very awesome Teeko logo.
    
    Graphic design is my passion

    '''
    t.clear()
    t.bgcolor("sea green")
    t.width(15)
    
    t.penup()
    t.goto(-250, 300)
    t.pendown()
    t.width(15)
    t.right(90)
    t.fd(100)
    t.circle(100, 90)
    t.penup()
    t.back(150)
    t.left(90)
    t.fd(150)
    t.right(90)
    t.pendown()
    t.fd(200)
    t.left(90)
    t.circle(50, 270)
    t.fd(150)
    t.left(90)
    t.circle(50, 270)
    t.fd(50)
    t.circle(50, 90)
    t.fd(100)
    t.bk(200)
    t.right(90)
    t.penup()
    t.fd(50)
    t.pendown()
    t.circle(50, -180)
    t.penup()
    t.right(180)
    t.fd(25)
    t.pendown()
    t.fillcolor("red")
    t.rt(90)
    t.begin_fill()
    t.circle(100, 360)
    t.end_fill()

def reset():
    '''
    

    Resets formatting things such as pen color and orientation
    Also brings the turtle back to position (0,0)
    Does not interfere with pen width

    '''
    t.color("black")
    t.setheading(0)
    t.penup()
    t.goto(0,0)
    t.pendown()

def drawtitletexts():
    '''
    

    Creates the graphic components of the Start and Rules buttons
    Boxes them in a neat little rectangle for your clicking pleasure

    '''
    t.width(15)
    t.tracer(0,0)
    t.setheading(0)
    t.write("START GAME", align="center", font=("Courier", 60, "normal"))
    t.pendown()
    t.fd(300)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(600)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(300)
    t.penup()
    
    
    t.right(90)
    t.fd(100)
    t.write("RULES", align="center", font=("Courier", 60, "normal"))
    t.pendown()
    t.left(90)
    t.fd(150)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(300)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(150)
    t.penup()
    t.update()
    
def startbutton(x, y):
    '''
    

    Parameters
    ----------
    x : integer
        x position that is clicked
    y : integer
        y position that is clicked

    If the place that the user clicks is within this range, the purpose of the
    button will activate

    '''
    if x>-300 and x<300 and y>-50 and y<50:
        game = Teeko()
        game.stop()
        
def rulesbutton(x, y):
    '''
    

    Parameters
    ----------
    x : integer
        x position that is clicked
    y : integer
        y position that is clicked

    If the place that the user clicks is within this range, the purpose of the
    button will activate

    '''
    if x>-150 and x<150 and y>-150 and y<-50:
        rulesscreen()
        
def rulesscreen():
    t.clear()
    t.bgcolor("sea green")
    t.penup()
    t.goto(0, -200)
    t.write("The Teeko board consists of twenty-five \nspaces arranged in a five-by-five grid. \n"
                +"There are eight markers in a Teeko game, \nfour black and four red. One player,\n"
                +" Black plays the black markers, and the \nother, Red, plays the red. Black moves \n"
                +"first and places one marker on any space \non the board. Red then places a marker \n"
                +"on any unoccupied space; black does the \nsame; and so on until all eight markers \n"
                +"are on the board. The object of the game \nis for either player to win by having all \n"
                +"four of their markers in a straight line \n(vertical, horizontal, or diagonal) or on a \n"
                +"square of four adjacent spaces. (Adjacency \nis horizontal, vertical, or diagonal, but \n"
                +"does not wrap around the edges of the board.)\n If neither player has won after the drop \n"
                +"(when all eight pieces are on the board), \nthen they move their pieces one at a time, \n"
                +"with Black playing first. A piece may be \nmoved only to an adjacent space",align="center", font=('Courier',16,'normal'))
    
    t.goto(0, -250)
    t.write("Back to Title", align="center", font=("Courier", 12, "normal"))
    t.pendown()
    t.width(3)
    t.tracer(0,0)
    t.setheading(0)
    t.fd(78)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(156)
    t.left(90)
    t.fd(20)
    t.left(90)
    t.fd(78)
    t.update()
    
    t.onscreenclick(backtotitlebutton)
    t.listen()

def backtotitlebutton(x, y):
    if x>-78 and x<78 and y>-250 and y<-230:
        drawtitle()
        reset()
        t.penup()
        t.right(90)
        t.fd(50)
        drawtitletexts()
        t.onscreenclick(startbutton)
        t.onscreenclick(rulesbutton, add=True)
        t.listen()

############################## NO MORE FUNCTION LAND #########################

#Setting up screen
t.setup(1000,700,10,10)
t.bgcolor('sea green')
t.ht()
#Glorious logo
drawtitle()

#Putting turtle in the right pos to not interfere with title
reset()
t.penup()
t.right(90)
t.fd(50)
drawtitletexts()

#Click input stuff
t.onscreenclick(startbutton)
t.onscreenclick(rulesbutton, add=True)
t.listen()

#Compile later
t.mainloop()
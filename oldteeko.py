import turtle
import numpy as np


class Teeko:

    def __init__(self):

        self.tilecount = [0]
        self.isblack = True
        self.alltilesplaced = False
        self.boardarray = np.array([[-1, -1, -1, -1, -1],
                                    [-1, -1, -1, -1, -1],
                                    [-1, -1, -1, -1, -1],
                                    [-1, -1, -1, -1, -1],
                                    [-1, -1, -1, -1, -1]])
        print(self.boardarray)

        self.screen = turtle.Screen()
        self.screen.setup(1000, 700, 10, 10)
        self.screen.tracer(0, 0)
        turtle.ht()
        self.draw_board()
        self.screen.onscreenclick(self.buttonClick, 1)
        self.screen.listen()

    def draw_board(self):

        # Game Board
        # -450--50 x 300--100
        y = 300
        x = -450
        turtle.width(2)
        turtle.penup()
        turtle.setx(x)
        turtle.sety(y)
        turtle.pendown()
        for i in range(4):
            turtle.forward(400)
            turtle.right(90)
        for j in range(2):
            for i in range(2):
                turtle.forward(80)
                turtle.right(90)
                turtle.forward(400)
                turtle.left(90)
                turtle.forward(80)
                turtle.left(90)
                turtle.forward(400)
                turtle.right(90)
            turtle.penup()
            turtle.setx(x + 400)
            turtle.sety(y)
            turtle.right(90)
            turtle.pendown()

        ################################################################################################

        # Rules Button
        # 200-300 x 250-270
        turtle.penup()
        turtle.goto(200, 250)
        turtle.pendown()
        turtle.right(180)
        for i in range(2):
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
        turtle.penup()
        turtle.goto(200, 250)
        rulesshow = 'Show Rules'
        turtle.write(rulesshow, font=('Courier', 12, 'normal'))

        turtle.update()

    def draw_circle(self, xcoord, ycoord, c):

        turtle.penup()
        turtle.setx(xcoord + 40)
        turtle.sety(ycoord + 68)
        turtle.pendown()
        turtle.color(c)

        turtle.begin_fill()
        for i in range(360):
            turtle.forward(.5)
            turtle.right(1)
        turtle.end_fill()

    def showrules(self):
        turtle.penup()
        turtle.goto(-350, -300)
        turtle.pendown()
        turtle.write("The Teeko board consists of twenty-five \nspaces arranged in a five-by-five grid. \n"
                     + "There are eight markers in a Teeko game, \nfour black and four red. One player,\n"
                     + " Black plays the black markers, and the \nother, Red, plays the red. Black moves \n"
                     + "first and places one marker on any space \non the board. Red then places a marker \n"
                     + "on any unoccupied space; black does the \nsame; and so on until all eight markers \n"
                     + "are on the board. The object of the game \nis for either player to win by having all \n"
                     + "four of their markers in a straight line \n(vertical, horizontal, or diagonal) or on a \n"
                     + "square of four adjacent spaces. (Adjacency \nis horizontal, vertical, or diagonal, but \n"
                     + "does not wrap around the edges of the board.)\n If neither player has won after the drop \n"
                     + "(when all eight pieces are on the board), \nthen they move their pieces one at a time, \n"
                     + "with Black playing first. A piece may be \nmoved only to an adjacent space",
                     font=('Courier', 5, 'normal'))
        turtle.update()

    def buttonClick(self, x, y):

        if self.tilecount[0] < 8:
            if self.isblack == True:
                color_local = 'black'
            else:
                color_local = 'red'
        else:
            self.alltilesplaced = True

        # Each of 25 squares
        if x > -450 and x < -370:
            if y > -100 and y < -20:
                if not self.alltilesplaced:
                    if self.boardarray[(4, 0)] == -1:
                        self.draw_circle(-450, -100, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(4, 0)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(4, 0)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > -20 and y < 60:
                if not self.alltilesplaced:
                    if self.boardarray[(3, 0)] == -1:
                        self.draw_circle(-450, -20, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(3, 0)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(3, 0)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 60 and y < 140:
                if not self.alltilesplaced:
                    if self.boardarray[(2, 0)] == -1:
                        self.draw_circle(-450, 60, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(2, 0)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(2, 0)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 140 and y < 220:
                if not self.alltilesplaced:
                    if self.boardarray[(1, 0)] == -1:
                        self.draw_circle(-450, 140, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(1, 0)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(1, 0)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 220 and y < 300:
                if not self.alltilesplaced:
                    if self.boardarray[(0, 0)] == -1:
                        self.draw_circle(-450, 220, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(0, 0)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(0, 0)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

        if x > -370 and x < -290:
            if y > -100 and y < -20:
                if not self.alltilesplaced:
                    if self.boardarray[(4, 1)] == -1:
                        self.draw_circle(-370, -100, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(4, 1)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(4, 1)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > -20 and y < 60:
                if not self.alltilesplaced:
                    if self.boardarray[(3, 1)] == -1:
                        self.draw_circle(-370, -20, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(3, 1)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(3, 1)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 60 and y < 140:
                if not self.alltilesplaced:
                    if self.boardarray[(2, 1)] == -1:
                        self.draw_circle(-370, 60, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(2, 1)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(2, 1)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 140 and y < 220:
                if not self.alltilesplaced:
                    if self.boardarray[(1, 1)] == -1:
                        self.draw_circle(-370, 140, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(1, 1)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(1, 1)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 220 and y < 300:
                if not self.alltilesplaced:
                    if self.boardarray[(0, 1)] == -1:
                        self.draw_circle(-370, 220, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(0, 1)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(0, 1)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

        if x > -290 and x < -210:
            if not self.alltilesplaced:
                if y > -100 and y < -20:
                    if self.boardarray[(4, 2)] == -1:
                        self.draw_circle(-290, -100, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(4, 2)] = self.isblack
                        self.isblack = not self.isblack
            else:
                thispiececolor = self.boardarray[(4, 2)]
                if thispiececolor != -1:
                    print("There is a piece here")
                    turtle.write('There is a piece here')
                else:
                    print("There is NOT a piece here")
                    turtle.write('There is NOT a piece here')

            if y > -20 and y < 60:
                if not self.alltilesplaced:
                    if self.boardarray[(3, 2)] == -1:
                        self.draw_circle(-290, -20, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(3, 2)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(3, 2)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 60 and y < 140:
                if not self.alltilesplaced:
                    if self.boardarray[(2, 2)] == -1:
                        self.draw_circle(-290, 60, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(2, 2)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(2, 2)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 140 and y < 220:
                if not self.alltilesplaced:
                    if self.boardarray[(1, 2)] == -1:
                        self.draw_circle(-290, 140, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(1, 2)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(1, 2)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 220 and y < 300:
                if not self.alltilesplaced:
                    if self.boardarray[(0, 2)] == -1:
                        self.draw_circle(-290, 220, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(0, 2)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(0, 2)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

        if x > -210 and x < -130:
            if not self.alltilesplaced:
                if y > -100 and y < -20:
                    if self.boardarray[(4, 3)] == -1:
                        self.draw_circle(-210, -100, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(4, 3)] = self.isblack
                        self.isblack = not self.isblack
            else:
                thispiececolor = self.boardarray[(4, 3)]
                if thispiececolor != -1:
                    print("There is a piece here")
                    turtle.write('There is a piece here')
                else:
                    print("There is NOT a piece here")
                    turtle.write('There is NOT a piece here')

            if y > -20 and y < 60:
                if not self.alltilesplaced:
                    if self.boardarray[(3, 3)] == -1:
                        self.draw_circle(-210, -20, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(3, 3)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(3, 3)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 60 and y < 140:
                if not self.alltilesplaced:
                    if self.boardarray[(2, 3)] == -1:
                        self.draw_circle(-210, 60, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(2, 3)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(2, 3)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is a piece here')

            if y > 140 and y < 220:
                if not self.alltilesplaced:
                    if self.boardarray[(1, 3)] == -1:
                        self.draw_circle(-210, 140, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(1, 3)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(1, 3)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 220 and y < 300:
                if not self.alltilesplaced:
                    if self.boardarray[(0, 3)] == -1:
                        self.draw_circle(-210, 220, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(0, 3)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(0, 3)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

        if x > -130 and x < -50:
            if y > -100 and y < -20:
                if not self.alltilesplaced:
                    if self.boardarray[(4, 4)] == -1:
                        self.draw_circle(-130, -100, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(4, 4)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(4, 4)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > -20 and y < 60:
                if not self.alltilesplaced:
                    if self.boardarray[(3, 4)] == -1:
                        self.draw_circle(-130, -20, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(3, 4)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(3, 4)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 60 and y < 140:
                if not self.alltilesplaced:
                    if self.boardarray[(2, 4)] == -1:
                        self.draw_circle(-130, 60, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(2, 4)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(2, 4)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 140 and y < 220:
                if not self.alltilesplaced:
                    if self.boardarray[(1, 4)] == -1:
                        self.draw_circle(-130, 140, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(1, 4)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(1, 4)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

            if y > 220 and y < 300:
                if not self.alltilesplaced:
                    if self.boardarray[(0, 4)] == -1:
                        self.draw_circle(-130, 220, color_local)
                        self.tilecount[0] += 1
                        self.boardarray[(0, 4)] = self.isblack
                        self.isblack = not self.isblack
                else:
                    thispiececolor = self.boardarray[(0, 4)]
                    if thispiececolor != -1:
                        print("There is a piece here")
                        turtle.write('There is a piece here')
                    else:
                        print("There is NOT a piece here")
                        turtle.write('There is NOT a piece here')

        # Show rules
        if x > 200 and x < 300 and y > 250 and y < 270:
            self.showrules()

    def stop(self):
        turtle.done()


game = Teeko()
game.stop()

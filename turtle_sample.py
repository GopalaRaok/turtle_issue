# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:43:39 2019

@author: Ashika Devaguptapu
"""
import turtle
import math
window = turtle.Screen()
window.bgcolor("black")
window.title("A maze Game")
window.setup(700,700)
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color("blue")
        self.penup()
        self.speed(0)
    def playerUp(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()+24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def playerDown(self):
        move_to_x=player.xcor()
        move_to_y=player.ycor()-24
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)

    def playerRight(self):
        move_to_x=player.xcor()+24
        move_to_y=player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
            

    def playerLeft(self):
        move_to_x=player.xcor()-24
        move_to_y=player.ycor()
        if (move_to_x,move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
    def is_collision(self,other):
       a=self.xcor() - other.xcor()
       b=self.ycor() - other.ycor()
       distance = math.sqrt((a*2)+(b*2))
       if distance < 5:
           return True
       else:
           return False
class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self,x,y)
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)
        
    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()
        
levels=[""]
level_1=['XXXXXXXXXXXXXXXXXXXXXXXXX',
            'XP XXXXXXX          XXXXX',
            'X  XXXXXXX  XXXXXX  XXXXX',
            'X       XX  XXXXXX  XXXXX',
            'X       XX  XXX        XX',
            'XXXXXX  XX  XXX        XX',
            'XXXXXX  XX  XXXXXX  XXXXX',
            'XXXXXX  XX    XXXX  XXXXX',
            'X  XXX        XXXXT XXXXX',
            'X  XXX  XXXXXXXXXXXXXXXXX',
            'X         XXXXXXXXXXXXXXX',
            'X                XXXXXXXX',
            'XXXXXXXXXXXX     XXXXX  X',
            'XXXXXXXXXXXXXXX  XXXXX  X',
            'XXXT XXXXXXXXXX         X',
            'XXX                    TX',
            'XXX         XXXXXXXXXXXXX',
            'XXXXXXXXXX  XXXXXXXXXXXXX',
            'XXXXXXXXXX             TX',
            'XX   XXXXX              X',
            'XX   XXXXXXXXXXXXX  XXXXX',
            'XX     XXXXXXXXXXX  XXXXX',
            'XX          XXXX        X',
            'XXXX                    X',
            'XXXXXXXXXXXXXXXXXXXXXXXXX'
         ]


        
treasure_list=[""]      
levels.append(level_1)
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character=level[y][x]
            screen_x=-288+(x*24)
            screen_y=288-(y*24)
            if character =="X":
                pen.goto(screen_x,screen_y)
                pen.stamp()
                walls.append((screen_x,screen_y))
            if character =="P":
                player.goto(screen_x,screen_y)
            if character =="T": 
               treasure_list.append(Treasure(screen_x,screen_y))
        
pen=Pen()
player=Player()
#treasure=Treasure()
walls=[]
setup_maze(levels[1])
turtle.listen()
turtle.onkey(player.playerLeft,"Left")
turtle.onkey(player.playerRight,"Right")
turtle.onkey(player.playerUp,"Up")
turtle.onkey(player.playerDown,"Down")
window.tracer(0)
while True:
    for treasure in treasure_list:
        if player.is_collision(treasure):
            player.gold = treasure.gold+player.gold
        print("Player Gold: {}".format(player.gold))
        treasure.destroy()
        treasure_list.remove(treasure)
    window.update()

        

# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:10:04 2020

@author: SARVESH
"""
#part one
import turtle
import time
import random

delay = 0.1
score=0
high_score=0


window = turtle.Screen()
window.title("Snake game by Sarvesh")
window.bgcolor("green")
window.setup(width=500, height=500)
window.tracer(0)#turns of the scree update

#part two
head =turtle.Turtle()
head.speed(0)#fastest animation speed
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"


# Snake food

food=turtle.Turtle()
food.speed(0)#fastest animation speed
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,215)
pen.write("Score: 0  High Score: 0",align="center",font=("Courier",24,"normal"))



segments=[]



#functions 
def go_up():
    if head.direction !="down":
        head.direction="up"
    
def go_left():
    if head.direction!="right":
        head.direction="left"
    
def go_down():
    if head.direction!="up":
        head.direction="down"
    
def go_right():
    if head.direction!="left":
        head.direction="right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)   
        
#key Bindings
        
window.listen()
window.onkeypress(go_up,"Up")
window.onkeypress(go_right,"Right")
window.onkeypress(go_left,"Left")
window.onkeypress(go_down,"Down")
        
        
        
        
        
        
#main game loop
while True:
    window.update()
    # check for a collision with the border
    if head.xcor()>240 or head.xcor()<-240 or head.ycor()>240 or head.ycor()<-240:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)
            
        #clear the segments list
        segments.clear()
        #reset score
        score=0
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        #reset the delay
        delay=0.1
    
    # check for a collison for food
    if head.distance(food)<20:
        #move the food to random postion
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        food.goto(x,y)
        
        #add segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        
        #shorten te delay
        delay-=0.001
        #help to make the game hard
        
        #increase score
        score += 10
        
        if score>high_score:
            high_score=score
        
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
        
        
    #move the end segments first in reverse order
    
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
        
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
        
    move()       
    #check for head collision with the body

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            
            #clear the segments list
            segments.clear()
            #reset the code
            score=0
            pen.clear()
            pen.write("Score:{}  High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
            # reset the delay
            delay=0.1
    

            
            
    time.sleep(delay)

window.mainloop()
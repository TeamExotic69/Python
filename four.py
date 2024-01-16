'''# importing the necessary packages
import time
import sys
import os
  
# Function for implementing the loading animation
def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "starting your console application..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
  
# Driver program
if __name__ == '__main__': 
    load_animation()'''
  























'''
# Your desired code continues from here 
# s = input("Enter your name: ")
s ="Anurag"
sys.stdout.write("Hello "+str(s)+"\n")

# required modules
import turtle
#from turtle import * from random import randint
#from randint 
import random   
      
# classic shape turtle
speed(0)
penup()
goto(-140, 140)
   
# racing track
  
for step in range(15):
    write(step, align ='center')
    right(90)
      
    for num in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
          
    penup()
    backward(160)
    left(90)
    forward(20)
  
# first player details
player_1 = Turtle()
player_1.color('red')
player_1.shape('turtle')
   
# first player proceeds to racing track
player_1.penup()
player_1.goto(-160, 100)
player_1.pendown()
   
# 360 degree turn
for turn in range(10):
    player_1.right(36)
  
# second player details
player_2 = Turtle()
player_2.color('blue')
player_2.shape('turtle')
   
# second player enters in the racing track
player_2.penup()
player_2.goto(-160, 70)
player_2.pendown()
   
# 360 degree turn
for turn in range(72):
    player_2.left(5)
  
# third player details
player_3 = Turtle()
player_3.shape('turtle')
player_3.color('green')
   
# third player enters in the racing track
player_3.penup()
player_3.goto(-160, 40)
player_3.pendown()
   
# 360 degree turn
for turn in range(60):
    player_3.right(6)
  
# fourth player details
player_4 = Turtle()
player_4.shape('turtle')
player_4.color('orange')
   
# fourth player enters in the racing track
player_4.penup()
player_4.goto(-160, 10)
player_4.pendown()
   
# 360 degree turn
for turn in range(30):
    player_4.left(12)
  
# turtles run at random speeds
for turn in range(100):
    player_1.forward(randint(1, 5))
    player_2.forward(randint(1, 5))
    player_3.forward(randint(1, 5))
    player_4.forward(randint(1, 5))'''


























'''
import time
import datetime as dt
import turtle
  
     
# create a turtle to distplay time
t = turtle.Turtle()
 
# create a turtle to create rectangle box
t1 = turtle.Turtle()
 
# create screen
s = turtle.Screen()
 
# set background color of the screen
s.bgcolor("grey")
  
# obtain current hour, minute and second
# from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(7)
t1.color('yellow')
t1.penup()
  
# set the position of turtle
t1.goto(-20, 0)
t1.pendown()
  
# create rectangular box
for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)
     
# hide the turtle
t1.hideturtle()
 
while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hr).zfill(2)
            +":"+str(min).zfill(2)+":"
            +str(sec).zfill(2),
            font =("Arial Narrow", 35, "bold"))
    time.sleep(1)
    sec+= 1
     
    if sec == 60:
        sec = 0
        min+= 1
     
    if min == 60:
        min = 0
        hr+= 1
     
    if hr == 13:
        hr = 1'''

























'''

# Python program to create a
# a new window using Tkinter
# importing the required libraires
import tkinter

# creating a object 'top' as instance of class Tk
top = tkinter.Tk()

# This will start the blank window
top.mainloop()

# Python program to illustrate a stop watch
# using Tkinter
#importing the required libraries
import tkinter as Tkinter
from datetime import datetime
counter = 66600
running = False
def counter_label(label):
    def count():
        if running:
            global counter
    
            # To manage the intial delay.
            if counter==66600:          
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string
    
            label['text']=display # Or label.config(text=display)
    
            # label.after(arg1, arg2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count)
            counter += 1
    
    # Triggering the start of the counter.
    count() 
    
# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    
# Stop function of the stopwatch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
    
# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600
    
    # If rest is pressed after pressing stop.
    if running==False:  
        reset['state']='disabled'
        label['text']='Welcome!'
    
    # If reset is pressed while the stopwatch is running.
    else:               
        label['text']='Starting...'
    
root = Tkinter.Tk()
root.title("Stopwatch")
    
# Fixing the window size.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")
root.mainloop()
'''











'''

# import package
import turtle

# create a Screen Object
screen = turtle.Screen()

# Screen configuration
screen.setup(500, 500)

# Make turtle Object
clk = turtle.Turtle()

# set a Turtle object color
clk.color('black')

# set a Turtle object width
clk.width(4)


def draw_hour_hand():
    clk.penup()
    clk.home()
    clk.right(90)
    clk.pendown()
    clk.forward(100)


# value for numbers in clock
val = 0

# loop for print clock numbers
for i in range(12):
    # increment value by 1
    val += 1

    # move turtle in air
    clk.penup()

    # for circular motion
    clk.setheading(-30 * (i + 3) + 75)

    # move forward for space
    clk.forward(22)

    # move turtle to surface
    clk.pendown()

    # move forward for dash line
    clk.forward(15)

    # move turtle in air
    clk.penup()

    # move forward for space
    clk.forward(20)

    # write clock integer
    clk.write(str(val), align="center",
              font=("Arial",
                    12, "normal"))

# colored centre by setting position
# sets position of turtle at given position
clk.setpos(2, -112)
clk.pendown()
clk.width(2)

# To fill color green
clk.fillcolor('black')

# start filling
clk.begin_fill()

# make a circle of radius 5
clk.circle(5)

# end filling
clk.end_fill()

clk.penup()
draw_hour_hand()
clk.setpos(-20, -64)
clk.pendown()
clk.penup()

# Write Clock by setting position
clk.setpos(-30, -170)
clk.pendown()
clk.write(' 009 Clock', font=("Arial", 14,
                              "normal"))
clk.hideturtle()
turtle.done()
'''















'''
import turtle


# getting a Screen to work on
ws=turtle.Screen()

# Defining Turtle instance
t=turtle.Turtle()

# setting up turtle color to green
t.color("Green")

# Setting Up width to 2
t.width("2")

# Setting up speed to 2
t.speed(2)

# Loop for making outside square of
# length 300
for i in range(4):
    t.forward(300)
    t.left(90)


# code for inner lines of the square
t.penup()
t.goto(0,100)
t.pendown()

t.forward(300)

t.penup()
t.goto(0,200)
t.pendown()

t.forward(300)

t.penup()
t.goto(100,0)
t.pendown()

t.left(90)
t.forward(300)

t.penup()
t.goto(200,0)
t.pendown()


t.forward(300)'''

# import package and making object
import turtle


pen = turtle.Turtle()

# method to draw square with dots
# space --> distance between dots
# x  --> side of square
def draw(space,x):
    for i in range(x):
        for j in range(x):
            # dot
            pen.dot()
            # distance for another dot
            pen.forward(space)
            pen.backward(space*x)
            # direction
            pen.right(90)
            pen.forward(space)
            pen.left(90)
            # Main Section
            pen.penup()
            draw(10,8)
            # hide the turtle
            pen.hideturtle()
# import package and making object
import turtle


pen = turtle.Turtle()

# method to draw rectangle with dots
# space --> distance between dots
# x  --> height of rectangle
# y  --> width of rectangle
def draw(space,x,y):
    for i in range(x):
        for j in range(y):

            # dot
            pen.dot()
            # distance for another dot
            pen.forward(space)
            pen.backward(space*y)
            # direction
            pen.right(90)
            pen.forward(space)
            pen.left(90)
            # Main Section
            pen.penup()
            draw(10,5,12)
            # hide the turtle
            pen.hideturtle()
            # import package and making object
            import turtle
            pen = turtle.Turtle()
            # method to draw diamond with dots
            # space --> distance between dots
            # x  --> side of diamond
            def draw(space,x):
                for i in range(x):
                    for j in range(x):
                        # dot
                        pen.dot()
                        # distance for another dot
                        pen.forward(space)
                        pen.backward(space*x)
                        # direction
                        pen.right(90)
                        pen.forward(space)
                        pen.left(90)
                        #Main Section
                        pen.penup()
                        # direction to form diamond
                        pen.left(45)
                        draw(10,8)
                        # hide the turtle
                        pen.hideturtle()








# Python program to draw square
# using Turtle Programming
import turtle
#turtle.pencolor('red')
#turtle.fillcolor("yellow")
skk = turtle.Turtle()
ssk=turtle.Turtle()
ss=turtle.Turtle()
sk1 = turtle.Turtle()
sk = turtle.Turtle()
ss1=turtle.Turtle()
#ass=turtle.Turtle()
#ass.dot(0.67)
#turtle.shapesize(10,5,1)
#turtle.color('white',"brown")
turtle.bgcolor("pink")
#turtle.shape("circle")

'''
c = turtle.clone()
turtle.color("magenta")
c.color("red")
turtle.circle(100)
c.circle(90)
turtle.circle(80)
c.circle(70)
turtle.circle(60)
c.circle(50)
turtle.circle(40)
c.circle(30)
turtle.circle(20)
c.circle(10)


for i in range(300):
    ssk.forward(180)
    ssk.right(177)
    ssk.speed(0)

for i in range(200):
   skk.forward(500)
    skk.right(-580.290)
    skk.speed(0)
for i in range(600):
    ss1.forward(1800)
    ss1.right(98)
    ss1.speed(0)

for i in range(200):
    sk1.forward(100)
    sk1.right(-80.290)
    sk1.speed(0)
for i in range(200):
    sk.forward(100)
    sk.right(80.290)
    sk.speed(0)



for i in range(600):
    ss.forward(1800)
    ss.right(-98)
    ss.speed(0)
'''





player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

die = [1,2,3,4,5,6]

for i in range(20):
    if (player_one.pos()) >= (300,100):
        print("Player One Wins!")
        break
    elif (player_two.pos()) >= (300,-100):
        print("Player Two Wins!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        player_two_turn = input("Press 'Enter' to roll the die ")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)



turtle.done()

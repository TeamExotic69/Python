'''
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












import turtle
import random
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


















# importing the necessary packages
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
    load_animation()
  

























# Your desired code continues from here
# s = input("Enter your name: ")
s = ("Anurag")
#sys.stdout.write("Hello" +str(s)+ "\n")

# required modules
import turtle
from turtle import *
from random import randint 
import random   
      
# classic shape turtle
turtle.speed(0)
turtle.penup()
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
    player_4.forward(randint(1, 5))








# importing the necessary packages
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
    load_animation()
'''


'''
print("\U0001F987")
print("\U0001F917")#SLIMYwithHANDS
print("\U0001F918")
print("\U0001F919")
print("\U0001F920")
print("\U0001F921")
print("\U0001F922")
print("\U0001F923")
print("\U0001F924")
print("\U0001F925")
print("\U0001F926")
print("\U0001F927")
print("\U0001F928")
print("\U0001F929")
print("\U0001F930")
print("\U0001F931")
print("\U0001F932")
print("\U0001F933")
print("\U0001F934")
print("\U0001F935")
print("\U0001F936")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F917")
print("\U0001F602")
print("\U0001F601")
print("\U0001F150")
print("\U0001F130")
print("\U0001F122")
'''
#01
'''for row in range(1,11):
    for col in range(1,10):
        prod=row*col
        if prod < 10:
            print('',prod,'',end=' ') 
        else:
            print(prod,'',end=' ')
    print() 
'''
#02
'''To=30
for K in range(0,To):
    if K%4==0:
        print(K*4)
    else:
        print(K+3)
'''
#03
'''
for name in ['jayes','Ramya','taruna','suraj']:
    print(name)
    if name[0]=='s':
        break
    else:
        print('Finished!')
        break
    break
print('Got it!')'''
#04
'''m=3
n=5
while n<10:
    m=n-1
    n=2*n-m
    print(n,m)
    break
'''
#05
'''limit=float(input("Enter the limit:"))
max_price=0
next_price=float(input("Enter a price or 0 to stop:"))
while next_price>0:
    print(next_price)
    next_price=float(input("Enter next price:"))
    break
if max_price>0:
    print(max_price)
else:
    print("Nothing")
'''
#06
'''
line=input("Enter a line:")
lowercount=uppercount=0
digitcount=alphacount=0
for a in line:
    if a.islower():
        lowercount +=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphacount+=1
print("Number of uppercase letters:",uppercount)
print("Number of lowercase letters:",lowercount)
print("Number of alphabets:",alphacount)
print("Number of digits:",digitcount)'''

#07
'''
from turtle import *
color('red')
begin_fill()
pensize(3)
left(50)
forward(113)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()'''

#08
'''
def oct2others(n):
    print("Passed octal number:",n)
    numString=str(n)
    decNum=int(numString,8)
    print("Number in Decimal:", decNum)
    print("Number in Binary:", bin(decNum))
    print("Number in Hexadecimal:", hex(decNum))

num = int(input("Enter an octal number:"))
oct2others(num)'''

#09
#from turtle import dot, st
'''
def retSeries(init,step):
    return init,init+step,init+2*step,init+3*step

ini =int(input("Enter initial value of the AP series:"))
st= int(input("Enter step value of the AP seies:"))
print("Series with initial value",ini,"& step value",st,"goes as:")
t1,t2,t3,t4=retSeries(ini,st)
print(t1,t2,t3,t4)'''

#rewrite 
'''
l=range(0,17)
with open("student","wb") as bin_file:
    print(bytes(l))
    bin_file.write(bytes(l))
'''

#10
'''
n=6
if n%2==0 and n%3==0:
     print("BuzzFizz!",end='')
elif n%2==0:
    print("Buzz",end='')
elif n%3==0:
    print("Fizz!")'''

#11
'''
ans=0
for i in range(11,20,1):
    if i%2==0:
        ans+=5
    else:
        ans+=2
print(ans)'''

#12
'''
ans=20
while ans<50:
    if ans%10==0:
        ans+=5
    elif ans%5==0:
        ans+=10
    else:
        ans+=15
print(ans)'''

#13
'''
l=[7,12,16,5,4,28,25]
n=l[0]
for i in range(len(l)-1):
    l[i]=l[i+1]
l[i+1]=n
print(l)'''

#14
'''l=[7,12,16,5,4,28,25,30]
print(l)
for i in range(0,len(l)-1,2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)
'''

#15
'''
word="CBSE 2021"
for alpha in word[3:9]:
    print('Study')
    '''

#16
'''def study(n):
    ans=0
    for i in range(1,n):
        ans+=i
    return ans
print(study(5))
'''

#17
'''def f(n):
    if n==1:
        return 1
    else:
        return n*f(n-1)
'''
#18
'''
def f():
    num = int ( input("Enter a number(0..999):"))
    if num<0:
        print("Invalid enter, Valid entry range is 0 to 999.")
    elif num <10:
        print("Single digit number is entred")
    elif num <100:
        print("Two digit number is entereed")
    elif num <=999:
        print("Three digit number is entred")
    else:
        print("Tnvalid entry, valid range is 0 to 999.")
 
for i in range (10):
    i=f()
'''
#19
'''
for i in range(15,21):
    print("Cube of number",i,end=' ')#end (add the print statements with space in single quorts )
    print("is",i**3)
    '''

#20
'''
for i in range(1,10):
    print("square root of ",i,"is",(i**0.5))
'''

#21
'''
arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for i in range(0,6):
    print(arr[i],end=" ")
    '''
    
#22
'''
def arCalc(x,y):
    return x+y, x-y, x*y, x/y, x%y
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
add , sub, mult, div, mod = arCalc(num1,num2)
print("Sum of given numbers:", add)
print("Substraction of given numbers:", sub)
print("Product of given numbers:", mult)
print("Division of given numbers:", div)
print("Modulo of given numbers:", mod)
'''

#23
'''
def myFunc1(a):
    print("\t Inside myFunc1()")#\t ==> tab
    print("\t Value recived in 'a' as", a)
    a=a+2
    print("\t Value of 'a' now changes to",a)
    print("\t Returning from myFunc1()")

num=3
print("Calling myFunc1() by passing 'num' is", num)
myFunc1(num)
print("back from myFunc1(). Value of 'num' is", num)'''

#24
'''def power(b,p):
    y=b**p
    return y

def calcSquare(x):
    a=power(x,2)
    return a

n=5 
result = calcSquare(n)+power(3,3)
print(result)
'''
#25
'''
obj = open("New.txt","w")
obj.write("A poem by paramhansa yogananda ")
obj.write("Better than Heaven or Arcadia")
obj.write("I Love Thee, O my India!")
obj.write("And they love I shell give")
obj.write("To even brother nation that lives.")
obj.close()
obj1=open("New.txt","r")
s1=obj1.read(49)
print(s1)
obj1.close()'''

#26
'''
f=open("New.txt","r")
for line in f:
    words = line.split()
    for i in words:
        for letter in i:
            if(letter.isdigit()):
                print(letter)'''

#27
'''
def displayMeMy():
    num=0
    f=open("New.txt","rt")         
    n=f.read()
    m=n.split()
    for x in m:
        if  x=="Me" or x=="My":
            print(x)
            num=num+1
    f.close()
    print("count of Me/My in file:",num)'''

#28
'''
k=open("New.txt","w")
for i in range(5):
    name = input("Enter name of student:")
    k.write(name)
k.close()'''

#29
'''
count = int(input("How many students are there in the class?"))
f= open("New.txt","w")
for i in range(count):
    print("Enter details for students ",(i+i),"below :")

    rollno=int(input("Rollno:"))
    name= input("Name :")
    marks =float(input("Marks :"))
    rec = str(rollno) +","+ str(name)+'\n'
    f.write(rec)
f.close()'''

#30
'''
my_points={'a':(4,3),'b':(1,2),'c':(5,1)}
highest=[0,0]
init=0
for a in range(2):
    init=0
    for b in my_points.keys():
        val = my_points[b][a]
        if init==0:
            highest[a]=val
        init+=1
        if val>highest[a]:
            highest[a]=val
    print("Maximum value at index(my_points,",a,")=",highest[a])'''

'''p=['w','p','y','h','b','m','fg','fghj','edvbj','123456789','1234','98765432','anu','Anuy']
print(p)
p.sort()
p.remove('98765432')
print(p)
p.clear()
print(p,'clear')
o=[1,4,4,2,4,6,6,7,8,9,2,7,4,5,7,9,6,5,2,0]
i=o.count(4)
print(o)
o.reverse()
o.remove(4)
o.remove(4)
o.remove(4)
o.remove(4)
print(o)
print(i)
'''



'''with open("desktop\\dlip(ch01)QnA.txt","r") as file:
    data=file.read(200)
    print(data)
    data=file.readlines(200)#print the file as a list (whole file)
    print(data)
    data=file.readline(2)#read only one line 
    print(data)
    #print(file.closed) SINCE THIS STATEMENT IS IN THE INDENTATION SO THIS DOESN'T RETURN TRUE
print(file.closed)
'''



'''p=open("C:\\Users\\Anurag\\Desktop\\asit.txt","r")
l=p.readlines()
print(l)
'''


'''
import pickle
emp1={'Empno':12001,'Name':'Anu','Age':25,'Salary':40000}
emp2={'Empno':13001,'Name':'Anuy','Age':24,'Salary':50000}
emp3={'Empno':12004,'Name':'Anurag','Age':25,'Salary':30000}
emp4={'Empno':13002,'Name':'Anuu','Age':21,'Salary':77000}
emp5={'Empno':12009,'Name':'Anup','Age':20,'Salary':67000}
emp6={'Empno':11001,'Name':'Anukrat','Age':19,'Salary':90000}
emp7={'Empno':17001,'Name':'Anuskha','Age':20,'Salary':10000}
empfile=open('Emp.dat','wb')
pickle.dump(emp1,empfile)
pickle.dump(emp2,empfile)
pickle.dump(emp3,empfile)
pickle.dump(emp4,empfile)
pickle.dump(emp5,empfile)
pickle.dump(emp6,empfile)
pickle.dump(emp7,empfile)
print("Sucessfully written seven dictionaries") 
print("File pointer is at :",empfile.tell())  
empfile.close()'''



'''
y= str(123)
x="hello"*3
print(x,y)
x="hellow"+"world"
y=len(x)
print(y,x)
    '''                        
'''
#Flush()   method remove all the data present in your file
MYMFILE=open("C:\\Users\\Anurag\\Desktop\\asit.txt","r")
#o=MYMFILE.read()
#print(o)
#MYMFILE.flush()
t=MYMFILE.readline.rstrip('\n')
print(t)
#print(MYMFILE.read())
for i in range(5):
    name=input("Enter name of the student:")
    MYMFILE.write('\n'+name)
    #MYMFILE.write('\n')
#p=MYMFILE.read()
#print(o)
MYMFILE.close()
'''
 
'''import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=36
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    t.color(c)
    t.left(10)
    for j in range(5):
        t.forward(200)
        t. left(144)









Stack=[]
top=None 
while True:
    print("STACK OPERATIONS")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display stack")
    print("5.Exit") 
    ch=int(input("Enter your choice (1-5) :"))
    if ch==1:
        item=int(input("Enter item:"))
        Push(Stack,item)
    elif ch==2:
        item=pop(Stack)
        if item=="Underflow":
            print("Underflow! stack is empty!")
        else:
            print("Popped items is", item)
    elif ch==3:
        item=peek(Stack)
        if item=="Underflow":
            print("Underflow Stack is empty!")
        else:
            print(Topmost item is),item
    elif ch==4:
        Display(Stack)
    elif ch==5:
        break
    else:
        print("Invalid choice!")
'''     


from telnetlib import PRAGMA_HEARTBEAT
from turtle import st


s = []
top=None
def isEmpty(stk):
    if(stk==[]):
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if(isEmpty(stk)):
        return("Underflow!")
    else:
        i=stk.pop()
        if(len(stk)==0):
            top=None
        else:
            top=top-1
    return i
    

def peek(stk):
    if(isEmpty(stk)):
        return('Underflow!')
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if(isEmpty(stk)):
        print('stack is empty!')
    else:
        top=len(stk)-1
        print(stk[top],'<----top')
        for i in range(top-1,-1,-1):
            print(stk[i])


print('STACK IMPLEMENTATION')
print('1. Push')
print('2. Pop')
print('3. Peek')
print('4. Display')
print('5. Exit')
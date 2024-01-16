'''name=input("enter the name of person")
age=input("enter the age of person")
f=open("")'''


'''
x=5
def func(a):
    b=a+1
    return b

y=int(input("Enter number:"))
z=y+func(x)
print(z)


#non-fruitful function (Void function)
def replicate():
    return "&&&"

print(replicate())

e=26**3
print(e)



def squared(x,y,z):
    return x*x, y*y, z*z

t=squared(2,3,4)
print(t)



def arCalc(x,y):
    return x+y, x-y, x*y, x/y, x%y

num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
add,sub,mult,div,mod=arCalc(num1,num2)
print("Sum of given numbers:",add)
print("subtraction of given numbers:",sub)
print("product of given numbers:",mult)
print("division of given numbers:",div)
print("Modulo of given numbers:",mod)


x=5
p=80
def func(a,d):
    b=a+d+1
    return b

y=(int(input("Enter number:")))
w=(int(input("enter number:")))
z=y+func(x)+func(p)
print(z)
   




   

import pickle
from sys import flags
record=[]
while True:
    roll_no=int(input("enter student roll no:"))
    name=input("enter student name:")
    marks=int(input("enter the marks obtained:"))
    date=[roll_no,name,marks]
    record.append(date)
    choice=input("wish to enter more records(Y/N)?:")
    if choice.upper()=='N':
        break
f=open("student","wb")
pickle.dump(record,f)
print("record added")
f.close()


#import pickle
f=open("student","rb")
stu=pickle.load(f)
print("the content of binary file is ")
for R in stu:
    roll_no=R[0]
    name=R[1]
    marks=R[2]
    print(roll_no,name,marks)
f.close()

                       
f=open("student","rb")
stu=pickle.load(f)
found=0
roll_no=int(input("enter the roll_no. to be searched:"))
for R in stu:
    if R[0]==roll_no:
        print("successfully search",R[1],R[2],"found")
        found=1
        break
if found==0:
    print("sorry, records are not found")
f.close()
     

#program to update the name of student in binary file
f=open("student","rb+")
stu=pickle.load(f)
found=0
rno=int(input("enter the roll_no. to be searched:"))
for R in stu:
    rno=R[0]
    if rno==roll_no:
        print("current name is:",R[1])
        R[1]=input("New Name:"); found=1
        break
if found==1:
    f.seek(0)
    pickle.dump(stu,f)
    print("Records are successfully updated")
f.close()
'''



































































'''
import os
import pickle
#Accepting data dor dictionary
def insertRec():
    rollno = int(input("Enter roll number:"))
    name=input("Enter Name:")
    marks=int(input("Enter Marks:"))
    #creatind the dictionary
    rec = {"Rollno": rollno, "Name": name, "Marks": marks}
    #Writing the dictionary
    f=open("student.dat","ab")
    pickle.dump(rec,f)
    f.close()

#Reading the records
def readRec():
    f = open("student.dat","rb")
    while True:
        try:
            rec = pickle.load(f)
            print("Roll Num:", rec['Rollno'])
            print("Name:", rec["Name"])
            print("Marks:", rec["Marks"])
        except EOFError:
            break
    f.close()

#Searching a record based on Rollno
def searchRollNo(r):
    f = open("student.dat","rb")
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['Rollno'] == r:
                print("Roll Num:", rec['Rollno'])
                print("Name:", rec["Name"])
                print("Marks:", rec["Marks"])
                flag=True
        except EOFError:
            break
    if flag == False:
        print("No Record Found")
    f.close()

#Marks Modification for a RollNo
def updateMarks(r,m):
    f = open("Student.dat","rb")
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    for i in range(len(reclst)):
        if reclst[i]['Rollno'] == r:
            reclst[i]['Marks'] = m
    f = open("student.dat", 'wb')
    for c in reclst:
        pickle.dump(x,f)
    f.close()

#Deleting a record based on RollNo.
def deleteRec(r):
    f=open("student.dat","rb")
    reclst=[]
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f=open("student.dat",'wb')
    for x in reclst:
        if x['Rollno']==r:
            continue
        pickle.dump(x,f)
    f.close()

while True:
    print('Type 1 to insert rec.')
    print('Type 2 to display rec.')
    print('Type 3 to search rec.')
    print('Type 4 to update rec.')
    print('Type 5 to delete rec.')
    print('Enter your choice 0 to exit')
    choice=int(input("Enter your choice:"))
    if choice == 0:
        break
    elif choice == 1:
        insertRec()
    elif choice == 2:
        readRec()
    elif choice == 3:
        r =int(input("Enter a rollno to search:"))
        searchRollNo(r)
    elif choice == 4:
        r= int(input("Enter a rollno:"))
        m=int(input("Enter new Marks:"))
        updateMarks(r,m)
    elif choice == 5:
        r=int(input("Enter a rollno:"))
        deleteRec(r)
    
'''

















'''
f=open('scgiil.txt','r')
print("before reading:",f.tell())
s=f.read()
print("after reading:",f.tell())
f.seek(0)
print("from beginning again:",f.tell())
s=f.read(4)
print("first four bytes are:",s)
print(f.tell())
s=f.read(3)
print("first three bytes",s)
print(f.tell())
f.close()
'''

























import csv
import imp
from io import UnsupportedOperation
'''f=open("C:\\Users\\Anurag\\Desktop\\student.csv")
csv_reader=csv.reader(f)
columns=next(csv_reader)
c = 0;
for row in csv_reader:
    c=c+1
print("No. of records are:",c)
#code004
obj=csv.reader(f)
for row in obj:
    print(row)
f.close()

#code005
with open("C:\\Users\\Anurag\\Desktop\\student.csv",'r') as csv_Anurag:
    reader=csv.reader(csv_Anurag)
    rows = []

    for rec in reader:
        rows.append(rec)
        print(rec)
#code006
f=open("C:\\Users\\Anurag\\Desktop\\student.csv",'r')
csv_reader=csv.reader(f)
csvRows = []
value = 0
for row in csv_reader:
    if csv_reader.line_num == 0:
        continue
    csvRows.append(row)
    value=len(list(csv_reader))
print("No. of records are :", value)
f.close()

#code006
f=open("C:\\Users\\Anurag\\Desktop\\student.csv",'r')
a=csv.reader(f)
for row in a:
    print(','.join(row))
f.close()

#code007
f=open("C:\\Users\\Anurag\\Desktop\\student.csv",'r')
a=csv.reader(f)
Name = input("Enter the name to be searched: ")
for row in a:
    if(row[0] == Name):
        print(row)
#code009
fields = ['Name','Class','Year','Percent']
rows = [
        ['Anurag','XII','2021','70'],
        ['Aman','XII','2021','99'],
        ['Ansh','XII','2020','89']
       ]
filename = "anuragyadav.csv"
with open(filename,'w',newline='') as f:
    csv_w=csv.writer(f,delimiter=',')
    csv_w.writerow(fields) 
    for i in rows:
        csv_w.writerow(i)
        print("file created")
#code010
fields = ['Name','Class','Year','Percent']
rows = [
        ['Anurag','XII','2021','70'],
        ['Aman','XII','2021','99'],
        ['Ansh','XII','2020','89']
       ]
filename = "anuy.csv"
with open(filename,'w',newline='') as f:
    csv_w=csv.writer(f,delimiter=',')
    csv_w.writerow(fields) 
    csv_w.writerows(rows)
    print("All rows written in one row")


#code011
def countH():
    f = open("scgiil.tx",'r')
    lines = 0
    l=f.readlines()#represent all lines 
    for i in l:
        if i[0]=='H':
            lines+=1
    print("No. of linesare:",lines)
'''















































'''
import os
import pickle
#Accepting data dor dictionary
def insertRec():
    rollno = int(input("Enter roll number:"))
    name=input("Enter Name")
    marks=int(input("Enter Marks:"))
    #creatind the dictionary
    rec = {"Rollno": rollno, "Name": name, "Marks": marks}
    #Writing the dictionary
    f=open("student.dat","ab")
    pickle.dump(rec,f)
    f.os.close()

#Reading the records
def readRec():
    f = open("student.dat","rb")
    while True:
        try:
            rec = pickle.load(f)
            print("Roll Num:", rec['Rollno'])
            print("Name:", rec["Name"])
            print("Marks:", rec["Marks"])
        except EOFError:
            break
    f.close()

#Searching a record based on Rollno
def searchRollNo(r):
    f = open("student.dat","rb")
    flag = False
    while True:
        try:
            rec = pickle.load(f)
            if rec['Rollno'] == r:
                print("Roll Num:", rec['Rollno'])
                print("Name:", rec["Name"])
                print("Marks:", rec["Marks"])
                flag=True
        except EOFError:
            break
    if flag == False:
        print("No Record Found")
    f.close()

#Marks Modification for a RollNo
def updateMarks(r,m):
    f = open("Student.dat","rb")
    reclst = []
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    for i in range(len(reclst)):
        if reclst[i]['Rollno'] == r:
            reclst[i]['Marks'] = m
    f = open("student.dat", 'wb')
    for c in reclst:
        pickle.dump(x,f)
    f.close()

#Deleting a record based on RollNo.
def deleteRec(r):
    f=open("student.dat","rb")
    reclst=[]
    while True:
        try:
            rec = pickle.load(f)
            reclst.append(rec)
        except EOFError:
            break
    f.close()
    f=open("student.dat",'wb')
    for x in reclst:
        if x['Rollno']==r:
            continue
        pickle.dump(x,f)
    f.close()

while True:
    print('Type 1 to insert rec.')
    print('Type 2 to display rec.')
    print('Type 3 to search rec.')
    print('Type 4 to update rec.')
    print('Type 5 to delete rec.')
    print('Enter your choice 0 to exit')
    choice=int(input("Enter your choice:"))
    if choice == 0:
        break
    elif choice == 1:
        insertRec()
    elif choice == 2:
        readRec()
    elif choice == 3:
        r =int(input("Enter a rollno to search:"))
        searchRollNo(r)
    elif choice == 4:
        r= int(input("Enter a rollno:"))
        m=int(input("Enter new Marks:"))
        updateMarks(r,m)
    elif choice == 5:
        r=int(input("Enter a rollno:"))
        deleteRec(r)
'''

















'''
def linearSearch(list, key): #function to perform the search
 for index in range(0,len(list)):
     if list[index] == key: #key is present 
         return index+1 #position of key in list
         return None #key is not in list
#end of function
list1 = [] #Create an empty list
maximum = int(input("How many elements in your list? "))
print("Enter each element and press enter: ") 
for i in range(0,maximum):
 n = int(input())
 list1.append(n) #append elements to the list 
print("The List contents are:", list1)
key = int(input("Enter the number to be searched:")) 
position = linearSearch(list1, key)
if position is None:
 print("Number",key,"is not present in the list") 
else:
 print("Number",key,"is present at position",position)
'''

'''
def binarySearch(list, key):
    first = 0
    last = len(list) - 1
    while(first <= last):
        mid = (first + last)//2
        if list[mid] == key:
            return mid
        elif key > list[mid]:
            first = mid + 1
        elif key < list[mid]:
            last = mid - 1
        return -1
numLIST = [] #Create an empty list
print ("Create a list by entering elements in ascending order")
print ("press enter after each element, press -999 to stop")
num = int(input())
while num!=-999:
    numLIST.append(num)
    num = int(input())
n = int(input("Enter the key to be searched: "))
pos = binarySearch(numLIST,n)
if(pos != -1):
    print( n,"is found at position", pos+1)
else:
    print (n,"is not found in the list ")'''




























'''
#math library
import math
print(math.floor(-100.012))

print(math.ceil(-100.012))
print(math.sqrt(100.012))
print(math.fabs(-100.012))
print(math.exp(-100.012))
print(math.log(100.012))
print(math.log(10))
print(math.floor(-100.012))
print(math.floor(-100.012))


for i in range(0,401):
    print(i)
    i+=1
a=0
while a<=400:
    print(a)
    a+=1
    break

abc = input("Enter a line:")
lowercase=0
uppercase=0
digitcount=0
alphabet=0
for a in abc:
    if a.islower():
        lowercase+=1
    elif a.isupper():
        uppercase+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphabet+=1
print("no. of loweletter",lowercase)
print("no. of upperletter",uppercase)
print("no. of digits",digitcount)
print("no. of alphabets",alphabet)

















for i in range(-10,0):
    print(i)
p=-10    
while p<0:
    print(p)
    p+=1
 


k="Hello\
 World"
print(k)

p=15
o=p-10
print(p+3)
if o > 5 : 
    print("Value of 'p' was more than 15 initially.")
else:
    print("value of'p'was 15 or less than initially.")
'''



'''
code = "powerful"
for ch in code:
    print(ch,'~')

print("power"+"Rangers")
print("anurag"*4)


def red():
    global x
    x=90
    return x
print()'''
#import turtle
#sc=turtle.Screen()
#sc.setup(6000,6000)
#spiral = turtle.Turtle()
#spiral.speed(10)
#sc.bgcolor("black")
#col =["yellow","blue","white","green"]
#c=0
#for i in range(500):
#    spiral.forward(i*10)
#    spiral.right(1440)
#    spiral.color(col[c])
#    if c==3:
#        c=0
#    else:
#        c+=1

'''
for( i = arr.length-1; i >=0 ; i--){
    print arr[i]
}




for(i=0; i < a.length/2 ; i--){
    temp = a[i];
    a[i] = a[a.length-i];
    a[a.length-i] = temp
}'''



'''
from  turtle import *
speed(0)
color('blue')
bgcolor('black')
b=100
while b>0:
    left(b)
    forward(b*0.00912342)
    b=b+0.09'''



'''
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()'''
'''
import pika, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)'''




'''
import random
import os
import re
os.system('cls' if os.name == 'nt' else 'clear')
while (1<2):
   print ("\n" )
   print ("Rock, Paper, Scissors - Shoot!")
   userChoice = raw_input("Choose your weapon [R]ock, [p]aper, or [s]cissors: ")
   if not re.match("[SsRrPp", userChoice):
       print("Please choose a letter:")
       print("[R]ock, [S]cissors or [P]aper.")
       continue
    // Echo the user's Choice
    print("You choose:" + userChoice)
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
print("I chose: " + opponenetChoice)
if opponenetChoice == str.upper(userChoice):
    print("Tie!")
    #if opponenetChoice == str("R") and str.upper(userChoice) == "p"
else opponenetChoice == 'R' and userChoice.upper() == 'S':

  print("Scissors beats rock, I win!")'''



'''
   
import random
score_player , score_computer = 0 ,0

while score_computer!=5 and score_player!=5:
    print("rock = 0, paper = 1, scice = 2")
    player = int(input("Choose:"))

    c = ["rock", "paper", "scice"]
    computer = random.choice(c)

    #draw
    if player == 0 and computer == "rock":
        print("Draw!")
        print(f"You:{score_player} - computer:{score_computer}")
        
    if player == 1 and computer == "paper":
        print("Draw!")
        print(f"You:{score_player} - computer:{score_computer}")

    if player == 2 and computer == "scice":
        print("Draw!")
        print(f"You:{score_player} - computer:{score_computer}")
        
    
    #player win
    if player == 0 and computer == "scice":
        score_player +=1
        print("Good!")
        print(f"You:{score_player} - computer:{score_computer}")
    if player == 1 and computer == "rock":
        score_player +=1
        print("Good!")
        print(f"You:{score_player} - computer:{score_computer}")
    if player == 2 and computer == "paper":
        score_player +=1
        print("Good!")
        print(f"You:{score_player} - computer:{score_computer}")

    #computer win
    if computer == "rock" and player == 2:
        score_computer +=1
        print("haha loser!")
        print(f"You:{score_player} - computer:{score_computer}")
    
    if computer == "paper" and player ==0:
        score_computer +=1
        print("haha loser!")
        print(f"You:{score_player} - computer:{score_computer}")
    
    if computer == "scice" and player == 1:
        score_computer +=1
        print("haha loser!")
        print(f"You:{score_player} - computer:{score_computer}")

if score_player == 5:
    print("You Win!")
else:
    print("computer Win :")

'''





from sketchpy import library as lib
obj=lib.rdj()
obj.draw()
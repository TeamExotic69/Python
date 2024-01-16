## Taking kilometers input from the user
#kilometers = float(input("Enter value in kilometers: "))
#
## conversion factor
#conv_fac = 0.621371
#
## calculate miles
#miles = kilometers * conv_fac
#'''Doubtdown''' print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
#print(kilometers,"kilometers is equal to",miles,"miles")
#
#
## Python Program to convert temperature in celsius to fahrenheit
#
## change this value for a different result
#celsius = 37.5
#
## calculate fahrenheit
#fahrenheit = (celsius * 1.8) + 32
#print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

##---------for only one word recognisastion----------
#p=[]
#if len(p)==0:
#	print(" you have an EmptyStack now")
#print("Add values to test this:-")
#for i in range(10):
#	u=str(input("Enter you stack value:"))
#	if u=='a':
#		print(p,"Your value is not valid")
#	elif u=='e':
#		print(p,"Your value is not valid")
#	elif u=='i':
#		print(p,"Your value is not valid")
#	elif u=='o':
#		print(p,"Your value is not valid")
#	elif u=='u':
#		print(p,"Your value is not valid")
#	elif True:
#		p.append(u)
#	elif len(p)==0:
#		print("EmptyStack")
#		
#	print(p)
##---------------------END-----------------------
#
#


#a=[]
#q=['a','e','i','o','u']
#for i in range(5):
#	u=str(input("Enter you stack value:"))
#	if q in a:
#		a.pop()
#	elif a[0]=='e':
#		a.pop()
#	elif a[0]=='i':
#		a.pop()
#	elif a[0]=='o':
#		a.pop()
#	elif a[0]=='u':
#		a.pop()
#	elif True:
#		a.append(u)
#		print(a)
#	print(a)


import random 
 
player_score,computer_score=0,0
c={1:'ROCK',2:'PAPER',3:'SCISSORS'}

while true:
	print("Choice=[1:'ROCK',2:'PAPER',3:'SCISSORS']")
	u=int(input('Choice:'))
	if choice=1 and computer='rock':
		  
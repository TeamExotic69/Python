#this is the example of empty statement
'''condition=True
while(condition==True):
	print("pass")
else:
	print(false)'''
#this will print infinity times
#print("Sum of 3 and 2 is:",2+3)
#print(3*1**3)
#name="Anuy"
#print("Greeting!!!")
#print("Hello",name)
#print("How do you do?")
#Value='Anurag'
#age=17
#print(name,",you are",17,"now but",end=' ')
#print("you will be ",age+1,"next year")
#miles=int(input("Enter miles:"))
#km=miles/0.621371
#print("miles:",miles)
#print("kilometer:",km)
#x=int(input('Enter value 1:'))
#y=int(input("Enter value 2:"))
#summ=x+y
#diff=x-y
#mult=x*y
#div=x/y
#mod=x%y
#print("Numbers are:",x,y)
#print("summ:",summ)
#print("difference:",diff)
#print("multiply:",mult)
#print("Divide:",div)
#print("Modulas:",mod)




height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
bmi = weight/(height**2) 
print("Your BMI is: {0} and you are: ".format(bmi), end='')
if ( bmi < 16):
   print("severely underweight")

elif ( bmi >= 16 and bmi < 18.5):
   print("underweight")

elif ( bmi >= 18.5 and bmi < 25):
   print("Healthy")

elif ( bmi >= 25 and bmi < 30):
   print("overweight")

elif ( bmi >=30):
   print("severely overweight")







cels=float(input("Enter temp in cels:"))
print("Temperature in cels:", cels)
fahr=cels*9/5+32
print("Temperature in fahrenhite is:", fahr)











     
yup=float(input("Enter temp. in fah:"))
print("Temperature in frh",yup)
cel=(yup-32)*5/9
print("temperature in cel:",cel)















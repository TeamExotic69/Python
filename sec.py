name=input("enter your name:")
marks = float(input("Enter marks:"))
print(name)
print(marks)
print(type(name))
print(type(marks))
message=input("Enter welcome message:")
print("Hello,",message)
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
sum=num1+num2+num3
print("Three number are:",num1,num2,num3)
print("sum is :", sum)
length=float(input("Enter length of the rectangle:"))
breath=float(input("Enter breath of the rectangle:"))
area=length*breath
print("rectangle specifications")
print("length=",length,end='')
print("breath=",breath)
print("Area=", area)
weight_in_kg=float(input("Enter weight in kg:"))
height_in_meter=float(input("Enter height  in meter:"))
bmi=weight_in_kg/(height_in_meter*height_in_meter)
print("BMI is :",bmi)
if bmi>=25:
    print("Over weight")
else:

	print("Normal")	
num=int(input("Enter a number:"))
cube=num**3
print("It's cube is:",cube)
km=int(input("Enter kilometers:"))
miles=km*0.621371
print("kilometers:",km)
print("miles:",miles)
tonnes=float(input("Enter tonnes:"))
quintals=tonnes*10
kgs=quintals*100
print("tonnes:",tonnes)
print("quintals:",quintals)
print("kilograms:",kgs)
n1=int(input("Enter number1:"))
n2=int(input("Enter number2:"))
print("Original numbers:",n1,n2)
n1,n2=n2,n1
print("After swapping:",n1,n2)
cels=float(input("Enter tem in celsius:"))
print("Temparature in celsius is:",cels)
fahr=cels*9/5+32
print("temperature in fahrenheit is :",fahr)
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
z=int(input("Enter value of z:"))
print("I ndividually,A,B and C takes days respectively as:",x,y,z)
days=(x*y*z)/(x*y+y*z+x*z)
print("Together A,B and C takes days respectively as :",days)
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
print("Original numbers :",n1,n2)
n1,n2=n2,n1
print("After swapping :",n1,n2)
value='Anuy'
age=17
print(value,"you are", 17,"now but",end=' ')
print("you will be",age+1,"next year")
x,y=1,2
x,y,x,y=x+1,y+3,x+10,y+10
print(x,y)
miles=int(input("Enter miles :"))
km=miles/0.621371
print("miles :",miles)
print("kilometers :",km)
x=int(input("Enter value 1 :"))
y=int(input("Enter value 2 :"))
summ=x+y
diff=x-y
mult=x*y
div=x/y
mod=x%y
print("Numbers are :",x,y)
print("sum=",summ)
print("Difference=",diff)
print("Product=",mult)
print("Modules=",mod) 
z=(1+3.8j)+(-2-3.34j)
print(z.real)
print(z.imag)
a=34j
print(a)
p=36+0.j
print(p)
o=343+0j
print(o)
print(p.imag)
print(o.real)
print(o.imag)
string1=input("Enter a string :")
print("The",string1,"in reverse order is:")
length=len(string1)
for a in range(-1,(-length-1),-1) :
	print(string1[a])
string2=input("Enter a string :")
length=len(string2)
i=0
for a in range(-1,(-length-1),-1):
	print(string2[i],"\t",string2[a])
	i+=1
num=int(input("enter a number :"))
print("number entered",num)
onum=oct(num)
hnum=hex(num)
bnum=bin(num)
print("octal conversion", onum)
print("hexadecimal conversion", hnum)
print("binary conversion", bnum)

Weight=float(input("Enter your Weight in kg:"))
Height=float(input("Enter your Height in meters:"))
BMI=Weight/(Height*Height)
print(BMI,"this is your BMI")
if 24.9>=BMI>=18.5:
	print("Normal Weight")
if BMI<=18.5:
    print("Underweight")	
elif BMI>=24.9:
	print("Overweight")

z=0+4.5j
x=1.1+3.4j
print(z)
print(x)
a=(1+2.54j)+(-1-3.45j)
print(a)
print(z.real)
print(z.imag)
print(a.imag)
print(a.real)
a=[1,2,3,4,5,6,7,8,9]
a[0]=10
print(a)
p=(1,2,3,4,5,6,7,8,9)
myset={1,2,3,4,5,6,7,8,9}
vowels={'a':1,'e':2,'i':3,'o':4,'u':5}
print(vowels['a'])
p=5
q=p
r=5
print(id(5))
print(id(q))
p=10
r=7
q=r
print(id(r))
print(id(q))
name="superb"
for ch in name:
	print(ch,end='-')
type(x)
w="tea"+"pot"
print(w)

f=int(input("Enter the number:"))
a=10
b=23

c=43
d=45
e=90
num=int(input("Enter the number:"))
if num<=10:
	print(a)
	print(b)
	print(c)
	print(d)
	print(e)
Number=input("Enter a Number:")
DoubleTheNumber=Number*2
print(DoubleTheNumber)
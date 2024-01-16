def push(value):
	Stack.append(value)
def POP():
	Stack.POP()
def Peek():
	print(Stack[-1])
def Display():
	for i in range(len(Stack)-1,-1,-1):
		print(Stack[i],end=",")

Stack=[]
while True:
	Ch=int(input("Hey User Press\n"
		"1 for push\n"
		"2 for POP\n"
		"3 for Peek\n"
		"4 for Display"))
    
        if Ch==1:
            value=int(input("Enter value to push into Stack"))
            push(value)
        elif Ch==2:
            if len(Stack)==0:
                print("Underflow")
                break
            else:
    		pop()
        elif Ch==3:
            if len(Stack)==0:
                print("Stack is empty")
    		break
            else:
    		Peek()
        elif Ch==4:
            if len(Stack)==0:
    		print("Stack is empty")
    		break
            else:
    		Display()
        else:
            print("Exit")
            break


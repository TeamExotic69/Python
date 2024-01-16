
# Home Function
def Home():
	
	print("\t\t\t\t\t\t WELCOME TO HOTEL 009\n")
	print("\t\t\t 1 Booking\n")
	print("\t\t\t 2 Rooms Info\n")
	print("\t\t\t 3 Room Service(Menu Card)\n")
	print("\t\t\t 4 Payment\n")
	print("\t\t\t 5 Record\n")
	print("\t\t\t 0 Exit\n")

	ch=int(input("->"))
	
	if ch == 1:
		print(" ")
		Booking()
	
	elif ch == 2:
		print(" ")
		Rooms_Info()
	
	elif ch == 3:
		print(" ")
		restaurant()
	
	elif ch == 4:
		print(" ")
		Payment()
	
	elif ch == 5:
		print(" ")
		Record()
	
	

#Home()
h=0#int(input("enter number"))
while h==0:
    Home()




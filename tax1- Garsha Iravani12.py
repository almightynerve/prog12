print("welcome to the tax calculator" )
print("please put your items price number to proceed")
item1 = int(input("please enter your first item's value $"))
item2 = int(input("please enter your second item's value $"))
item3 = int(input(" please enter your next item's value $"))
totalcostaftertax = float(item1) + float(item2) + float(item3) + float(item1 * .12) + float(item2 * .12) + float(item3 * .12)
print("you need to pay $%.2f with Taxes included " % totalcostaftertax)

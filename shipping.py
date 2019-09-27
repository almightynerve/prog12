print("      << Shipping Charges Calculator >>    ")
item1 = int(input("Please enter the amount of your first items value $"))
item2 = int(input("please enter the amount of your second items value $"))
item3 = int(input("please enter the amount of your third items value $"))
totalpurchase = (float(item1 * .12) + float(item2 * .12) + float(item3 * .12))
if totalpurchase < 50.0 :
  print(" An additional fee of $10.0 will be charged for the shipping")
else:
  print("The shipping will be free")
if totalpurchase < 50.0 :
  print(" your total pay including shipping cost and tax is ${0: .2f}".format(totalpurchase+10))
if totalpurchase > 50.0 :
    print("Your total pay is ${0:.2f}".format(totalpurchase))
print("Thank You for Choosing us, See you Soon!")


print("-")
print(" -")
print("  -")
print("   -")
print("          << Welcome to the Calculator >>    ")
Total = float(input("please type your total purchase value: $"))
country= input("Do you live in Canada? ")
if country == "yes":
  province1= input("what province do you live in?:" )
else:
  print(" No tax will included")
  print("your total amount is: $")
  print(Total)
  print("Thank you for choosing us, See You Soon!")
if country== "yes":
  province1= "alberta"
  Total = float(Total * .05) + Total
  print(" your total pay including Tax will be:")
  print(Total)
if province1== "ontario" or province1== "new brunswick" or province1== "nova scotia":
  Total = float(Total * .13) + Total
  print("Your total pay including Tax will be:")
  print(Total)
if province1== "others":
  Total = float(Total * .11) + Total
  print( "Your total pay including tax will be:")
  print(Total)
print("Thank you for choosing us, See You Soon!")

price = int(input("enter your price: $"))
tip_percentage = int(input("enter you tip percentage: %"))

real_tip = tip_percentage / 100

realer_tip = price * real_tip
print("your tip is: ", realer_tip)

full_input = input("would you like to see the total price? ")

if full_input == "yes":
    print(realer_tip + price, "$")
elif full_input == "no":
    print("understood bigman")
else:
    print("an error occured")

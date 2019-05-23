print("Welcome to the commute cost calculator")
mileage = float(input("Please enter the vehicles mileage: "))
distance = float(input("Please enter the distance traveled in km: "))
gasPrice = float(input("Please enter the average gas price in dollars per litre: "))
numDays = int(input("Please enter the number of days you commuted: "))
numSplit = int(input("Please enter the number of ways you want the final cost split: "))

cost = (((distance * numDays) / (mileage*0.4251)) * gasPrice)/numSplit

if numSplit > 1:
	print("The cost of gas per person is ${}".format(round(cost,2)))
else:
	print("The cost of gas is ${}".format(round(cost,2)))
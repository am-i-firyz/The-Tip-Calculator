print("Welcome to the tip calculator.")

total = float(input("What was the total bill? "))
percentage = int(input("What percantage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

result = ((total * (percentage / 100 + 1.0)) / people)
real_result = "{:.2f}".format(result)

print (f"Each person should pay: {real_result}")

current = int(input("Enter your current money:"))
increasePercentage = int(input("Enter the percentage of increase:"))
year = int(input("Enter how many years current money will be increased:"))
increasedMoney = ((current / 100) * increasePercentage) * year + current
print("Your increased money is: {} ".format(increasedMoney))

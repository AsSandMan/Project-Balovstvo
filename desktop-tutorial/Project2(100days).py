# Приветствие
print("Welcome to the tip calculator.")
# Какая сумма
bill = float(input("What was the total bill? $"))
# сколько процентов хотите оставить чаевых
tip = int(input("What percentage tip would you like to give? 10,12 or 15?"))
tips_pers = tip / 100 * bill + bill
# Сколько человек
friend = int(input("How many people to split the bill?"))
result = round(tips_pers / friend, 2)


# Результат: сколько заплатит каждый

print("Each person should pay: " + f"${result}")
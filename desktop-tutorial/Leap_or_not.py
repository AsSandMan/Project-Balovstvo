year = int(input("Какой сейчас год? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} - Это высокосный год!")
        else:
            print(f"{year} - Это невысокосный год!")
    else:
        print(f"{year} - Это высокосный год!")
else:
    print(f"{year} - Это невысокосный год!")
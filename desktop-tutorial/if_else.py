print("Welcome to the rollercoaster!")
height = int(input("What os your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:

        print(f"Child tickets are ${bill}.")
    elif age <= 18:
        bill += 7
        print(f"Youth tickets are ${bill}.")
    else:
        bill += 12
        print(f"Adult tickets are ${bill}.")

    photo = input("Do you want a photo taken? Y or N.")
    if photo == "Y":
        #Add $3 to their bill
        bill += 3
        print(f"Please pay ${bill}.")
    else:
        print(f"Please pay ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
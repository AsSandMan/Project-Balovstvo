import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissor]
user_choice = int(input("Выбери 0. Камень, 1. Ножницы или 2. Бумага. \n"))
if user_choice >= 3 or user_choice < 0:
    print("Ты что, жульничаешь? ТЫ ПРОИГРАЛ!")

else:
    print(game_images[user_choice])

    computer_choice = random.randint (0, 2)
    print("Kомпьютер выбрал:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("Ты выйграл!")
    elif computer_choice > user_choice:
        print("Ты проиграл")
    elif computer_choice == 0 and user_choice == 2:
        print("Ты проиграл")
    elif computer_choice == user_choice:
        print("Ничья")
    elif user_choice > computer_choice:
        print("Ты выйграл!")



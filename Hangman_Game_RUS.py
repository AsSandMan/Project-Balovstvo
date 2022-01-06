#HangMan_The_Game
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
          '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
          '''
  +---+
  |   |
      |
      |
      |
      |
=========

''']

lives = 7
end_of_game = False
word_list = ["толерантность", "эксгумация", "либерализм", "экспонат", "пышность",
             "скабрёзность", "шаловливость", "экспозиция", "индульгенция",
             "контрацептив", "шкворень", "эпиграф", "эпитафия", "барбекю",
             "жульен", "энцефалопатия", "парашютист", "импозантность",
             "индифферент", "демультипликатор", "педикулёз", "выхухоль",
             "россомаха", "сущность", "поэтапность", "напыщенность",
             "возвышенность"]

#TODO-1 - Randomly chose a word from the word_list and assingn it to a variable called chosen_word
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


chosen_word = random.choice(word_list)




#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)



while not end_of_game:
    user_guess = input("Угадай букву: ").lower()


#TODO-3 - Check if the letter the user guessed (guess) is one of the leters in the chosen_word.
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter


    if user_guess not in chosen_word:
        print(stages[lives - 1])
        lives -= 1
        if lives < 1:
            end_of_game = True
            print("Game Over")
            print(chosen_word)


#TODO-01 - СДЕЛАЙ НОРМАЛЬНО!


    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

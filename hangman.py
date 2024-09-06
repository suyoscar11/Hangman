

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
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["antelope", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6





display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
        


    if guess not in chosen_word:
        lives= lives-1
        print(stages[lives])
        if lives==0:
            print("Game Over")
            end_of_game= True
        if "_" not in display:
            print("You Win")
            end_of_game= True
            
        
    print(f"{' '.join(display)}")

  

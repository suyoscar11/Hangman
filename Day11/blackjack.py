import random

play= input("Do you want to play? 'y' or 'n': ")


card1= random.randint(1,13)
card2= random.randint(1,13)

def random_card():
 x=random.randint(1,13)
 return x
your_cards= []
comp_cards = []

your_cards.append(card1)
your_cards.append(card2)
comp_cards.append(random_card())
print(f"Your cards: {your_cards}")

print(f"Computer's first card: {random_card()}")

new_card=input("Type 'y' to get another card, type 'n' to pass: ")

your_sum = card1 + card2

if new_card == 'y':
    third= random_card()
    your_cards.append(third)
    print(f"Your cards: {your_cards}")

if new_card=='n':
   fourth= random_card()
   comp_cards.append(fourth)
   print(f"Your Final Hand: {your_cards}")
   print(f"Computer's Final Hand: {comp_cards}")
sum = 0
for element in your_cards:
   sum = sum+ element 
print(sum)
som = 0
for elemnt in comp_cards:
   som =+ elemnt
print(som)

if sum>som:
   print("You Win")
elif sum== som:
   print("Draw")
else:
   print("You lose")




#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     x = random.choice(cards)
#     return x



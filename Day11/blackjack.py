import random

play= input("Do you want to play? 'y' or 'n': ")


card1= random.randint(1,13)
card2= random.randint(1,13)

def random_card():
 random.randint(1,13)

your_cards= []
comp_cards = []

your_cards.append(card1)
your_cards.append(card2)
comp_cards.append(random_card())
print(f"Your cards: {your_cards}")

print(f"Computer's first card: {random_card()}")

new_card=input("Type 'y' to get another card, type 'n' to pass: ")

your_sum = card1 + card2

while new_card == 'y':
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
   som += elemnt
print(som)

if sum>som:
   print("You Win")
elif sum== som:
   print("Draw")
else:
   print("You lose")


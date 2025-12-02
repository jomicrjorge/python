import random
import time # time module to use sleep in the program
""" This program is the 2 face of the blackjack game. In here we have our first program of a card game. 

The objective of the game:
- Whoever has the highest card wins.

What will be done in this program:
- We will create a deck of 52 cards
- Each player will be given a card"""


#Create the deck

figures= [2,3,4,5,6,7,8,9,10,"Ace","Queen","King","Jack"]
naipes = ["clubs","diamonds", "hearts" ,"spades"]
card_dictionary= {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Ace":14,"Queen":12,"King":13,"Jack":11}
deck = [ f"{fig}"for naipe in naipes for fig in figures ]# Create a list of 52 card ranks as strings (we ignore suits in this game)


player1=random.choice(deck)
deck.remove(player1) # Remove the card so it cannot be drawn again
player2=random.choice(deck)
deck.remove(player2) # Same for Player 2



def shuffling():
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("...")
  time.sleep(1)
  print("...")

def give_cards():
 print("Giving card to Player1...")
 shuffling()
 print("Giving card to Player2...")
 shuffling()

class figures_value:
  def __init__(self, deck):
   self.rank = deck
   self.value = card_dictionary[deck]

# See if user wants to play the game or not

play_game=input("Do you want to play the game?[yes or no]: ")
while play_game == "yes":
 print("Shuffling the cards...")
 shuffling()
 give_cards()
 
 player1_value = figures_value(player1)
 player2_value =  figures_value(player2)
 
 def show_cards():
  print(f"Player1 cards : {player1}") 
  shuffling()
  print(f"Player2 cards : {player2}")#Para print em 2 linhas ter cuidado como \

 if player1_value.value > player2_value.value :
  time.sleep(1)
  show_cards()
  time.sleep(1)
  print("Player1 Wins !")
 elif player1_value.value < player2_value.value:
  time.sleep(1)
  show_cards()
  time.sleep(1)
  print("\nPlayer2 Wins!")
 else:
  while player1_value.value == player2_value.value :
   time.sleep(1)
   show_cards()
   print(f"\n{player1} = {player2}, it is a Draw!" )
   time.sleep(1)
   print("I will give you another card to see who wins!")
   player1=random.choice(deck)
   deck.remove(player1)
   player2=random.choice(deck)
   deck.remove(player2)
   player1_value = figures_value(player1)
   player2_value =  figures_value(player2)
   time.sleep(1)
   give_cards()
   show_cards()
 play_game=input("Do you want to play the game again ?[yes or no]: ")


  




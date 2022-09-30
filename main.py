import random
from art import *
print(logo)
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=random.sample(cards,2)
dealer_cards=random.sample(cards,2)
print(f"Your cards\n{user_cards}")
print(f"value chosen by dealer\n{dealer_cards[0]}")
user_sum=sum(user_cards)
dealer_sum=sum(dealer_cards)
flag=True
while flag:
  k=random.choice(cards)
  if dealer_sum<17:
    dealer_cards.append(k)
    dealer_sum=sum(dealer_cards)
    #print(dealer_cards)
  elif(dealer_sum+k<=21):
    dealer_cards.append(k)
    dealer_sum=sum(dealer_cards)
    #print(dealer_cards)
    if dealer_sum+k>21:
      deal=k
  else:
    if dealer_sum>21:
      if 11 in dealer_cards:
        dealer_cards.remove(11)
        dealer_cards.append(1)
      else:
        flag=False
        #print(dealer_cards)
    else:
      flag=False
def decide(user_cards,dealer_sum,contin,choice):
  user_sum=sum(user_cards)
  ##print("It's a draw.")
  if user_sum>21:
    if 11 in user_cards:
      user_cards.remove(11)
      user_cards.append(1)
      user_sum=sum(user_cards)
      contin=True
      blackjack(user_cards,user_sum,dealer_cards,dealer_sum,contin)

    else:
      print(f"dealer cards:{dealer_cards}")
      print("you lose.")
  #elif user_sum==21 or dealer_sum>21:
   # print("you won.")
  
  else:
    if choice=="n":
      if dealer_sum>21:
        print(f"dealer cards:{dealer_cards}")
        print("you win.")
      else:
        if user_sum==dealer_sum:
          print(f"dealer cards:{dealer_cards}")
          print("it's a draw.")
        elif user_sum>dealer_sum:
          dealer_cards.append(k)
          print(f"dealer cards:{dealer_cards}")
          print("you won.")
        else:
          print(f"dealer cards:{dealer_cards}")
          print("you lose")
    else:
      contin=True
      blackjack(user_cards,user_sum,dealer_cards,dealer_sum,contin)
     
contin=True

def blackjack(user_cards,user_sum,dealer_cards,dealer_sum,contin):
  while  contin:
    contin=False
    choice = input("you wanna choose a card ,type 'y' if yes or else type 'n'")
    if choice=='n':
      decide(user_cards,dealer_sum,contin,choice)
    else:
      contin=True
      user_cards.append(random.choice(cards))
      print(user_cards)
      user_sum=sum(user_cards)
      decide(user_cards,dealer_sum,contin,choice)
      contin=False
if user_sum==21:
    print("you won.")
else:
  blackjack(user_cards,user_sum,dealer_cards,dealer_sum,contin)     

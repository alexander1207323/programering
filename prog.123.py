
import random


deck = [
    "2 av Hjärter", "3 av hjärter", "4 av hjärter", "5 av hjärter", "6 av hjärter", "7 av hjärter", "8 av hjärter",
    "9 av hjärter", "10 av hjärter", "knekt av hjärter", "drotning av hjärter", "kung av hjärter", "Ace av hjärter",
    "2 av ruter", "3 av ruter", "4 av ruter", "5 av ruter", "6 av ruter", "7 av ruter", "8 av rutter",
    "9 av ruter", "10 av ruter", "knekt av ruter", "drotning av ruter", "Kung av ruter", "Ace av ruter",
    "2 av klöver", "3 av klöver", "4 av klöver", "5 av klöver", "6 av klöver", "7 av klöver", "8 av klöver",
    "9 av klöver", "10 av klöver", "knekt av klöver", "drotning av klöver", "kung av klöver", "Ace av klöver",
    "2 av spader", "3 av spader", "4 av spader", "5 av spader", "6 av spader", "7 av spader", "8 av spader",
    "9 av spader", "10 av spader", "knekt av spader", "drotning av spader", "kung av spader", "Ace av spader"
]


def play_round():
   
    random.shuffle(deck)
    
   
    player_card = deck.pop()
    computer_card = deck.pop()
    
    
    print("ditt kort är:", player_card)
    print("datorn kort är:", computer_card)
    
   
    player_value = get_card_value(player_card)
    computer_value = get_card_value(computer_card)
    
    if player_value > computer_value:
        print("du van spelaet!")
    elif player_value < computer_value:
        print("datorn van!")
    else:
        print("det blev lika!")
        

def get_card_value(card):
    value = card.split()[0]
    
    if value == "Ace":
        return 14
    elif value == "kung":
        return 13
    elif value == "drotning":
        return 12
    elif value == "knekt":
        return 11
    else:
        return int(value)


while True:
    play_round()
    choice = input("vill du spela igen? ")
    if choice.lower() != "ja":
        break

print("tack för att du spela!")



import random

# Definiera kortlek
cards = [
    "Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"
]

# Skapa funktion för att dra kort
def draw_card():
    card = random.choice(cards)
    return card

# Skapa funktion för att räkna poäng
def count_points(hand):
    points = 0
    ace_count = 0
    
    for card in hand:
        if card == "Ace":
            ace_count += 1
            points += 11
        elif card in ["King", "Queen", "Jack", "10"]:
            points += 10
        else:
            points += int(card)
    
    while ace_count > 0 and points > 21:
        points -= 10
        ace_count -= 1
    
    return points

# Skapa funktion för att spela en omgång
def play_round():
    # Skapa kortlekar för spelaren och dealern
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]
    
    # Spela spelarens drag
    while True:
        print("Your hand:", player_hand)
        print("Your points:", count_points(player_hand))
        
        if count_points(player_hand) > 21:
            print("Bust! You lose.")
            return
        
        choice = input("Do you want to hit or stand? ")
        if choice.lower() == "hit":
            player_hand.append(draw_card())
        elif choice.lower() == "stand":
            break
    
    # Spela dealerns drag
    while count_points(dealer_hand) < 17:
        dealer_hand.append(draw_card())
    
    # Räkna poäng och avgör vinnare
    player_points = count_points(player_hand)
    dealer_points = count_points(dealer_hand)
    
    print("Your hand:", player_hand)
    print("Your points:", player_points)
    print("Dealer's hand:", dealer_hand)
    print("Dealer's points:", dealer_points)
    
    if dealer_points > 21:
        print("Dealer busts! You win.")
    elif player_points > dealer_points:
        print("You win!")
    elif dealer_points > player_points:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Spela spelet
while True:
    play_round()
    choice = input("Do you want to play again? ")
    if choice.lower() != "yes":
        break

print("Thanks for playing!")



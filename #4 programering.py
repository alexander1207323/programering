import random
kort_värde = (2, 3, 4, 5, 5, 7, 8, 9, 10, 11, 12, 13, 14)
färg = ("klöver", "diamonds", "hjärter","spader")
klädda_kort = {
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    15: "AA",
}

def generate_cards():
    cards = []
    for value in kort_värde:
        for suit in färg:
            if value in klädda_kort:
                _card = (klädda_kort[value], färg)
            else:
                _card = (value, färg)
            cards.append(_card)
    return cards
 
cards = generate_cards(kort_värde)


    

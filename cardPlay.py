# Loose load function implementation
import csv

class Card :

    name   = ""
    type   = ""
    color  = ""
    rarity = ""
    
    cost  = 0

    def __init__ (self, name, type, color, rarity, cost):
        self.name   = name
        self.type   = type
        self.color  = color
        self.rarity = rarity
        self.cost   = cost

if __name__ == '__main__':

    file = "C:\\Users\\mount\\Downloads\\AllPrintingsCSVFiles\\cards.csv" # This would be the userFileInput

    masterDeck = []

    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        try:
            for row in reader:

                # Pass relevant card parameters to Card constructor and add to list
                newcard = Card(row["name"], row["type"], row["colorIdentity"], row["rarity"], row["manaValue"])

                masterDeck.append(newcard)

        except:
            pass
    
    for card in masterDeck:
        print(f'\nMaster Card Deck Name: {card.name} | Type: {card.type}')
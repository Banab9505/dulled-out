import random

class Stats():

    """ docstring for Stats"""

    def __init__(self, name, attack, defense, health, range, cycle, utility, elixir, rating: float):
        self.name=name
        self.attack=attack
        self.defense=defense
        self.health=health
        self.range=range
        self.cycle=cycle
        self.utility=utility
        self.elixir=elixir
        self.rating = round(((self.attack + self.defense + self.health)/3) * (self.utility/self.elixir))

    def get_stats(x):
        print("Overal rating is: " , x.rating)

    #def cycle_eligible(self):
    #    if self.cycle is False:
    #    else:
    #        return("Can be cycled.")

    #def cycle_type(self):
    #    if self.cycle is True and cycle_deck == 'yes':
    #        return deck.append(random.choice(troops))

    def __str__(self):
        return(self.name)

    def elixir_cost(self):
        print(Stats(self.elixir, self.attack, self.defense, self.health, self.range, self.cycle, self.utility, self.rating, None))

    def cycle_status(self):
        return Stats(self.cycle, self.attack, self.defense, self.health, self.range, self.elixir, self.utility, self.rating, None)

    def __repr__(self):
        return self.name



#Cards: Name, Attack, defense, health, range, cycle, utility, elixir, rating (ignore None value)

#Common Cards
knight = Stats("Knight", 3, 6, 8, 1, True, 7, 3, None)
goblins = Stats("Goblins", 2, 7, 2, 1, True, 7, 2, None)
spear_goblins = Stats("Spear Goblins", 3, 7, 1, 5, True, 9, 2, None)
skeletons = Stats("Skeletons", 1, 5, 1, 1, True, 10, 1, None)
ice_spirit = Stats("Ice Spirit", 2, 4, 2, 3, True, 9, 1, None)
minions = Stats("Minions", 5, 9, 4, 4, False, 8, 3, None)
fire_spirit = Stats("Fire Spirit", 5, 5, 2, 3, True, 8, 1, None)
minion_horde = Stats("Minion Horde", 4, 8, 1, 4, False, 5, 5, None)
fire_cracker = Stats("Fire Cracker", 8, 8, 3, 6, True, 9, 3, None)

#Rare Cards
hog_rider = Stats("Hog Rider", 10, 0, 7, 1, True, 8, 4, None)

def ask_user():
    troops = [
        knight,
        goblins,
        spear_goblins,
        skeletons,
        ice_spirit,
        minions,
        fire_spirit,
        minion_horde,
        fire_cracker,
        hog_rider
        ]
    deck = []

    for i in troops:
        i.get_stats()

    ask_for_list = input("If you would like a list of cards, type in: 'list'. ")
    if ask_for_list == "list":
        print(knight, goblins, spear_goblins, skeletons, ice_spirit, minions, fire_spirit, minion_horde, fire_cracker, hog_rider) #Problem with __main__ object at xxxxxxxxxxxxxxxxxxxx

    Rating = input("Do you want the overall rating for any given card? If so, type in the card that you want the rating for. If you want to continue, type in 'continue'. ")
    while Rating != 'continue':
        return
    if Rating == "continue":
        cycle_deck = input("Do you want a cycle deck? ") #Problem with input being a string and not an argument
        if cycle_deck == 'yes':
            troops.remove(minions)
            troops.remove(minion_horde)
            k = 8
            deck.append(random.sample(troops, k))
            if hog_rider in deck:
                deck.remove(hog_rider)
            else:
                print(repr(deck))
    else:
        return

ask_user()



#print(Stats(fire_spirit.elixir, fire_spirit.attack, fire_spirit.defense, fire_spirit.health, fire_spirit.range, fire_spirit.cycle, fire_spirit.utility, fire_spirit.rating, None))

#print("Overall rating:", (knight.get_rating()))
#print("%s" % (knight.cycle_eligible()))

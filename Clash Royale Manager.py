import random

class stats_troops():

    """ docstring for stats_troops"""

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

    def get_stats_troops(x):
        print("Overal rating is: " , x.rating)

    #def cycle_eligible(self):
    #    if self.cycle is False:
    #    else:
    #        return("Can be cycled.")

    #def cycle_type(self):
    #    if self.cycle is True and cycle_deck == 'yes':
    #        return deck.append(random.choice(troops))

    def __str__(self):
        return "%s, " % (self.name)

    def elixir_cost(self):
        return stats_troops(self.elixir, self.attack, self.defense, self.health, self.range, self.cycle, self.utility, self.rating, None)/8

    def cycle_status(self):
        return stats_troops(self.cycle, self.attack, self.defense, self.health, self.range, self.elixir, self.utility, self.rating, None)

    def __repr__(self):
        return("%s" % (self.name))


class stats_spells(object):
    """docstring for stats_spells."""

    def __init__(self, name, attack, defense, cycle, utility, elixir, rating):
        self.name=name
        self.attack=attack
        self.defense=defense
        self.cycle=cycle
        self.utility=utility
        self.elixir=elixir

    def __str__(self):
        return "%s, " % (self.name)


#Cards: Name, Attack, defense, health, range, cycle, utility, elixir, rating (ignore None value)
# Spells: Name, Attack, Defense, Utility, Cycle, Elixir, rating (ignore None value)
#Common Cards
knight = stats_troops("Knight", 3, 6, 8, 1, True, 7, 3, None)
goblins = stats_troops("Goblins", 2, 7, 2, 1, True, 7, 2, None)
spear_goblins = stats_troops("Spear Goblins", 3, 7, 1, 5, True, 9, 2, None)
skeletons = stats_troops("Skeletons", 1, 5, 1, 1, True, 10, 1, None)
ice_spirit = stats_troops("Ice Spirit", 2, 4, 2, 3, True, 9, 1, None)
minions = stats_troops("Minions", 5, 9, 4, 4, False, 8, 3, None)
fire_spirit = stats_troops("Fire Spirit", 5, 5, 2, 3, True, 8, 1, None)
minion_horde = stats_troops("Minion Horde", 4, 8, 1, 4, False, 5, 5, None)
fire_cracker = stats_troops("Fire Cracker", 8, 8, 3, 6, True, 9, 3, None)
giant_snowball = stats_spells("Giant Snowball", 2, 9, 10, True, 2, None)

#Rare Cards
hog_rider = stats_troops("Hog Rider", 10, 0, 7, 1, True, 8, 4, None)

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

    ask_for_list = input("If you would like a list of cards, type in: 'list'. ")
    if ask_for_list == "list":
        print(knight, goblins, spear_goblins, skeletons, ice_spirit, minions, fire_spirit, minion_horde, fire_cracker, hog_rider) #Problem with __main__ object at xxxxxxxxxxxxxxxxxxxx

    Rating = input("Do you want the overall rating for any given card? If so, type in the card that you want the rating for. If you want to continue, type in 'continue'. ")
    while Rating != 'continue':
        return
    if Rating == "continue":
        cycle_deck = input("Do you want a cycle deck? ")
        if cycle_deck == 'yes':
            troops.remove(minions)
            troops.remove(minion_horde)
            k = 8
            deck.append(random.sample(troops, k))
            if hog_rider in deck:
                deck.remove(hog_rider)
            else:
                if deck.elixir_cost() <= 3:
                    print("Here's your deck.")
                    print(repr(deck))
    else:
        print("Sorry, check your spelling.")

ask_user()

knight.get_rating()

#print(stats_troops(fire_spirit.elixir, fire_spirit.attack, fire_spirit.defense, fire_spirit.health, fire_spirit.range, fire_spirit.cycle, fire_spirit.utility, fire_spirit.rating, None))

#print("Overall rating:", (knight.get_rating()))
#print("%s" % (knight.cycle_eligible()))

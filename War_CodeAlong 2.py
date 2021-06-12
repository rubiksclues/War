import random
# card suits and ranks
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# dictionary of values for cards
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


"""
CARD CLASS:
SUIT, RANK, VALUE
"""
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
    
two_of_hearts = Card("Hearts","Two")
# print(values[two_of_hearts.rank])
three_of_clubs = Card("Clubs","Three")

class Deck:
    def __init__(self):
        
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # create the card objects
                created_card = Card(suit, rank)

                # adds all 52 cards to the list all_cards
                self.all_cards.append(created_card)
    # shuffle function for the deck
    def shuffle(self):
        # will shuffle the deck in place, does not store the result and does not need to
        random.shuffle(self.all_cards)

    # deals out one card from the deck, uses pop method to pop one card off the end of the list of cards in the deck then returns it
    def deal_one(self):
        return self.all_cards.pop()

'''
# creates a deck, then prints the display are cards stored within the function to check if this works
# new_deck = Deck()
# print(new_deck.all_cards)


CHECKING TO SEE IF CODE WORKS
# grabs the first card from the deck, then prints the FIRST card and then the LAST card in the function to check if this works
top_card = new_deck.all_cards[0]
bot_card = new_deck.all_cards[-1]
# print(top_card)
# print(bot_card)
# prints all the cards in the deck
for card_object in new_deck.all_cards:
    print(card_object)


# shuffles new_deck
new_deck.shuffle()


#uses the deal_one function to deal out a card
my_card = new_deck.deal_one()
# print(my_card)
'''
# creates player class
class Player:
    
    def __init__(self, name):
        # attribute for players name
        self.name = name
        # creates the players current hand
        self.all_cards = []

    # removes one card when player plays from their hand, NEEDS the 0 in the pop method to make sure the card is taken from the TOP of the deck
    def remove_one(self):
        return self.all_cards.pop(0)
    # adds one card
    def add_cards(self, new_cards):
        # if the cards added are a list, this means we are adding multiple cards
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # otherwise, you are adding a single card
        else:
            self.all_cards.append(new_cards)

    # prints out a player cards
    def __str__(self):
            return f'Player {self.name} has {len(self.all_cards)} cards'

'''
# creates a new player
new_player = Player("One")
print(new_player)
#adds card from my_card function above to player one's hand to check if adding card function is working
new_player.add_cards(my_card)
print(new_player)
print(new_player.all_cards[0])
'''

# GAME SETUP

# creates player one and player 2
player_one = Player("One")
player_two = Player('Two')

# creates a new deck, then shuffles
new_deck = Deck()
new_deck.shuffle()

# divides deck between two player
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

# boolean to run game loop
game_on = True
# game round counter
match_round = 0
while game_on:
    match_round += 1
    print(f'Current Round: {match_round}')

    # condition check to see if a player is out of cards and has effectively lost, ending the game and then breaking out of the loop entirely
    if len(player_one.all_cards) == 0:
        print('Player One has run out of cards! Player Two wins !')
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print('Player Two has run out of cards! Player One wins !')
        game_on = False
        break
    # starts a new round
    #variable for current cards in play, takes a card out of a players hand and adds it to their cards in play variable
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True
    '''
    at war is run at true to account for other wars happening in the matchup. 
    the loop starts by checking if player ones card is bigger or if player twos card is bigger,
    if either is the case it will break out of the loop, if not it will continue the war
    '''
    while at_war:
        # -1 is specified as to ensure you are picking the last new card drawn that is being appended to the cards in play hand each player has
        # gives winning player all cards in play
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
            break
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
            break
        else:
            print("W A R ! ! !")

            # check for if you have enough cards to play the war
            if len(player_one.all_cards) < 4:
                print("Player One doesn't have enough cards to declare war, Player Two wins !")
                game_on = False
                break
            if len(player_two.all_cards) < 4:
                print("Player Two doesn't have enough cards to declare war, Player One wins !")
                game_on = False
                break
            else:
                for num in range(4):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

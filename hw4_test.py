#########################################
##### Name: Weifeng Xu              #####
##### Uniqname: samtsui             #####
#########################################

import unittest
import hw4_cards as cards

# SI 507 Winter 2020
# Homework 4 - Code

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    # this is a "test"
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        card = cards.Card(rank=12)
        self.assertEqual(card.rank_name, "Queen")

    def test_2_clubs(self):
        card = cards.Card(suit=1)
        self.assertEqual(card.suit_name, "Clubs")

    def test_3_KoS(self):
        card = cards.Card(suit=3, rank=13)
        s = card.__str__()
        self.assertEqual(s, "King of Spades")

    def test_4_52(self):
        deck = cards.Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_5_deal(self):
        deck = cards.Deck()
        c = deck.deal_card()
        self.assertIsInstance(c, cards.Card)

    def test_6_fewer(self):
        deck = cards.Deck()
        d1 = len(deck.cards) # number of cards before dealing
        deck.deal_card()
        d2 = len(deck.cards) # number of cards after dealing
        self.assertEqual(d1, d2+1)

    def test_7_more(self):
        deck = cards.Deck()  # original deck
        d1 = len(deck.cards)
        c = deck.deal_card() # remove a card
        d2 = len(deck.cards)
        deck.replace_card(c) # replace a card
        d3 = len(deck.cards)
        self.assertEqual(d3, d2+1)

    def test_8_size(self):
        deck = cards.Deck()   # original deck
        c1 = deck.deal_card() # deal the first card
        c2 = deck.deal_card() # deal the second card (just want to deal one more card)
        deck.replace_card(c1) # replace the first card
        d1 = len(deck.cards)
        deck.replace_card(c1) # try to replace the first card again
        d2 = len(deck.cards)
        self.assertEqual(d1, d2)
        
        



############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()

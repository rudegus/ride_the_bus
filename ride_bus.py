import random

class Card:
  def __init__(self, suit, val):
    self.suit = suit
    self.value = val

  def black(self):
    if self.suit == "Spades" or self.suit == "Clubs":
      return('black')

  def red(self):
    if self.suit == "Hearts" or self.suit == "Diamonds":
      return('red')

  def num(self):
    num = self.value
    return(num)

  def suitz(self):
    sui = self.suit
    return(sui.lower())

  def show(self):
    print("{} of {}".format(self.value, self.suit))


class Deck:
  def __init__(self):
    self.cards = []
    self.build()

  def build(self):
    for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
      for v in range(1,14):
        self.cards.append(Card(s, v))

  def show(self):
    for c in self.cards:
      c.show()

  def shuffle(self):
    for i in range(len(self.cards) - 1, 0, -1):
      r = random.randint(0, i)
      self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

  def drawCard(self):
    return self.cards.pop()

class Player:
  def __init__(self):
    pass


#   deck = Deck()
#   deck.shuffle()
#   my_card = deck.drawCard()
#   red_black = input("Red or Black?: ")
#   my_card.show()
#   if red_black == 'spade'

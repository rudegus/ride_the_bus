from ride_bus import *

deck = Deck()
counter = 0

while counter <= 51:

# Red or Black?
  g1 = input("red or black?\n")
  deck.shuffle()
  my_card = deck.drawCard()
  my_card.show()
  if g1 == my_card.black() or g1 == my_card.red():
    print("\tCorrect!\n")
    counter += 1
    if counter == 51:
        break
  else:
    print("\tTry again!\n")
    counter += 1
    if counter == 51:
        break
    continue

# High or Low?
  second_card = deck.drawCard()
  high_low = input("high or low?\n")
  n = range(1, 14)

  if second_card.num() > my_card.num():
    answer = 'high'
  else:
    answer = 'low'
  if answer == high_low:
    second_card.show()
    print("\tCorrect!\n")
    counter += 1
    if counter == 51:
        break
  else:
    second_card.show()
    print("\tTry again!\n")
    counter += 1
    if counter == 51:
        break
    continue

# Outside or Inside?
  third_card = deck.drawCard()
  out_in = input("outside or inside\n")

  if my_card.num() > third_card.num() and third_card.num() > second_card.num():
    ans = 'inside'
  elif my_card.num() < third_card.num() and third_card.num() < second_card.num():
    ans = 'inside'
  elif third_card.num() > my_card.num() and third_card.num() > second_card.num():
    ans = 'outside'
  else:
    ans = 'outside'
  if ans == out_in:
    third_card.show()
    print("\tCorrect!\n")
    counter += 1
    if counter == 51:
        break
  else:
    third_card.show()
    print("\tTry again!\n")
    counter += 1
    if counter == 51:
        break
    continue

# Suit?
  fourth_card = deck.drawCard()
  zuit = input("What suit? (spades,diamonds, etc.)\n")
  if zuit == fourth_card.suitz():
    fourth_card.show()
    print("\tCorrect! You may exit the bus.")
    break
  else:
    fourth_card.show()
    print("\tGet back on the bus!\n")
    counter += 1
    if counter == 51:
        break
    continue
if counter == 51:
    print("\nYou ran out of cards!")
    print("\nGame over!\n")
else:
    print("\nYou may exit the bus!\n")
    print("turns: " + str(counter + 1))

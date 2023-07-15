#Stores choices from user input, for fstring and path selection.
choices = []

def big_choice():
  """
  First set of choices, currently in 'A'.
  Possible choices are 'B', 'C' and ending '1'.
  """
  while True:
    print("\n----------------------------------------------------------------------")
    print("\n You wake up and put on some clothes, grab a can of caffinated energy drink")
    print("and sit infront of your computer screen, ready for another day of coding.")
    print("I mean, that's what you should be doing... Is is what you're going to do?")
    print("\nIt's probably time to start 'work', the hardest part is starting!")
    print("Just one quick 'game'? I mean, you have got ALL day to study...")
    print("Feet up, music on and finish your 'drink'. You need that caffeine.")
    player_choice = input("Urgh... Mornings are the worst. What are you going to do?\n")
    player_choice = player_choice.lower()
    if player_choice == "work":
      choices.append("work")
      break
    elif player_choice == "game":
      choices.append("game")
      break
    elif player.choice == "quit":
      print("Game terminated. Thank you for playing.")
    elif player_choice == "drink":
      print("You open up 'Lo-Fi chill hop beats to study slash relax to' and click play")
      print("Turn up the volume, put your feet up on the desk and close your eyes.")
      print("Bliss! Well, until you reach for for your trusty energy drink...")
      print("Which is lying on it's side, it's contents emptied all over your keyboard.")
      print("Wow... The day is over before it began. Back to bed?")
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )


def good_choice_one():
  """
  Good path, first choice. Currently in 'C'.
  Possible choices are 'E' and 'G'.
  """
  while True:
    print("\n----------------------------------------------------------------------")
    print("\n You're up and running! You load up for favorite IDE, find the bookmark")
    print("for your latest online lesson and hit play. You take a sip of caffeine++ and")
    print("try to zone in on what's going on. Superclasses? Mixins!? Inheritance. What?")
    print("\n It's ok, you've got this. Check through 'slack' and see if there's any tips.")
    print("Or open 'youtube' and come back to it in a little bit, it's too early for this.")
    player_choice = input("It feels like all hope is gone and your mind is blank, what to do?\n")
    player_choice = player_choice.lower()
    if player_choice == "slack":
      choices.append("slack")
      break
    elif player_choice == "youtube":
      choices.append("youtube")
      break
    elif player.choice == "quit":
      print("Game terminated. Thank you for playing.")
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )

def main_game():
  """
  Main game functions, will run in order as the game progresses.
  """
  big_choice()
  if "work" in choices: 
    good_choice_one()
  elif "game" in choices:
    bad_choice_one()
  else:
    print("ERROR MESSAGE. CHOICES NOT FOUND")

#ASCII Art landing page, while loop which requires 'ready' to escape.
print("""
                      ____|====|____
     _______________/                \_______________ 
   _|________________________________________________|_
  |____________________________________________________|
     
  ,----------------------------------------------------,
  | [][][][][]  [][][][][]  [][][][]  [][__]  [][][][] |
  |                                                    |
  |  [][][][][][][][][][][][][][_]    [][][]  [][][][] |
  |  [_][][][][][][][][][][][][][ |   [][][]  [][][][] |
  | [][_][][][][][][][][][][][][]||     []    [][][][] |
  | [__][][][][][][][][][][][][__]    [][][]  [][][]|| |
  |   [__][________________][__]              [__][]|| |
  `----------------------------------------------------'
""")
print("Welcome to 'A day in the life', A text based adventure through")
print("the life of a student. All you need to do is type out the")
print("'keyword' highlighted in quotes to progress through the day.")
print("You can also type 'quit' at any time to leave the game.")
while True:
  game_start = input("\nAre you 'ready' to wake up in the life of a coding student?\n")
  game_start = game_start.lower()
  if game_start == "ready":
    break
  elif game_start =="quit":
    print("Not now... You didn't even start playing! Do you think that's funny?")
  else:
    print("That's ok, we can wait until you're 'ready'...\n")
    
main_game()
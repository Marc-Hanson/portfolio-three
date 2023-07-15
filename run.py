# Stores choices from user input, for fstring and path selection.
choices = []

# Map of the project is included as an image in inside the Readme.
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


def good_choice_two():
  """
  Good path, second choice. Currently in 'G'.
  Possible choices are 'I' and 'J'.
  """
  while True:
    print("\n----------------------------------------------------------------------")
    print("\n It a lot of work! But you're sticking with it. It doesn't make complete sense")
    print("but that's ok. You're starting to understand what Python can do even if you can't")
    print("write it alone or even recite what was on the previous page. For now, it's enough.")
    print("\n Maybe if you just grabbed a snack, some 'chocolate' maybe. It would all make sense.")
    print("Take another sip of your drink and play with the 'code' to figure out how it works.")
    player_choice = input("It feels like all hope is gone and your mind is blank, what to do?\n")
    player_choice = player_choice.lower()
    if player_choice == "chocolate":
      choices.append("chocolate")
      break
    elif player_choice == "code":
      choices.append("code")
      break
    elif player.choice == "quit":
      print("Game terminated. Thank you for playing.")
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )


def good_choice_three():
  """
  Good path, third choice. Currently in 'I'.
  Possible choices are 'L' - The secret ending.
  """
  while True:
    print("\n----------------------------------------------------------------------")
    print("\n You've done it! You've worked hard and pushed through to get another day done.")
    print("Now the day is yours to enjoy, deep breath and relax those shoulders!")
    print("\n You've commited and pushed your code for the day and you're ahead of schedule!")
    print("You can close your terminal by typing 'quit' or guess the secret 'password'.")
    player_choice = input("It feels like all hope is gone and your mind is blank, what to do?\n")
    player_choice = player_choice.lower()
    if player_choice == "password":
      choices.append("password")
      break
    elif player.choice == "quit":
      print("Game terminated. Thank you for playing.")
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )
      

# Main game function
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

# ASCII Art landing page, while loop which requires 'ready' to escape.
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
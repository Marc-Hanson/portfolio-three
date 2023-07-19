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
    print("I mean, that's what you should be doing... That is what you're going to do?")
    print("\n It's probably time to start 'work', the hardest part is starting!")
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
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
      break
    elif player_choice == "drink":
      print("\n----------------------------------------------------------------------\n")
      print("You open up 'Lo-Fi chill hop beats to study slash relax to' and click play")
      print("Turn up the volume, put your feet up on the desk and close your eyes.")
      print("Bliss! Well, until you reach for for your trusty energy drink...")
      print("Which is lying on it's side, it's contents emptied all over your keyboard.")
      print("Wow... The day is over before it began. Back to bed?")
      break
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
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
      break
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords.")
   
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
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
      break
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
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
      break
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )
      
def good_choice_end_one():
  """
  Good path, dead end terminal. Currently in 'E'.
  Possible choices are endings '4' and '5'.
  """
  while True:
    print("\n----------------------------------------------------------------------")
    print("\n It's been a couple of hours now, you've watched a man making stone age tools")
    print("using only his hands. You've seen an American couple convert a van in to a camper")
    print("van. And you've wathced several episodes of How It's Made...")
    print("\n None of this is getting work done! Are you just going to watch 'more' videos?")
    print("Back to 'bed'!? You haven't done anything! Do not turn this computer off!")
    player_choice = input("It feels like all hope is gone and your mind is blank, what to do?\n")
    player_choice = player_choice.lower()
    if player_choice == "more":
      print("\n----------------------------------------------------------------------")
      print("Bonsai trimming masters. Bob Ross paintings. Theme park histories...")
      print("Rock climbing championships, backpacking videos, DIY aquariums and")
      print("Independent film making. You've wasted another day in a YouTube rabbit hole!")
      break
    elif player_choice == "bed":
      print("\n----------------------------------------------------------------------")
      print("Safe and warm, an episode of Family Guy playing on your phone next to you.")
      print("You're not watching, just listening, until you drift off back to sleep.")
      print("Behind schedule and extra work to do tomorrow? Not todays problem!")
      break
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
      break
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )

def good_choice_end_two():
  """
  Good path, dead end terminal. Currently in 'J'.
  Possible choices are endings '9' and '10'.
  """
  while True:
    print("\n----------------------------------------------------------------------")
    print("\n Mmmm, chocolate. There's a jumbo bag of peanut M&Ms that's been waiting for")
    print("you, and today is the day! You rip open and the bag and just a couple turns to")
    print("a few more won't hurt. You look down and you've eaten more than half of a bag...")
    print("\n Well, it's less than one portion left so you might as well 'finish' them off!")
    print("Or do you think you need a 'milkshake' to wash down this tasty snack.")
    player_choice = input("Don't do it! You're still young and have so much to live for!\n")
    player_choice = player_choice.lower()
    if player_choice == "milkshake":
      print("WHAT SORT OF IDEA WAS THIS!? You were already full, now you can barely move!")
      print("You sit there with less than half a milkshake and a few M&Ms left over, but,")
      print("we both know you're not going to stop there. You enter a food coma and die.")
      break
    elif player_choice == "finish":
      print("TOO... MUCH... CHOCOLATE! It got out of hand and now you feel too sick to study.")
      print("What a day... You can go out later and buy a new bag to replace the one you've")
      print("devoured today. What are the chances this will happen again tomorrow?")
      break
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )

def secret_ending():
  """
  Good path, secret ending. Currently in 'L'.
  Possible choices are endings '12', '13' and '15'.
  """
  while True:
    print("\n----------------------------------------------------------------------")
    print("\n The password was password!? You need to change that... Unbelievable.")
    print("Apart from that, you're becoming a code master! Projects submitted and all of this")
    print("hard work is starting to pay off. You're having fun and making the most of things.")
    print("\n Maybe it's time for some 'music'.")
    print("Or a terrible 'joke'?")
    print("Or are you just here for the 'hero' ending? Typical...")
    player_choice = input("\n")
    player_choice = player_choice.lower()
    if player_choice == "music":
      print("\n----------------------------------------------------------------------\n")
      print("Never gonna give you up")
      print("Never gonna let you down")
      print("Never gonna run around and desert you.")
      print("Never gonna make you cry")
      print("Never gonna say goodbye")
      print("Never gonna tell a lie and hurt you!")
      break
    if player_choice == "joke":
      print("\n----------------------------------------------------------------------\n")
      print("Why is Voldemort so good with computers?")
      print("...")
      print("He's fluent in Python (worth it, right?)")
      break
    if player_choice == "hero":
      print("\n----------------------------------------------------------------------\n")
      print("\n Your hard work has been noticed and you're noticed by top companies on LinkedIn")
      print("Using your coding knowledge you've built apps that detect and help eliminate")
      print("almost every known disease to humankind. Oh, and you're like super rich. And")
      print("erm, lots of very attractive, funny, amazing people all want to marry you!")
      print(f"\n All because you decided to {choices[0]}, use {choices[1]} and write pro {choices[2]}.")
      print("Excellent work, you're a god among coders <3")
      break
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
      break
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )
 
def bad_choice_one():
  """
  Bad path, first choice. currently in B.
  Possible choices are 'D' and 'F'.
  """
  while True:
    print("\n----------------------------------------------------------------------\n")
    print("Just one one lttle game right? You boot up World of Warcraft to check your")
    print("auctions and somebody is starting a group for that dungeon you need! You can")
    print("get so many quests done in one quick run. ")
    print("\n Let's go, finish 'fast' and get back to studying! Or 'close' the game and")
    print("focus up. You've delayed things enough.")
    player_choice = input("It's your choice thoough... I'm just a text interface.\n")
    player_choice = player_choice.lower()
    if player_choice == "fast":
      choices.append("fast")
      break
    elif player_choice == "close":
      choices.append("close")
      break
    elif player_choice == "quit":
      print("Game terminated. Thank you for playing.")
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )

def bad_choice_two():
  """
  Bad path, first choice. currently in F.
  Possible choices are 'H' and ending '7'.
  """
  while True:
    print("\n----------------------------------------------------------------------\n")
    print("Focus, focus, focus! You're in the zone! The study zone! No more stalling.")
    print("You open up your emails to clear out all the spam and see if there are any")
    print("updates from your course provider.")
    print("\n You've won an air fryer! It's not a competition you remember entering but")
    print("it IS a free air fryer. Let's 'claim' it! Or delete it and just go back to a")
    print("'regular' non air frying lifestlye.")
    player_choice = input("Can you resist that perfectly cooked crispy goodness?\n")
    player_choice = player_choice.lower()
    if player_choice == "regular":
      choices.append("regular")
      break
    elif player_choice == "claim":
      print("You click CLAIM NOW. Download the claim form to fill out and... Hmm, your")
      print("mouse has stopped working. Ctrl+Alt+Del... nope. Alt+F4... nope. ESC ESC!")
      print("Files downloading? This isn't good! You PC powers down and won't reboot.")
      print("It's not a cheap life lesson but it's an important one. Your game is over!")
      break
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )

def bad_choice_three():
  """
  Bad path, first choice. currently in H.
  Possible choices are 'K' and ending '8'.
  """
  while True:
    print("\n----------------------------------------------------------------------\n")
    print("Still struggling to start, but you're still trying your best! I mean, how many")
    print("more distractions could there possible be? It's hard to concentrate on an empty")
    print("stomach. Your stomach grumbles away, and you go to the kitchen to check for food.")
    print("\n There's nothing that catches your eye, just a quick run to the local 'shop'")
    print("to pick up some treats. Make something with what you already have at 'home', you")
    print("need to get to work!")
    player_choice = input("\n Make a something with food you have at home or go out shopping?")
    player_choice = player_choice.lower()
    if player_choice == "home":
      choices.append("home")
      break
    elif player_choice == "shop":
      print("You put on some shoes and head out to the shops, on your walk there you notice")
      print("an advertisement for 50% off a Playstation 5 at a store not far from here. WOW!")
      print("This is too good to pass up, you forget how hungry you are and are consumed only")
      print("by the dream of finally owning a next gen console. No more time to study!")
      break
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )

def bad_choice_four():
  """
  Bad path, first choice. currently in H.
  Possible choices are endings '11' and '14'.
  """
  while True:
    print("\n----------------------------------------------------------------------\n")
    print("")
    print("\n")
    player_choice = input("\n")
    player_choice = player_choice.lower()
    if player_choice == "continue":
      print("")
      break
    elif player_choice == "lost":
      print("")
      break
    else:
      print(f"You entered '{player_choice}', please enter one of the given keywords." )

# Main game function.
def main_game():
  """
  Main game functions, will run in order as the game progresses.
  """
  big_choice()
  if "work" in choices: 
    good_choice_one()
    if "slack" in choices:
      good_choice_two()
      if "code" in choices:
        good_choice_three()
      elif "chocolate" in choices:
        good_choice_end_two()
    elif "youtube" in choices:
      good_choice_end_one()
  elif "game" in choices:
    bad_choice_one()
  if "work" and "slack" and "code" in choices:
    secret_ending()

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
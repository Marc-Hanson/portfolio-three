def main_game():
  """
  Main game functions, will run in order as the game progresses.
  """
  first_choice()
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
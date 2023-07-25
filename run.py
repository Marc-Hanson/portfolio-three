# Import statements.
import colorama
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init(autoreset=True)

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
        print(f"\n It's probably time to start {Fore.GREEN}'work'{Style.RESET_ALL}, the hardest part is starting!")
        print(f"Just one quick {Fore.GREEN}'game'{Style.RESET_ALL}? I mean, you have got ALL day to study...")
        print(f"Feet up, music on and finish your {Fore.GREEN}'drink'{Style.RESET_ALL}. You need that caffeine.")
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
            choices.clear()
            break
        elif player_choice == "drink":
            print("\n----------------------------------------------------------------------\n")
            print("You open up 'Lo-Fi chill hop beats to study slash relax to' and click play")
            print("Turn up the volume, put your feet up on the desk and close your eyes.")
            print("Bliss! Well, until you reach for for your trusty energy drink...")
            print("Which is lying on it's side, it's contents emptied all over your keyboard.")
            print("Wow... The day is over before it began. Back to bed?")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")
        break


# Good day functions.

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
        print(f"\n It's ok, you've got this. Check through {Fore.GREEN}'slack'{Style.RESET_ALL} and see if there's any tips.")
        print(f"Or open {Fore.GREEN}'youtube'{Style.RESET_ALL} and come back to it in a little bit, it's too early for this.")
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
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


def good_choice_two():
    """
    Good path, second choice. Currently in 'G'.
    Possible choices are 'I' and 'J'.
    """
    while True:
        print("\n----------------------------------------------------------------------")
        print("\n It a lot of work! But you're sticking with it. It doesn't make complete sense")
        print("but that's ok. You're starting to understand what you can do even if you can't")
        print("write it alone or even recite what was on the previous page. But it's enough.")
        print(f"\n Maybe if you grabbed a snack, some {Fore.GREEN}'chocolate'{Style.RESET_ALL}? It would all make sense.")
        print(f"Take a sip of your drink and play with the {Fore.GREEN}'code'{Style.RESET_ALL} to figure out how it works.")
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
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


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
        print(f"You can close your terminal by typing {Fore.GREEN}'quit'{Style.RESET_ALL} or guess the secret {Fore.GREEN}'password'{Style.RESET_ALL}.")
        player_choice = input("It feels like all hope is gone and your mind is blank, what to do?\n")
        player_choice = player_choice.lower()
        if player_choice == "password":
            choices.append("password")
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


# Good day end nodes.

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
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "bed":
            print("\n----------------------------------------------------------------------")
            print("Safe and warm, an episode of Family Guy playing on your phone next to you.")
            print("You're not watching, just listening, until you drift off back to sleep.")
            print("There will always be other days to study. Naps are priceless.")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")
        break


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
        print(f"\n Well, it's less than one portion left so you might as well {Fore.GREEN}'finish'{Style.RESET_ALL} them off!")
        print(f"Or do you think you need a {Fore.GREEN}'milkshake'{Style.RESET_ALL} to wash down this tasty snack.")
        player_choice = input("Don't do it! You're still young and have so much to live for!\n")
        player_choice = player_choice.lower()
        if player_choice == "milkshake":
            print("\n----------------------------------------------------------------------")
            print("WHAT SORT OF IDEA WAS THIS!? You were already full, now you can barely move!")
            print("You sit there with less than half a milkshake and a few M&Ms left over, but,")
            print("we both know you're not going to stop there. You enter a food coma and die.")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "finish":
            print("\n----------------------------------------------------------------------")
            print("TOO... MUCH... CHOCOLATE! It got out of hand and now you feel too sick to study.")
            print("What a day... You can go out later and buy a new bag to replace the one you've")
            print("devoured today. What are the chances this will happen again tomorrow?")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


# Good day perfect ending.

def secret_ending():
    """
    Good path, secret ending. Currently in 'L'.
    Possible choices are endings '12', '13' and '15'.
    """
    while True:
        print("\n----------------------------------------------------------------------")
        print("\n The password was password!? You need to change that... Unbelievable.")
        print("Apart from that, you're becoming a code master! Projects submitted and your")
        print("hard work is starting to pay off. You're having fun and killing it.")
        print(f"\n Maybe it's time for some {Fore.GREEN}'music'{Style.RESET_ALL}.")
        print(f"Or a terrible {Fore.GREEN}'joke'{Style.RESET_ALL}?")
        print(f"Or are you just here for the {Fore.GREEN}'hero'{Style.RESET_ALL} ending? Typical...")
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
        elif player_choice == "joke":
            print("\n----------------------------------------------------------------------\n")
            print("Why is Voldemort so good with computers?")
            print("...")
            print("He's fluent in Python (worth it, right?)")
            break
        elif player_choice == "hero":
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
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


# Bad day functions.

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
        print(f"\n Let's go, finish {Fore.GREEN}'fast'{Style.RESET_ALL} and get back to studying! Or {Fore.GREEN}'close'{Style.RESET_ALL} the game and")
        print("focus up. You've delayed things enough.")
        player_choice = input("It's your choice though... I'm just a text interface.\n")
        player_choice = player_choice.lower()
        if player_choice == "fast":
            choices.append("fast")
            break
        elif player_choice == "close":
            choices.append("close")
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


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
        print(f"it IS a free air fryer. Let's {Fore.GREEN}'claim'{Style.RESET_ALL} it! Or delete it and just go back to a")
        print(f"{Fore.GREEN}'regular'{Style.RESET_ALL} non air frying lifestlye.")
        player_choice = input("Can you resist that perfectly cooked crispy goodness?\n")
        player_choice = player_choice.lower()
        if player_choice == "regular":
            choices.append("regular")
            break
        elif player_choice == "claim":
            print("\n----------------------------------------------------------------------")
            print("You click CLAIM NOW. Download the claim form to fill out and... Hmm, your")
            print("mouse has stopped working. Ctrl+Alt+Del... nope. Alt+F4... nope. ESC ESC!")
            print("Files downloading? This isn't good! You PC powers down and won't reboot.")
            print("It's not a cheap life lesson but it's an important one. Your game is over!")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


def bad_choice_three():
    """
    Bad path, first choice. currently in H.
    Possible choices are 'K' and ending '8'.
    """
    while True:
        print("\n----------------------------------------------------------------------\n")
        print("Still struggling to start, but you're still trying your best! I mean, how many")
        print("more distractions could there possible be? It's hard to concentrate on an empty")
        print("stomach. Your stomach grumbles away, you go to the kitchen to check for food.")
        print(f"\n There's nothing that catches your eye, just a quick run to the local {Fore.GREEN}'shop'{Style.RESET_ALL}")
        print(f"to pick up some treats. Make something with what you already have at {Fore.GREEN}'home'{Style.RESET_ALL}, you")
        print("need to get to work!")
        player_choice = input("Make a something with food you have at home or go out shopping? \n")
        player_choice = player_choice.lower()
        if player_choice == "home":
            choices.append("home")
            break
        elif player_choice == "shop":
            print("\n----------------------------------------------------------------------")
            print("You put on some shoes and head out to the shops, on your walk there you notice")
            print("an advertisement for 50% off a Playstation 5 at a store not far from here. WOW!")
            print("This is too good to pass up, you forget how hungry you are and are consumed only")
            print("by the dream of finally owning a next gen console. No more time to study!")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


def bad_choice_four():
    """
    Bad path, first choice. currently in H.
    Possible choices are endings '11' and '14'.
    """
    while True:
        print("\n----------------------------------------------------------------------\n")
        print("You've finished your drink, ate your food, been distracted and came though it")
        print("all and you're still here. It's not always easy but you should be rewarded for")
        print("your efforts!")
        print(f"\n Open up your {Fore.GREEN}'IDE'{Style.RESET_ALL} and get to work, the day is wasting away. Let's get")
        print("something written. It doesn't have to be world changing but every little step")
        print(f"is progress. Kind of a {Fore.GREEN}'face'{Style.RESET_ALL} down on the keyboard and cry kind of day?")
        player_choice = input("You're so close... Write something, anything!\n")
        player_choice = player_choice.lower()
        if player_choice == "ide":
            print("\n----------------------------------------------------------------------")
            print("You're in and writing! It's not fast and it's not flashy but it's progress!")
            print("It's a marathon not a sprint and you're still here at the finish line. Great")
            print("effort! Another day you've made a step in the right direction.")
            break
        elif player_choice == "face":
            print("\n----------------------------------------------------------------------")
            print("We've all been there, it's just not your day. Take a break, grab a cup of tea,")
            print("don't get downhearted and you can try again tomorrow. It's not the perfect run")
            print("but you've put the work in! Good job.")
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


# Bad day perfect end.

def bad_choice_end():
    """
    Bad path, dead end terminal. Currently in 'D'.
    Possible choices are endings '2', '3' and '6'.
    """
    while True:
        print("\n----------------------------------------------------------------------")
        print("\n It's been two hours of dying in a dungeon, with the same angry group of")
        print("kids. They've insulted your mom, your pc, your dog, your voice. It's all your")
        print("fault, apparently...")
        print(f"\n Do you unleash your inner {Fore.GREEN}'demon'{Style.RESET_ALL} and rage at these nerds? Can you keep your")
        print(f"cool and {Fore.GREEN}'clear'{Style.RESET_ALL} the last boss? Or just {Fore.GREEN}'ragequit'{Style.RESET_ALL} out and leave them to it?")
        player_choice = input("I mean there are no right answers are there, what do you think?\n")
        player_choice = player_choice.lower()
        if player_choice == "demon":
            print("\n----------------------------------------------------------------------")
            print("CAPS MODE ACTIVATED! YOU RAGE AND SMASH AT THE KEYS USING EVERY EXPLITIVE YOU")
            print("KNOW! KEYCAPS ARE FLYING! THE SCREEN FLICKERS AND FALLS FROM THE TABLE AS YOUR")
            print("INNER HULK BREAKS FREE. THERE WILL BE NO STUDYING TODAY, THIS IS LIFE NOW!")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "clear":
            print("\n----------------------------------------------------------------------")
            print("You hide the chat window and keep doing what you're doing. It takes a while and")
            print("a couple more attempts but you get the dungeon finished. Your quests are done!")
            print("Success. Wait, it's getting dark and we didn't study!?")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "ragequit":
            print("\n----------------------------------------------------------------------")
            print("You close the game, throw your headset on the keyboard and stare in to the middle")
            print("distance. Energy levels depleted and filled with a fresh hatred for anybody and")
            print("everybody. Maybe online gaming just isn't for you, other people just make you angry.")
            while True:
                end_game = input(f"\nGame over! Do you wish to try again, {Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}?\n")
                end_game = end_game.lower()
                if end_game == "yes":
                    choices.clear()
                    print("\n----------------------------------------------------------------------\n")
                    main_game()
                elif end_game == "no":
                    print("\n----------------------------------------------------------------------\n")
                    print("Game terminated. Thank you for playing.")
                    choices.clear()
                    break
                else:
                    print(f"You entered {Fore.GREEN}{end_game}{Style.RESET_ALL}, please enter one of the given keywords.")
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL}, please enter one of the given keywords.")


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
                if "work" and "slack" and "code" in choices:
                    secret_ending()
            elif "chocolate" in choices:
                good_choice_end_two()
        else:
            good_choice_end_one()
    elif "game" in choices:
        bad_choice_one()
        if "close" in choices:
            bad_choice_two()
            if "regular" in choices:
                bad_choice_three()
                if "home" in choices:
                    bad_choice_four()
    else:
        bad_choice_end()


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
print(f"{Fore.GREEN}'keyword'{Style.RESET_ALL} highlighted in quotes to progress through the day.")
print(f"You can also type {Fore.GREEN}'quit'{Style.RESET_ALL} at any time to leave the game.")
while True:
    game_start = input(f"\nAre you {Fore.GREEN}'ready'{Style.RESET_ALL} to wake up in the life of a coding student?\n")
    game_start = game_start.lower()
    if game_start == "ready":
        break
    elif game_start == "quit":
        print("Not now... You didn't even start playing! Do you think that's funny?")
    elif game_start == "keyword":
        print("Yes... that is a keyword. But it's not the right one, try again.")
    else:
        print(f"That's ok, we can wait until you're {Fore.GREEN}'ready'{Style.RESET_ALL}...\n")    
main_game()

# Import statements.
import colorama
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
colorama_init(autoreset=True)

# Stores choices from user input for path selection.
choices = []


# Map of the project is included as an image in inside the Readme.
def big_choice():
    """
    First set of choices, you are currently in 'A'.
    Possible choices are 'B', 'C' and ending number '1'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n

You wake up, put on some clothes, grab a can of caffeinated energy drink, and
sit in front of your computer screen, ready for another day of coding. Well,
That's what you should be doing. That's what you're going to do, right?
It's probably time to start {Fore.GREEN}'work'{Style.RESET_ALL}, the hardest
part is starting! Or maybe just one quick {Fore.GREEN}'game'{Style.RESET_ALL}?
I mean, you have all day to study. Or just put your feet up, put on some music.
And finish your {Fore.GREEN}'drink'{Style.RESET_ALL}. You need some
caffeine before your brain starts to work.


""")
        player_choice = input("""
Urgh, mornings... What are you going to do?
""")
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
            print("""
\n----------------------------------------------------------------------------\n
You open up 'Lo-Fi chill hop beats to study slash relax to' and click play.
Turn up the volume, put your feet up on the desk, and close your eyes. Bliss!
Well, until you reach for your trusty energy drink. Which is lying on it's
side, its contents emptied all over your keyboard. The day is over before it
even really began. What an expensive lesson to learn...
""")
            game_over()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")

# Good day functions.


def good_choice_one():
    """
    Good path, first choice. You are currently in 'C'.
    Possible choices are 'E' and 'G'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
You're up and running! You load up your favorite IDE, find the bookmark for
your latest online lesson and hit play. You take a sip of caffeine++ and try to
zone in on what's going on. Superclasses? Mixins!? Inheritance. What?
It's okay; you've got this. Check through {Fore.GREEN}'slack'{Style.RESET_ALL}
and see if there are any tips. Or open {Fore.GREEN}'youtube'{Style.RESET_ALL}
and come back to it in a little bit, it's too early for this.
""")
        player_choice = input("""
It feels like all hope is gone and your mind is blank, what to do?
""")
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
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


def good_choice_two():
    """
    Good path, second choice. You are currently in 'G'.
    Possible choices are 'I' and 'J'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
It's a lot of work! But you're sticking with it. It doesn't make complete sense
but that's okay. You're starting to understand what you can do, even if you
can't write it alone or even recite what was on the previous page, but it's
enough. Maybe if you grabbed a snack, some {Fore.GREEN}'chocolate'
{Style.RESET_ALL}? It would all make sense. Or take a sip of your drink and
play with the {Fore.GREEN}'code'{Style.RESET_ALL} to figure out how it works.
""")
        player_choice = input("""
It's so easy to get distracted, what will you do?
""")
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
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


def good_choice_three():
    """
    Good path, third choice. You are currently in 'I'.
    Possible choices are 'L' - The secret ending.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
You've done it! You've worked hard and pushed through to get another day done.
Now the day is yours to enjoy. Take a deep breath and relax those shoulders!
You've committed and pushed your code for the day, and you're ahead of
schedule! You can close your terminal by typing {Fore.GREEN}'quit'
{Style.RESET_ALL} or guess the secret {Fore.GREEN}'password'{Style.RESET_ALL}.
""")
        player_choice = input(f"""
Secret {Fore.GREEN}'password'{Style.RESET_ALL}, hmm. What could it be?
""")
        player_choice = player_choice.lower()
        if player_choice == "password":
            choices.append("password")
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


# Good day end nodes.

def good_choice_end_one():
    """
    Good path, dead end terminal. You are currently in 'E'.
    Possible choices are endings '4' and '5'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
It's been a couple of hours now, and you've watched a man make Stone Age tools
using only his hands. You've seen an American couple convert a van into a
Camper van. And you've watched several episodes of How It's Made... None of
this is getting work done! Are you just going to watch {Fore.GREEN}'more'
{Style.RESET_ALL} videos? Or back to {Fore.GREEN}'bed'{Style.RESET_ALL}!?
""")
        player_choice = input("""
You haven't done anything! Do not turn this computer off! Hello?
""")
        player_choice = player_choice.lower()
        if player_choice == "more":
            print("""
\n----------------------------------------------------------------------------\n
Bonsai trimming masters. Bob Ross paintings. Theme park histories. The world
Rock climbing championships, worldwide backpacking videos, DIY aquariums, and
Independent filmmaking. You've wasted another day in a YouTube rabbit hole!
""")
            game_over()
            break
        elif player_choice == "bed":
            print("""
\n----------------------------------------------------------------------------\n
Safe and warm, an episode of Family Guy is playing on your phone next to you.
You're not watching; you're just listening until you drift off back to sleep.
There will always be other days to study. Naps are priceless. Zzzzzzzzz...
""")
            game_over()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


def good_choice_end_two():
    """
    Good path, dead end terminal. You are currently in 'J'.
    Possible choices are endings '9' and '10'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
Mm mm, chocolate. There's a jumbo bag of peanut M&Ms that's been waiting for
you, and today is the day! You rip open the bag, and "just a couple" turns to
"A few more won't hurt. You look down, and you've eaten more than half of a
bag. Well, there's less than one portion left, so you might as well
{Fore.GREEN}'finish'{Style.RESET_ALL} them off! Or do you think you need a
{Fore.GREEN}'milkshake'{Style.RESET_ALL} to wash down this tasty snack.

""")
        player_choice = input("""
This isn't going to end well, what are you going to choose?
""")
        player_choice = player_choice.lower()
        if player_choice == "milkshake":
            print("""
\n----------------------------------------------------------------------------\n
WHAT SORT OF IDEA WAS THIS!? You were already full; now you can barely move!
You sit there with less than half a milkshake and a few M&Ms left over, but,
we both know you're not going to stop there. After finishing both the milkshake
and chocolate, you enter a food coma and die.
""")
            game_over()
            break
        elif player_choice == "finish":
            print("""
\n----------------------------------------------------------------------------\n
TOO. MUCH. CHOCOLATE! Things have really gotten out of hand, and now you
feel too sick to study. What a day... You can go out later and buy a new bag to
replace the one you've devoured today. What are the chances that this will
happen again tomorrow?
""")
            game_over()
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


# Good day perfect ending.

def secret_ending():
    """
    Good path, secret ending. You are currently in 'L'.
    Possible choices are endings '12', '13' and '15'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
The password was password!? You need to change that. Unbelievable. Apart from
that, you're becoming a code master! Projects have been submitted, and your
hard work is starting to pay off. You're having fun and killing it. Maybe it's
time for some {Fore.GREEN}'music'{Style.RESET_ALL}.
Or a terrible {Fore.GREEN}'joke'{Style.RESET_ALL}?
Are you just here for the {Fore.GREEN}'hero'{Style.RESET_ALL} ending? Typical.


""")
        player_choice = input("Final choice, no pressure!")
        player_choice = player_choice.lower()
        if player_choice == "music":
            print("""
\n----------------------------------------------------------------------------\n
Never gonna give you up!
Never gonna let you down,
Never gonna run around and desert you.
Never gonna make you cry,
Never gonna say goodbye.
Never gonna tell a lie and hurt you!
""")
            break
        elif player_choice == "joke":
            print("""
\n----------------------------------------------------------------------------\n
Why is Lord Voldemort so good with computers?
...
...
He's fluent in Python!
(worth it, right?)
""")
            break
        elif player_choice == "hero":
            print(f"""
\n----------------------------------------------------------------------------\n
Your hard work has been noticed, and you're noticed by top companies on
LinkedIn. Using your coding knowledge, you've built apps that detect and help
eliminate almost every known disease to humankind. Oh, and you're like super
rich. And erm, lots of very attractive, funny, amazing people all want to marry
you!
Excellent work, you're a god among coders <3
""")
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


# Bad day functions.

def bad_choice_one():
    """
    Bad path, first choice. currently in B.
    Possible choices are 'D' and 'F'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
Just one little game, right? You boot up World of Warcraft to check your
mailbox and somebody is starting a group for that dungeon you need! You can get
so many quests done in one quick run. Let's go, finish {Fore.GREEN}'fast'
{Style.RESET_ALL} and get back to studying! Or {Fore.GREEN}'close'
{Style.RESET_ALL} the game and focus up. You've probably delayed things enough.
""")
        player_choice = input("""
It's your choice though... I'm just a text interface. What will it be?
""")
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
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


def bad_choice_two():
    """
    Bad path, first choice. You are currently in F.
    Possible choices are 'H' and ending '7'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
Focus, focus, focus! You're in the zone! The study zone! No more stalling. You
open up your emails to clear out all the spam and see if there are any updates
from your course provider. You've won an air fryer! It's not a competition you
remember entering, but it IS a free air fryer. Let's {Fore.GREEN}'claim'
{Style.RESET_ALL} it! Or delete it and just go back to a {Fore.GREEN}'regular'
{Style.RESET_ALL} non-air-frying lifestyle.

""")
        player_choice = input("""
Uh oh! Can you resist that perfectly cooked crispy goodness?
""")
        player_choice = player_choice.lower()
        if player_choice == "regular":
            choices.append("regular")
            break
        elif player_choice == "claim":
            print("""
\n----------------------------------------------------------------------------\n
You click CLAIM NOW. Download the claim form to fill out and... Hmm, your mouse
has stopped working. Ctrl+Alt+Del... nope. Alt+F4... nope. ESC ESC! Files
downloading? This isn't good! Your PC powers down and won't reboot. It's not a
cheap life lesson, but it's an important one. Your game is over!
""")
            game_over()
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


def bad_choice_three():
    """
    Bad path, first choice. You are currently in H.
    Possible choices are 'K' and ending '8'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
You're struggling to start, but you're still trying your best! I mean, how many
more distractions could there possible be? It's hard to concentrate on an empty
stomach. Your stomach grumbles away, and you go to the kitchen to check for
food. There's nothing that catches your eye, just a quick run to the local
{Fore.GREEN}'shop'{Style.RESET_ALL} to pick up some treats. Make something with
what you already have at {Fore.GREEN}'home'{Style.RESET_ALL}, you need to get
started with this work!
""")
        player_choice = input("""
Make a something with food you have at home or go out shopping?
""")
        player_choice = player_choice.lower()
        if player_choice == "home":
            choices.append("home")
            break
        elif player_choice == "shop":
            print("""
\n----------------------------------------------------------------------------\n
You put on some shoes and head out to the shops. On your walk there, you notice
an advertisement for 50% off a PlayStation 5 at a store not far from here. WOW!
This is too good to pass up; you forget how hungry you are and are consumed
only by the dream of finally owning a next-gen console. Your hands slowly morph
into controller-shaped claws, and you're no longer able to study.
""")
            game_over()
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


def bad_choice_four():
    """
    Bad path, first choice. You are currently in H.
    Possible choices are endings '11' and '14'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
You've finished your drink, eaten your food, been distracted, and come through
it all, and you're still here. It's not always easy, but you should be rewarded
for your efforts! Open up your {Fore.GREEN}'IDE'{Style.RESET_ALL} and get to
work; the day is wasting away. Let's get something written. It doesn't have to
be world changing, but every little step is progress. Or is it more a
{Fore.GREEN}'face'{Style.RESET_ALL} down on the keyboard and cry kind of day?
""")
        player_choice = input("You're so close... Write something, anything!")
        player_choice = player_choice.lower()
        if player_choice == "ide":
            print("""
\n----------------------------------------------------------------------------\n
You're in and writing! It's not fast, and it's not flashy, but it's progress!
It's a marathon, not a sprint, and you're still here at the finish line. Great
effort! Another day, you've made a step in the right direction. Well done :)
""")
            break
        elif player_choice == "face":
            print("""
\n----------------------------------------------------------------------------\n
We've all been there; it's just not your day. Take a break, grab a cup of tea,
don't get downhearted, and you can try again tomorrow. It's not the perfect run
but you've put the work in! Good job trying your best.
""")
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


# Bad day perfect end.

def bad_choice_end():
    """
    Bad path, dead end terminal. Currently in 'D'.
    Possible choices are endings '2', '3' and '6'.
    """
    while True:
        print(f"""
\n----------------------------------------------------------------------------\n
It's been two hours of dying in a dungeon with the same angry group of kids.
They've insulted your mom, your PC, your dog, and your voice. It's all your
fault, apparently... Do you unleash your inner {Fore.GREEN}'demon'
{Style.RESET_ALL} and rage at these nerds? Can you keep your cool and
{Fore.GREEN}'clear' {Style.RESET_ALL} the last boss? Or {Fore.GREEN}'ragequit'
{Style.RESET_ALL} out and leave them to it?
""")
        player_choice = input("""
I mean there are no right answers now are there, what do you think?
""")
        player_choice = player_choice.lower()
        if player_choice == "demon":
            print("""
\n----------------------------------------------------------------------------\n
CAPS MODE ACTIVATED! YOU RAGE AND SMASH AT THE KEYS, USING EVERY EXPLETIVE YOU
KNOW! KEYCAPS ARE FLYING! THE SCREEN FLICKERS AND FALLS FROM THE TABLE AS YOUR
INNER HULK BREAKS FREE. THERE WILL BE NO STUDYING TODAY; THIS IS YOUR LIFE NOW!
""")
            game_over()
            break
        elif player_choice == "clear":
            print("""
\n----------------------------------------------------------------------------\n
You hide the chat window and keep doing what you're doing. It takes a while,
and a couple more attempts, but you get the dungeon finished. Your quests are
done! Success. Wait, it's getting dark and we didn't study!? Uh oh...
""")
            game_over()
            break
        elif player_choice == "ragequit":
            print("""
\n----------------------------------------------------------------------------\n
You close the game, throw your headset on the keyboard, and stare into the
middle distance. Energy levels were depleted and filled with a fresh hatred for
anybody and everybody. Maybe online gaming just isn't for you; maybe you should
delete the games and remove that temptation for next time?
""")
            game_over()
            break
        elif player_choice == "quit":
            print("Game terminated. Thank you for playing.")
            choices.clear()
            break
        else:
            print(f"""
You entered {Fore.GREEN}{player_choice}{Style.RESET_ALL},
please enter one of the given keywords.
""")


# Main game function.
def main_game():
    """
    Main game logic, will run in order as the game progresses.
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
                return
        elif "youtube" in choices:
            good_choice_end_one()
            return
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
            return


# Game over function.
def game_over():
    """
    Function to provide replay game loop without restarting app.
    """
    while True:
        end_game = input(f"""
\n Game over! Do you wish to try again,
{Fore.GREEN}'yes'{Style.RESET_ALL} or {Fore.GREEN}'no'{Style.RESET_ALL}? \n
""")
        end_game = end_game.lower()
        if end_game == "yes":
            choices.clear()
            print("""
\n----------------------------------------------------------------------------\n
""")
            main_game()
        elif end_game == "no":
            print("""
\n----------------------------------------------------------------------------\n
""")
            print("Game terminated. Thank you for playing.")
            choices.clear()
            return
        else:
            print(f"""
You entered {Fore.GREEN}{end_game}{Style.RESET_ALL},
please enter one of the given keywords.
""")


# ASCII Art landing page, while loop which requires 'ready' to escape.
print("""
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
print(f"""
Welcome to 'A Day in the Life', a text-based adventure through a day in the
life of a coding student. All you need to do is type out the {Fore.GREEN}
'keyword'{Style.RESET_ALL} highlighted in quotes to progress through the day.
You can also type the keyword {Fore.GREEN}'quit'{Style.RESET_ALL} at any point
during play to leave the game.
""")
while True:
    game_start = input(f"""
Are you {Fore.GREEN}'ready'{Style.RESET_ALL} to wake up and begin?
""")
    game_start = game_start.lower()
    if game_start == "ready":
        break
    elif game_start == "quit":
        print("\n Not now... You didn't even start playing! Try again. \n")
    elif game_start == "keyword":
        print("\n Yes... that is a keyword. But it's not the right one. \n")
    else:
        print(f"""
That's ok, we can wait until you're {Fore.GREEN}'ready'{Style.RESET_ALL}.
""")
main_game()

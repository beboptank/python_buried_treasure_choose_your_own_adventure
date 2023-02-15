print("""  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     //    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    // " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    "/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------
 \_/__________________________________________________________________/""")

print("Welcome to Buried Treasure, a text-based choose your own adventure game.\n")
print("ASCII art from www.ascii.co.uk/art")
answer1 = input("You awaken on a deserted island with a piece of parchment in your hand. Open it? Y or N ")

if answer1 == 'Y' or answer1 == 'y':
    print("\nYou open the parchment.")
    answer2 = input("It's a treasure map! There are two Xs on the map - one to the northeast and one to the "
                    "northwest. Which way do you go? Type 1 for northeast, 2 for northwest ")
    if answer2 == '2':
        print("\nYou begin walking to the northwest.")
        answer3 = input("You come to a river. You can swim across or use the old wooden bridge. What do you do? Type "
                        "swim or bridge ")
        if answer3 == 'bridge':
            print("\nYou cross the bridge quickly without incident.")
            print("You arrive at the X on the map and begin to dig with your hands. Soon enough, you dig up a heavy "
                  "chest and open it. It's full of TREASURE! YOU WIN!")
        else:
            print("\nYou try to swim across, but the river is full of alligators. Uh-oh. GAME OVER")
    else:
        print("\nYou head northeast. Shortly after beginning your journey, you fall into a well-disguised hole full of "
              "snakes. GAME OVER")
else:
    print("\nYou decide not to open the parchment. You spend the rest of your brief life waiting for help to come to "
          "the island. GAME OVER")
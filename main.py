import random

# Rules of Nim:
# 1. Game starts with 21 matches
# 2. Players can take 1-3 matches
# 3. Player 1 always starts first
# 4. Players take turns taking matches
# 5. Player that takes the last match is the winner

# Choose between PvP or PvE:
print("Choose the mode: PvP, PvE")
mode = input(">>> ").lower()
while mode not in ["pvp", "pve"]:  # Validating input
    print("Incorrect input. Please choose between PvP and PvE")
    mode = input(">>> ").lower()
print()  # Blank space

# Choose difficulty if PvE
difficulty = "???"
if mode == "pve":
    print("Choose difficulty: Easy, Normal, Hard")
    difficulty = input(">>> ").lower()
    while difficulty not in ["easy", "normal", "hard", ""]:  # Validating input + a secret bot difficulty
        print("Incorrect input. Please choose between Easy, Normal and Hard")
        difficulty = input(">>> ").lower()
    print()  # Blank space
    if difficulty == "":
        difficulty = "???"  # Renaming

# Players choose nicknames
print("Player 1 - Choose a nickname:")
player_1 = input(">>> ")  # Naming a first player
if mode == "pve":
    if difficulty == "???":
        player_2 = "???"  # Who is it?
    else:
        player_2 = f"{difficulty.capitalize()} Bot"  # Generating bot name
else:
    print("Player 2 - Choose a nickname:")
    player_2 = input(">>> ")  # Naming a second player
print()  # Blank space

# Choosing rules: Default/Custom
print("Would you like to have Default or Custom rules?")
rules = input(">>> ").lower()
while rules not in ["default", "custom"]:  # Validating input
    print("Incorrect input. Please choose between Default and Custom")
    rules = input(">>> ").lower()
print()  # Blank space

# Defining default rules
max_matches = 21
min_take = 1
max_take = 3

# Players define custom rules
if rules == "custom":
    print("Choose amount of matches to have:")
    while True:
        try:
            max_matches = int(input(">>> "))
            if max_matches < 0:  # There can't be less than no matches
                raise ValueError
            break
        except ValueError:  # Matches must be a number
            print("Input must be a natural number.")

    print("Choose a minimum amount of matches that can be taken:")
    while True:
        try:
            min_take = int(input(">>> "))
            break
        except ValueError:  # Matches must be an integer (we allow negatives for the fun of it)
            print("Input must be an integer.")

    print("Choose a maximum amount of matches that can be taken:")
    while True:
        try:
            max_take = int(input(">>> "))
            if min_take > max_take:  # Error: The minimum is higher than the maximum
                raise ValueError
            break
        except ValueError:  # Matches must be an integer (we allow negatives for the fun of it)
            print("Input must be an integer and higher than the minimum.")

# Unlocked
unlocked = []

# Creating a game loop
running = True
while running:

    # Unknown
    unknowns = [f"??? ate all the matches and walked away with pride and a weird aftertaste.",
                 f"??? lit the matches on fire and ran away in fear.",
                 f"??? created a skyscraper out of the matches, but it fell.",
                 f"??? distracted you and stole the matches while you weren't looking.",
                 f"??? was your own imagination. You, I mean... it, had all the matches from the start.",
                 f"??? bought a match box, placed down new matches, and took them back again.",
                 f"??? hacked the matches and they all self destructed carefully.",
                 f"??? cheated in a fair game, the police got him, but shot the matches.",
                 f"??? made a mistake of not making any mistakes during the game.",
                 f"??? matched the matches in a match of matching match matches.", ]
    sentence = random.choice(unknowns)

    # Resetting
    matches = max_matches
    take = 0

    # Defining who goes second (due to a switch at the start)
    active_player = player_2
    if mode == "pve" and difficulty == "???":
        active_player = player_1

    # Wisdom of ???
    if len(unlocked) == len(unknowns):
        sentence = f"{active_player} saw through ???'s moves and took the match that was hidden in {active_player}'s pocket."
        active_player = player_2
    elif sentence not in unlocked:
        unlocked.append(sentence)

    # Setup is complete, now it is time to play
    while matches > 0:

        # Switching users
        if active_player == player_1:
            active_player = player_2
        else:
            active_player = player_1

        # Start information
        print(f"Right now there are {matches} matches.")
        print(f"Only from {min_take} to {max_take} matches can be taken.")

        # Bot taking matches
        if mode == "pve" and (active_player == player_2 or difficulty == "???"):
            if difficulty == "easy":
                take = random.randint(min_take, max_take)
                while take == matches % (max_take + 1) or take >= matches > min_take:
                    take = random.randint(min_take, max_take)

            elif difficulty == "normal":
                take = random.randint(min_take, max_take)
                if matches <= max_take:
                    take = matches

            elif difficulty == "hard":
                take = matches % (max_take + 1)
                if take == 0:
                    take = random.randint(min_take, max_take)

            else:  # ??? difficulty
                print(sentence)
                matches = 0

        # Players taking matches, also validating and adjusting slightly
        else:
            try:
                take = int(input(f"{active_player} >>> "))
            except ValueError:
                take = random.randint(min_take, max_take)
                if take > matches:
                    take = matches
                print(f"{active_player} got confused in the process and took {take} matches instead.")

        # Special unknown
        if mode != "pve" or difficulty != "???":

            # Extra validation and correctness: Less than minimum
            if take < min_take:
                take = min_take
                if take > matches:
                    take = matches
                    print(f"{active_player} tried taking more matches than there already are, so {active_player} took {matches} matches instead.")
                else:
                    print(f"{active_player} tried taking less than {min_take}, but failed and took {min_take} matches instead.")

            # Extra validation and correctness: More than maximum
            elif take > max_take:
                take = max_take
                if take > matches:
                    take = matches
                    print(f"{active_player} tried taking more matches than there already are, so {active_player} took {matches} matches instead.")
                else:
                    print(f"{active_player} tried taking more than {max_take}, but failed and took {max_take} matches instead.")

            # Extra validation and correctness: Not enough matches
            elif take > matches:
                take = matches
                print(f"{active_player} tried taking more matches than there already are, so {active_player} took {matches} matches instead.")

            # Fine :)
            else:
                print(f"{active_player} took {take} matches.")

        # Calculating matches
        matches -= take
        print()  # Blank space

    # Printing the name of the champion
    print(f"No more matches left. {active_player} took the last one.")
    print(f"Thus, {active_player} Won the game!")
    input("Press enter to continue...")  # Giving some time for the winner to show off against the loser
    print()  # Blank space

    # Asking if the player wants to continue playing
    print(f"{len(unlocked)} out of {len(unknowns)} secret messages observed so far.")
    print("Would you like to play again? Yes or No:")
    again = input(">>> ").lower()
    while again not in ["y", "yes", "n", "no"]:  # Checking the validity
        print("Invalid input. The input can only be Yes and No.")
        again = input(">>> ").lower()
    if again in ["n", "no"]:  # Checking the answer
        running = False
    print()  # Blank space

# Exiting the program
exit()

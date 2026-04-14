import time
import random
from valid_anagame_words import get_valid_word_list
import anagram_race as ar
from AnagramLookup import AnagramLookup

GAME_TIME_LIMIT = 60


def generate_letters() -> list:
    '''Generates a list of 7 randomly-chosen lowercase letters from the Scrabble
    distribution that includes three vowels.

      Returns:
          list: A list of 7 lowercase letters (including 3 vowels)

      Example
      -------
      >>> generate_letters()
      ["p", "o", "t", "s", "r", "i", "a"]
    '''
    scrabble_freqs = {
        "a": 9, "b": 2, "c": 2, "d": 4, "e": 12, "f": 2, "g": 3, "h": 2, "i": 9, "j": 1, "k": 1, "l": 4, "m": 2,
        "n": 6, "o": 8, "p": 2, "q": 1, "r": 6, "s": 4, "t": 6, "u": 4, "v": 2, "w": 2, "x": 1, "y": 2, "z": 1
    }

    # Build a string with the appropriate frequency of each letter
    # Ex: "aaaaaaaaabbcc..." for 9 a's, 2 b's, 2 c's, etc.
    scrabble_str = ""
    for letter in scrabble_freqs:
        scrabble_str += letter * scrabble_freqs[letter]

    # Get 7 random letters
    letters = random.sample(scrabble_str, k=7)

    # Keep regenerating the letters until you have 3 vowels
    # BEGIN SOLUTION

    # END SOLUTION

    return letters


def parse_guess(guess: str) -> tuple:
    '''Parses a guess into a unique tuple representation with the following properties:
       - cleaned to only contain lowercase a-z letters
       - sorted in alphabetical order to avoid recording duplicate guesses

        Args:
            guess (str): A single string reprsenting the player guess

        Returns:
            tuple: A tuple of two words. ("", "") in case of invalid input.

        Examples
        --------
        >>> parse_guess("ea!t, tea")
        ("eat", "tea")

        >>> parse_guess("eat , tea")
        ("eat", "tea")

        >>> parse_guess("tea,eat")
        ("eat", "tea")

        >>> parse_guess("eat tea")
        ("", "")
    '''
    # BEGIN SOLUTION

    # END SOLUTION


def play_game(time_limit: int, letters: list, lookup: AnagramLookup) -> list:
    '''Plays a single game of AnaGame

       Args:
         time_limit: Time limit in seconds
         letters: A list of valid letters from which the player can create an anagram
         lookup (AnagramLookup): helper object used to compute anagrams of letters.

       Returns:
          A list of tuples reprsenting all player guesses
   '''
    guesses = []
    quit = False

    start = time.perf_counter()  # start the stopwatch (sec)
    stop = start + time_limit

    while time.perf_counter() < stop and not quit:
        guess = input('')
        if guess.strip() == "quit":
            quit = True
        else:
            tuple_guess = parse_guess(guess)
            if len(tuple_guess[0]) == 0:
                print("Invalid input! Please enter two words separated by a comma.")
            elif tuple_guess in guesses:
                print("You've already guessed that pair - try again!")
            else:
                guesses.append(tuple_guess)

        print(f"{letters} {round(stop - time.perf_counter(), 2)} seconds left")

    return guesses


def calc_stats(guesses: list, lookup: AnagramLookup) -> dict:
    '''Aggregates several statistics into a single dictionary with the following key-value pairs:
        "valid" - list of valid guesses
        "invalid" - list of invalid guesses
        "score" - per the rules of the game
        "accuracy" -  truncated int percentage representing valid player guesses out of all player guesses
                      3 valid and 5 invalid guesses would result in an accuracy of 37 (3/8 = .375)
        "guessed" - set of unique words guessed from valid guesses
        "not guessed" - set of unique words not guessed
        "skill" - truncated int percentage representing the total number of unique anagram words guessed out of all possible unique anagram words
                  Guessing 66 out of 99 unique words would result in a skill of 66 (66/99 = .66666666)
     Args:
      guesses (list): A list of tuples representing all word pairs guesses by the user
      explorer (AnagramExplorer): helper object used to compute anagrams of letters.

     Returns:
      dict: Returns a dictionary with seven keys: "valid", "invalid", "score", "accuracy", "guessed", "not guessed", "skill"

     Example
     -------
     >>> letters = ["p", "o", "t", "s", "r", "i", "a"]
     >>> guesses = [("star","tarts"),("far","rat"),("rat","art"),("rat","art"),("art","rat")]
     >>> explorer = AnagramExplorer(get_valid_word_list())
     >>> calc_stats(guesses, letters, explorer)
     {
        "valid":[("rat","art")],
        "invalid":[("star","tarts"),("far","rat"),("rat","art"),("art","rat")],
        "score": 1,
        "accuracy": 20,
        "guessed": { "rat", "art" },
        "not_guessed": { ...73 other unique },
        "skill": 2
     }
    '''
    stats = {}
    stats["valid"] = []
    stats["invalid"] = []
    stats["score"] = 0
    stats["accuracy"] = 0
    stats["guessed"] = set()
    stats["not guessed"] = set()
    stats["skill"] = 0

    # BEGIN SOLUTION

    # END SOLUTION

    return stats


def display_stats(stats):
    '''Prints a string representation of the game results

        Args:
          score_info (dict): a dictionery of game play information
    '''

    print("\nThanks for playing Anagame!\n")
    print("------------")
    print(f"Accuracy: {round(stats['accuracy'], 2)}%")
    print(f" valid guesses ({len(stats['valid'])}):", end=" ")
    for guess in stats['valid']:
        print(f"  {guess[0]},{guess[1]}", end=" ")
    print(f"\n invalid guesses ({len(stats['invalid'])}):", end=" ")
    for guess in stats['invalid']:
        print(f"  {guess[0]},{guess[1]}", end=" ")
    print("\n------------")
    print(f"Skill: {stats['skill']}% ")
    print(f" Unique words used:", end=" ")
    for guess in sorted(stats['guessed']):
        print(f"  {guess}", end=" ")
    print(f"\n Words you could have used:", end=" ")
    for guess in sorted(stats['not guessed']):
        print(f"  {guess}", end=" ")
    print("\n------------")
    print(f"AnaGame - Final Score: {stats['score']}")
    print("------------")


if __name__ == "__main__":

    letters = generate_letters()
    lookup = AnagramLookup(get_valid_word_list(), letters)  # helper object

    print("\nWelcome to Anagame!\n")
    print("Please enter your anagram guessess separated by a comma: eat,tea")
    print("Enter 'quit' to end the game early.\n")
    print(
        f"You have {GAME_TIME_LIMIT} seconds to guess as many anagrams as possible!")
    print(f"{letters}")

    guesses = play_game(GAME_TIME_LIMIT, letters, lookup)
    stats_dict = calc_stats(guesses, lookup)
    display_stats(stats_dict)
    
import math
import random

def randomly_pick_who_goes_first(num_players:int)-> int:
  """Randomly picks who goes first to make the game more playable
        Args:
          num_players: 1 or 2 players

        Returns:
          An integer representing who goes first: 0->AI, 1->Player 1, 2->Player 2
  """
  turn = random.choice([num_players-1, num_players])  #[0, 1] or [1, 2]
  return turn

def format_pile(stones_in_pile: int) -> str:
  """Generates a pretty string version of the pile of stones

      Args:
        stones: Total number of stones in the pile

      Returns:
        A single string representing the pile of stones, where '*' indicates a single stone
            - The returned string should begin with a newline ('\n')
            - A maximum row length determined by the ceiling of the square root number of stones in the pile
            - '\n' should be used to indicate line breaks
            - The string should end with a text-based summary of the number of stones in the pile

        Examples
        --------
        >>>format_pile(1)
        "\n*\nThere is 1 stone in the pile."

        >>>format_pile(7)
        "\n***\n***\n*\nThere are 7 stones in the pile."
  """

  stones_str = "\n"
  row_length = math.ceil(stones_in_pile ** 0.5)

  stones_drawn = 0
  counter = 0 

  while counter < stones_in_pile:
        # error ahppened here in prev attempt
    for i in range(row_length):
      if counter >= stones_in_pile:
          break # ask mr harris if this break is causing issues
      stones_str += "*"
      stones_drawn += 1
      counter += 1
    stones_str += "\n"

  if stones_in_pile == 1:
    stones_str += "There is 1 stone in the pile."
  else:
    stones_str += f"There are {stones_in_pile} stones in the pile."

  return stones_str

def is_valid_move(stones_taken:int, stones_in_pile:int, valid_guesses:list) -> bool:
  """Determines whether a move is valid. A valid move must be included in valid_guesses, and cannot 
     cause a player to take the last stone.

      Args:
        stones_taken: Number of stones requested for removal
        stones_in_pile: Number of stones in the pile
        valid_guesses: A list of integers representing all valid guesses

      Returns:
        Whether the move is valid

      Examples
      --------
      >>>is_valid_move(1, 16, [1,2,3,4])
      True

      >>>is_valid_move(4, 4, [1,2,3,4])
      False
  """
  # pseudo code
  # if it is NOT IN (function is lit not in) valid guesses false
  # if it is more than or = to the sotn es its false
  # outside ocndiitonsals it is true
  if stones_taken not in valid_guesses:
        return False
  if stones_taken >= stones_in_pile:
    return False
  return True


def get_ai_guess(stones_in_pile:int, valid_guesses:list[int]) -> int:
  """Picks the perfect number of stones to eventually leave 
     the other player with 1 remaining stone

      Args:
        stones_in_pile: Total number of stones in the pile
        valid_guesses: A list of integers representing all valid guesses

      Returns:
        A valid number of stones to stones_taken from the pile.
        If possible, a perfect strategy is employed. Otherwise, the AI picks 1 to maximize room for
        the player to make a mistake.

      Examples
      --------
      >>>get_ai_guess(15, [1,2,3,4])
      4

      >>>get_ai_guess(6, [1,2,3,4])
      1
  """
  for playersguess in valid_guesses:
     if (stones_in_pile - playersguess) % 5 == 1:
        return playersguess
  return valid_guesses[0]
     

def get_player_guess(player:int, stones_in_pile:int, valid_guesses:list)->int:
  """Prompt a player to enter a guess until a valid guess has been entered

      Args:
        player: The player label: 0, 1 or 2.
        stones_in_pile: Total number of stones in the pile
        valid_guesses: A list of integers representing all possible guesses

      Returns:
        int: The number of stones to stones_taken from the pile
  """
  
  
  if player == 0:
      player_label = "The AI"
      stones_taken = get_ai_guess(stones_in_pile, valid_guesses)
  else: #player is human
    player_label= f"Player {player}" 
    stones_taken = input(f"\nPlayer {player} - How many stones would you like to remove from the pile?")
    stones_taken = int(stones_taken)

    while not is_valid_move(stones_taken, stones_in_pile, valid_guesses):
      print("Invalid input. Please make another guess.")
      stones_taken = input(F"{player}- How many stones would you like to remove from the pile?\n")
      stones_taken = int(stones_taken)

  if stones_taken > 1:
    print(F"\n{player_label} takes {stones_taken} stones.\n")
  else:
    print(F"\n{player_label} takes 1 stone.\n")
    
  
  return stones_taken
   
def play_game(num_players:int)->int:
  """Plays 1 full game of 16 Stones with either 1 or 2 players.

      Args:
        num_players (int): 1 or 2 players

      Returns:
        int- An integer representing the winner of the game: 0->AI, 1->Player 1, 2->Player 2
  """
  stones_in_pile= 16
  valid_guesses = range(1, 5)  #[1, 2, 3, 4]
  turn = randomly_pick_who_goes_first(num_players)

  while stones_in_pile > 1:
    #Display the current number of stones in the pile
    print( format_pile(stones_in_pile) )  

    #Next player takes some stones
    stones_taken = get_player_guess(turn, stones_in_pile, valid_guesses)
    stones_in_pile -= stones_taken

    #Check to see if the game is over
    if stones_in_pile == 1:
      print(format_pile(stones_in_pile))  #final display of the pile for visual confirmation of the win
      return turn
    else: #otherwise, switch players
      if turn == 1 and num_players == 1:
        turn = 0
      elif turn == 1 and num_players == 2:
        turn = 2
      else:
        turn = 1

if __name__ == "__main__":
  print("\n-----Welcome to 16 STONES-----")
  num_players = int(input("1 or 2 players?"))

  play="Yes"
  while play in ["Yes", "YES", "yes", "Y", "y", "yeah", "yup"]:
      winner = play_game(num_players)

      # 0->AI, 1->Player 1, 2->Player 2
      if winner == 0:
          print(F"AI WINS!\n")
      else:
          print(F"Player {winner}- You WIN!\n")

      play = input("Play again?")

  print("\n-----Thanks for playing 16 STONES!-----")
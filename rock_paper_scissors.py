# Rock, Paper, Scissors using the import module

# Import Random
import random

while True:

  # Welcome note
  print("\n***********************\nRock, Paper, Scissors Game Play. Use the controls to make your move;\n r = Rock, p = Paper, s = Scissors")

  # Game Controls
  game_controls = ["r", "p", "s"]

  # User Input
  user_choice = input("\nLet the game begin! Make your choice (r, p or s) ")

  # Computer Input
  robot_choice = random.choice(game_controls)
  
  # Conditional statements
  # If user and computer inputs are the same
  if user_choice == robot_choice: 
    
    # Print inputs made
    print(f"\nYou:{user_choice}, CPU:{robot_choice}")
    
    print("\nThere is a tie!")

    game_reset = input("Try again, you might be lucky this time! 'y' or 'n': ")

    if game_reset == "y":
            print("\nLet's begin!")

    else:
        print("\nGame Over!")

  #if user input rock
  elif user_choice == "r":
    
    # Print inputs made
    print(f"\nYou:{user_choice}, CPU:{robot_choice}")
    
    if robot_choice == "s":
      print("\nYou won! Rock crushes Scissors!")
    else:
      print("\nYou lost! Paper covers Rock!")

    break

  #if user input paper
  elif user_choice == "p":
    
    # Print inputs made
    print(f"\nYou:{user_choice}, CPU:{robot_choice}")
    
    if robot_choice == "s":
      print("\nYou lost! Scissors cuts Paper!")
    else:
      print("\nYou won! Paper covers Rock!")

    break

  #if user input scissors
  elif user_choice == "s":
    
    # Print inputs made
    print(f"\nYou:{user_choice}, CPU:{robot_choice}")
    
    if robot_choice == "r":
      print("\nYou lost! Rock crushes Scissors!")
    else:
      print("\nYou won! Scissors cuts Paper!")

    break  
  
  else:
    print("\nInvalid game control was used, try again!")
def treasure_island():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    choice1 = input("left or right? ").strip().lower()
    if choice1 != "left":
        print("Fall into a hole. Game Over.")
        return

    choice2 = input("swim or wait? ").strip().lower()
    if choice2 != "wait":
        print("Attacked by trout. Game Over.")
        return

    choice3 = input("Which door? Red, Blue, or Yellow: ").strip().lower()
    if choice3 == "red":
        print("Burned by fire. Game Over.")
    elif choice3 == "blue":
        print("Eaten by beasts. Game Over.")
    elif choice3 == "yellow":
        print("You Win!")
    else:
        print("Game Over.")

# Start the game
treasure_island()
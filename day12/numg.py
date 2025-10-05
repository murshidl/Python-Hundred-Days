import random

def pagain():
    print("welcome to this game")
    print("The computer will pick a random number between 1 and 100.")
    print("""Player needs to guess the number.
      1.Easy Mode:10 Guesses
      2.Hard Mode:5 Guesses
      """)



    gnum = int(random.randint(1,100))
    print(gnum)


    difficulty = input("1.Easy|2.Hard\n").lower()

    def set_difficulty():
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid input! Defaulting to 'easy'.")
            return 10

    attempts = set_difficulty()


    def feedback(guess, answer):
        if guess > answer:
            print("Too high!")
            return False
        elif guess < answer:
            print("Too low!")
            return False
        else:
            print(f"🎉 You got it! The answer was {answer}.")
            return True
        

    game_over = False

    while not game_over and attempts > 0:
        print(f"\n you have {attempts} attempts remaining.")
        guess = int(input("Make a guess:"))
        if guess <=0:
            print("You have ended the game")
            break

        correct = feedback(guess,gnum)

        if correct:
            game_over = True
        
        else:
            attempts -=1
            if attempts == 0:
                print(f"😢 You've run out of guesses. You lose! The correct number was {gnum}.")


pagain()

again = input("do you wanna play again..?")


if again == "yes" :
    pagain()
else:
    print("Your Game has ended")






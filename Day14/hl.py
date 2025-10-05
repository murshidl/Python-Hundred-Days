"""
Display the game logo (art).

Create a dictionary/list of data for accounts.

Format account data into a printable format.

Generate a random account (character).

Assign the account as A or B.

Compare follower counts between the two accounts.

Ask the user for their guess (who has more).

Check if the guess is correct.

Keep score and display it.

Continue game with the winner as account A, generate new account B.

End game when guess is wrong and display final score.
"""
import ascii
from randc import data
import random

print(ascii.art)



score = 0
while True:
    Aa = random.choice(data)
    print(f"Compare A: {Aa['name']}, {Aa['description']}, {Aa['country']}")

    print(ascii.vs)
    
    Bb = random.choice(data)
    print(f"Against B: {Bb['name']}, {Bb['description']}, {Bb['country']}")



    mychoice = input("Enter your Choice A or B\n").upper()

    print("COMPARING THE VALUES........!!!!")






    def compare(mychoice):
        
        A = Aa['follower_count']
        B = Bb['follower_count']
        
        if A == B:
            print(f"{Aa['name']} and {Bb['name']} have the same number of followers: {A}")
            return 'Tie'
        
        if mychoice == 'A':
            if A > B:
                print(f"Correct! {Aa['name']} has more followers: {A}")
                return 'Correct'
                
                
            else:
                print(f"Wrong! {Bb['name']} has more followers: {B}")
                return 'Wrong'
        elif mychoice == 'B':
            if B > A:
                print(f"Correct! {Bb['name']} has more followers: {B}")
                return 'Correct'
            else:
                print(f"Wrong! {Aa['name']} has more followers: {A}")
                return 'Wrong'
        else:
            print("Invalid choice! Enter A or B only.")
            return 'Invalid'

                    
    result = compare(mychoice)



    if result =='Correct':
        score += 1
        print(f"your score is {score}")
        Aa = Aa if Aa['follower_count'] > Bb['follower_count'] else Bb

    elif result =="Wrong":
        print(f"your score is {score}")
        break

    elif result == 'Tie':
        print("It's a tie! Try again.")
    else:
        print("Invalid choice! Enter A or B only.")


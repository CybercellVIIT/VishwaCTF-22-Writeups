import random

_000x80085 = [152, 230, 147, 140, 158, 146, 128, 149, 211, 203, 225, 177, 167, 228, 121]
def _000xf69106(a):
    c=[]
  
    c.append(a[-1])
    for i in range(len(a)-1,-1,-1):
        # b = a[i]
        a[i-1] = a[i-1] - a[i]
        
        c.append(a[i-1])
        
    
    for i in range(len(a)-1,-1,-1):
        print(chr(c[i]), end='')
    


target_amount = 100000
user_account = 500

print("\nHOW TO PLAY\n")
print("1. You are given 500 coins")
print("2. You need to place your bet")
print("3. Next you have to guess a number between 0 to 9")
print("4. You have 5 chances to guess the correct number")
print("5. For a correct guess you'll win the bet amount")
print("6. 5 consecutive incorrect guesses will result in deduction of bet amount from your account")
print("7. To buy the flag you need to win 100000 coins")
print("BEST OF LUCK!! (if you find it difficult to get the flag, take help from the Sage)\n")



while(True):
    print("\nPress 1 to Play\nPress 2 to buy the flag\nPress 3 to exit")

    user_choice = int(input())
    
    if(user_choice == 1):
        random_value = random.randint(0,9)
        # random_value = 5

        user_bet = int(input("Place your bet: "))
        if(user_account == 0):
            print("Sorry you've lost all your money")
            break

        if(user_bet > user_account):
            print("You don't have enough money for the bet!!")


        else:
            for i in range(5):
                user_guess = int(input("Enter your Guess: "))
                if(user_guess == random_value):
                    user_account = user_account + user_bet
                    print("You win this bet!!")
                    print("Account balance = ", user_account)
                    break
                else:
                    print("Wrong guess")

            else:
                print("You have lost your bet. Random number was: ",random_value," Try again")
                user_account = user_account - user_bet
                print("Account balance = ", user_account)

        
    
    
    elif(user_choice == 2):
        print("Your account balance = ", user_account)
        print("Flag price = ", target_amount)
        if(user_account >= target_amount):
            print("🎉🎉🎉")
            _000xf69106(_000x80085)
            print("\n🎉🎉🎉")

            break
        else:
            print("You do not have enough money")
        
    elif(user_choice == 3):
        break
    
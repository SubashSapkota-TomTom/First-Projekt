import random
num = random.randrange(0,25)

player_name = input("Please tell us your name to continue: ")
print(f"Hello {player_name} , Welcome to Guessing number game. I haved gussed a number between 0 and 25, Now it's your Turn !!  ") 



num_of_guess = 0

while num_of_guess < 5:
    guess = int(input("Enter a number: "))
    
    if type(guess) == int:
        try:

            num_of_guess += 1

            if guess < num:
                print("Your guess is too Small. Try Again!!")
        

            elif guess > num:
                print("Your guess is too Big. Try Again!!")
        

            else:
                print(f"You guess the Right in {num_of_guess} tries. You Won, Thank you {player_name} for Playing with us!! ")
                break
        except:
            print("Invalid input, try again")     


else:
    print(f"You didn't guess the right number. You Loss the game, Thank you {player_name} for Playing with us!! ")
import random

def play_game():
    snum=random.randint(1,100)

    attempts=0
    print("\n*****NUMBER GUESSING GAME*****")
    print("I haved done selecting a number between 1 and 100")
    print("Try to guess!!!")

    while True:
        try:
            guess=int(input("Enter your guess:"))
            attempts+=1

            if guess<snum:
                print("Too Low!Try again!!")
            elif guess>snum:
                print("Too High!Try again!!")
            else:
                print("Congratulations!You guessed the number right.")
                print(f"Number of attempts:{attempts}")
                break
        except ValueError:
            print("Please enter a valid number.")

#main program
def main():
    while True:
        play_game()

        choice=input("\nDo you want to play again?(yes/no):").lower()

        if choice!="yes":
            print("Thanks for playing!")
            break

main()


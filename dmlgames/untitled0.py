import random

def main():
    difficulty = input("Enter a difficulty level: 'easy','medium', or 'hard' : ")
    
    print("At any time, type 'hint' to get a hint")
    if difficulty == "easy":
        randomNumber = random.randint(1,100)
    
    elif difficulty == "medium":
        randomNumber = random.randint(1,10000)
    
    elif difficulty == "hard":
        randomNumber = random.randint(1,1000000)
    
    return randomNumber
    
randomNumber = main()
found = False

while not found:
    if difficulty == "easy":
        guess = int(input("Guess a number between 1 and 100"))

        if guess > randomNumber:
            print("Too high")
        elif guess == randomNumber:
            print("Thats correct!!")
            found = True
        else :
            print("Too Low")
                

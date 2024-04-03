import random
count=0
print("Welcome to our guessing game")
upper_limit=input("Please enter the upper limit: ")
lower_limit=input("Please enter lower limit: ")
while True:
    if float(upper_limit) - float(lower_limit) < 10:
        print("Low limit please enter again: ")
        upper_limit = input("Please enter the upper limit: ")
        lower_limit = input("Please enter lower limit: ")
    else:
        break
random_number=random.randint(int(lower_limit) , int(upper_limit))
answer=int(input("Please enter your guess: "))
while answer!=random_number:
    if answer<random_number:
        print("Too low, try again")
        answer = int(input("Please enter your guess: "))
        count+=1
    elif answer >random_number:
        print("Too high, try again")
        answer = int(input("Please enter your guess: "))
        count+=1
print("Congratulations,you guessed the number in:"+str(count)+"times")



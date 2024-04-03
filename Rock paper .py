import random
# 1=rock
# 2=paper
# 3=scissors

def proccessing(answer):
    computer_choice=int(random.randint(1,3))
    if answer== 1 and computer_choice==2:
        print("You lost")
        print("The computer chose: "+str(computer_choice))
    elif answer== 1 and computer_choice==3:
        print("You won")
        print("The computer chose: " + str(computer_choice))
    elif answer == 2 and computer_choice == 1:
        print("You won")
        print("The computer chose: " + str(computer_choice))
    elif answer== 2 and computer_choice==3:
        print("You lost")
        print("The computer chose: " + str(computer_choice))
    elif answer== 3 and computer_choice == 1 :
        print("You lost")
        print("The computer chose: " + str(computer_choice))
    elif answer == 3 and computer_choice ==2:
        print("You won")
        print("The computer chose: " + str(computer_choice))
    else:
        print("Wrong input")


count=0
print("Welcome to the Rock Paper Scissors game")
while True:
    answer = int(input("Please enter your answer: "))
    if answer not in [1, 2, 3]:
        print("Wrong input. Please enter a number between 1 and 3.")
        continue
    proccessing(answer)
    count+=1
    again = int(input("Do you want to play again(1 if yes, 0 if no): "))
    if again == 1:
        continue
    elif again == 0:
        print("You played " ,count ," times")
        break
    else:
        print("Wrong input")
        again = int(input("Do you want to play again(1 if yes, 0 if no): "))




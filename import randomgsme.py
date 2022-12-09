import random

score  = [0]
checker = 1


def game(counter):
    x = random.randint(1,6)
    print("Enter the number : ")
    n = int(input()) #User input
    if x == n:
        print("You entered the right number ✅")
        counter[0] += 1
    else:
        print("You entered the wrong number ❌")
        counter[0] = 0
    print ("Score : ",counter[0])

while(checker):
    game(score)
    print("Press 1 to play again : ")
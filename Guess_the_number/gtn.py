from random import randint

start = 1
end = 1000
value = randint(start,end)

print("The computer chose a no between ",start," and ",end)

guess = None

while guess!=value:
    a = input("guess the no ")
    guess = int(a)

    if guess>value:
        print("No is Lower")
    elif guess<value:
        print("No is higher")

print("Congratulations You won!!")
import random


number = random.randint(1,100)

min = 1
max = 100

times = 1
guess = 1
flag = False


while not(flag):
    try:
        guess = int(input(f"guess a number({min} - {max}): "))
    except ValueError:
        print("Enter an integer!")
        continue

    if guess > max or guess < min:
        print(f"You are not in range {min} - {max}")
        continue

    if guess > number:
        times += 1
        max = guess
    elif guess < number:
        times += 1
        min = guess
    else:
        flag = True
        print(f"The secret is {number}. You guess it in {times} times")    
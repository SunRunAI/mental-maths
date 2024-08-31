import random


def addition():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    print(f"{num1} + {num2} = ")
    input()
    print(f"Answer: {num1 + num2}\n")

def subtraction():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    if num1 < num2:
       num1, num2 = num2, num1
    print(f"{num1} - {num2} = ")
    input()
    print(f"Answer: {num1 - num2}\n")

def multiplication():
    num1 = random.randint(1, 99)
    num2 = random.randint(1, 99)
    print(f"{num1} * {num2} = ")
    input()
    print(f"Answer: {num1 * num2}\n")

def division():
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 13)
    if num1 < num2:
       num1, num2 = num2, num1
    print(f"{num1} / {num2} = \nTest for divisibility first!!!")
    input()
    print(f"Answer: {num1 / num2}\n")

def square():
    num1 = random.randint(1, 999)
    print(f"{num1}**2 = ")
    input()
    print(f"Answer: {num1**2}\n")

def square_root_even():
    num1 = random.randint(1, 99)
    print(f"{num1**2}**1/2 =  (Even)")
    input()
    print(f"Answer: {num1}\n")

def square_root():
    num1 = random.randint(1, 9999)
    print(f"{num1}**1/2 =  (Uneven)")
    input()
    print(f"Answer: {num1**0.5}\n")

def cube():
    num1 = random.randint(1, 99)
    print(f"{num1}^3 = ")
    input()
    print(f"Answer: {num1 ** 3}\n")

def percentage():
    num1 = random.randint(1, 9999)
    num2 = random.randint(1, 99)
    print(f"{num2}% of {num1} =")
    input()
    print(f"Answer: {num1 * (num2/100)}\n")


def main(problems, n_probs):
    for _ in range(n_probs):
        for prob in problems:
            prob()


if __name__ == "__main__":
    problems = [
        addition,
        subtraction,
        multiplication,
        division,
        square,
        square_root_even,
        square_root,
        cube,
        percentage,
    ]
    print("Run each question once mentally, then double check on pen and paper for hard problems.")
    main(problems, n_probs=5)


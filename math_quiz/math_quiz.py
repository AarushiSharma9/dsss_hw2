import random


def random_int(min, max):
    """
    Generates a random integer from the min, max range.
    """
    return random.randint(min, max)


def random_op(): # chooses a random airthmetic operator
    return random.choice(['+', '-', '*'])


def problem(n1, n2, o): #generate a math problem with n1: number 1; n2: number 2 & o: operator ('+', '-', '*').
    p = f"{n1} {o} {n2}" #the math problem
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a #p: problem ; a: answer

def math_quiz():
    score = 0
    total_ques = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_ques):
        n1 = random_int(1, 10); n2 = random_int(1, 5); o = random_op()

        p, ANSWER = problem(n1, n2, o)
        print(f"\nQuestion: {p}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_ques}")

if __name__ == "__main__":
    math_quiz()

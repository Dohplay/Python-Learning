"""
Version 1 of a math quiz program.
Adapted from a programming problem by Jeff Elkner.

dlb Dept. of Systems and Computer Engineering, Carleton U.
Initial release: Oct 12, 2007 (SYSC 1100)
Revised: October 28, 2011 (SYSC 1005)
Revised: October 21, 2014 (SYSC 1005 - updated for Python 3.x)
"""

import random

def ask_questions():
    """
    Ask 10 addition problems with random integer operands between 1 and 10.
    Return the number of questions that were answered correctly.
    """
    
    ok = 0      # Number of correct answers so far
    for question in range(10):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        correct_result = num1 + num2

        prompt = ("Question " + str(question + 1) + ". What's " +
                  str(num1) + " plus " + str(num2) + "? ")

        answer = int(input(prompt))
        if answer == correct_result:
            print("That's right -- well done.")
            ok += 1
        else:
            print("No, I'm afraid the answer is", correct_result)

    return ok

if __name__ == "__main__":
    correct = ask_questions()
    print("I asked you 10 questions.", end = " ")
    print("You got", correct, "of them right.")

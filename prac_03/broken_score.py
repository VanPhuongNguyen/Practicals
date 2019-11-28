"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

from random import randint

# TODO: Fix this!
def main():     
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)

    # Random
    randon_score = randint(0, 100)
    result = check_score(randon_score)
    print('Your score is {} with the result: {}'.format(randon_score, result))


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score >= 90:
            return 'Excellent'
        elif score in range (50, 90):
            return 'Pass'
        else:
            return 'Bad'


main()
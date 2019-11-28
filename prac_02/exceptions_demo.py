"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
- When the input is not int type
2. When will a ZeroDivisionError occur?
- When the denominator equals to 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print('Your denominator must not be 0!')
        exit()
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


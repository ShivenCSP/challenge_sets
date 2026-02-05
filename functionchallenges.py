# challeges on function in python

# Challenge 1
"""
Psuedocode
PROCEDURE add(a, b)
{
DISPLAY(a + b)
}
PROCEDURE subtract(a, b)
{
DISPLAY(a - b)
}
PROCEDURE multiply(a, b)
{
DISPLAY(a * b)
}
PROCEDURE divide(a, b)
{
DISPLAY(a / b)
}
add(34, 17)
subtract(72, 24)
multiply(13, 3)
divide(27, 9)
"""

# def add(a, b):
#     print(a + b)

# def subtract(a, b):
#     print(a - b)

# def multiply(a, b):
#     print(a * b)

# def divide(a, b):
#     print(a / b)

# add(34, 17)
# subtract(72, 24)
# multiply(13, 3)
# divide(27, 9)

# # Challenge 2
# """
# Psuedocode
# PROCEDURE average(a, b, c)
# {
# return (a + b + c)/3
# }
# num1 <-- input("Enter the first number: ")
# num2 <-- input("Enter the second number: ")
# num3 <--input("Enter the third number: ")
# result <-- average(num1, num2, num3)
# DISPLAY(result)
# """
# def average(a, b, c):

#     return(a + b + c) / 3

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# result = average(num1, num2, num3)

# print(result)

# challenge 3

"""
Psuedocode
PROCEDURE Is_Even(a)
{
    IF(a%2 = 0)
    {
    Return (That's even)
    }
    ELSE
    {
    Return (That's odd)
    }
}
num <-- INPUT(Is_Even(a))

print(num)
"""

# def Is_Even(a):

#     if a%2 == 0:
#         return "That's even"
#     elif a%2 > 0:
#         return "That's odd"

    
# num1 = int(input("Number?"))
# result = Is_Even(num1)

# print(result)

# Challenge 3

"""
Psuedocode
Already in the challenges as clue
"""

def analyze_word(word):

    vowelCount = 0
    consanentCount = 0

    Vowels = "aeiou"

    for i in range(len(word)):
        if word[i] in Vowels:
            vowelCount += 1
        else:
            consanentCount += 1
    return f"Contains {vowelCount} vowels and {consanentCount} consanents"

word1 = str(input("random word in all lowercases:"))
result = f"here {analyze_word(word1)}"

print(result)


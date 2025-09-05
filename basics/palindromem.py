"""
Palindrome Challenge Rules:
---------------------------
- A palindrome is a word, phrase, number, or sequence that reads the same
  forwards and backwards.
- Write a function that:
  1. Takes in a string from the user.
  2. Ignores spaces, capitalization, and punctuation.
  3. Checks if the cleaned string is a palindrome.
  4. Prints whether it is a palindrome or not.
"""


def isPalendrome(str):
    stringToList = str.split("")
    print(stringToList)

isPalendrome('hello')
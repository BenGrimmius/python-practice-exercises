"""
FizzBuzz Rules:
---------------
- Print numbers from 1 to 100
- If the number is divisible by 3 → print "Fizz"
- If the number is divisible by 5 → print "Buzz"
- If the number is divisible by both 3 and 5 → print "FizzBuzz"
"""


for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)

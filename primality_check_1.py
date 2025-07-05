# Program specification
"""
Test is an int > 2 is prime. If not, print the largest divisor.
"""

number = int(input("Enter an integer greater than 2: "))

largest_divisor = 1
for guess in range(2, number):
    if number % guess == 0:
        if guess > largest_divisor:
            largest_divisor = guess

if largest_divisor != 1:
    print("Largest divisor of", number, "is", largest_divisor)
else:
    print(number, "is a prime number")

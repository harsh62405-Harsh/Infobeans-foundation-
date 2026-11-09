# Q4. Prime Numbers in a Range — Nested Loops
# Write a Python program that accepts two numbers start and end and prints all prime numbers between them.
# Also display the total number of prime numbers found.
# Example:
# Enter start: 10
# Enter end: 30
# Prime numbers:
# 11 13 17 19 23 29
# Total prime numbers: 6

n1 = int(input("enter the first Starting number -:"))
n2 = int(input("Enter the ending number -:"))
prime_no_count = 0

for num in range(n1 , n2 + 1):
    if num > 1:
        for i in range(2 , num):
            if (num % i == 0):
                break
        else:
            print(num, end=" ")
            prime_no_count += 1

print(f"\nTotal prime numbers: {prime_no_count}")
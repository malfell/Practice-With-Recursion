# Write code for algorithm 1 below
# Write a program that takes a positive number as an argument 
# and prints the numbers from n to zero.

def to_zero(num):
    # Base
    if num == 0:
        return
    # Recursive
    else:
        print(num)
        to_zero(num - 1)

to_zero(6)
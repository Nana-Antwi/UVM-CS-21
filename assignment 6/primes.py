#Nana Antwi
#CS 021
#Assignment 6
#primes.py

#Design a program that tells if a number is prime or not.


#prime number list function
import math
def main():
    for num in range(1,101):
        if is_prime(num) == True:
            print(num, end=" ")

#function for determining prime numbers
def is_prime (num):

#condition loop statments
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    if num % 2 == 0 and num > 2:
        return False
    else:
        return True

#recall function
main ()
        

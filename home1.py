#Nana Antwi
#CS 021
#Assignment 6
#primes.py

#Design a program that tells if a number is prime or not.

#variables
num = int(input('Enter a number: '))

#function
import math
def is_prime (num):


#condition loop statments
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            print('Your number given is prime')
    if num % 2 == 0 and num > 2:
        print('Your number given is not prime')
    else:
        print('Your number given is prime')

#recall function
is_prime (num)
        

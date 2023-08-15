#!/usr/bin/env python3

def happy_new_year():
    for i in range(11):
        print(i)
        print("Happy New Year!")

def square_integers(int_list):
    squared_list = [i ** 2 for i in int_list]
    return squared_list
        
def fizzbuzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
            
            

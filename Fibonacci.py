#!/usr/bin/env -S  python  #
# -*- coding: utf-8 -*-
#====================================================================================================
# LICENCE INFORMATION
#====================================================================================================
# Samuel Louviot, PhD 
#
# MIT License
#
# Copyright (c) 2023 Samuel Louviot
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#====================================================================================================
# PROGRAM DESCRIPTION
#====================================================================================================
"""
This program is a simple implementation of the Fibonacci sequence.
It can be used to find the nth Fibonacci number or the closest Fibonacci number to a given number.
The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers,
starting with 0, and 1.

You can either run the program from the command line or import it as a module.
To run the program from the command line, simply type the following command in the terminal:
    python Fibonacci.py
And follow the instructions.
The program will give the mean elapsed time for each function when running it 10000 times.

This code respect the PEP8 style guide for Python code.
"""
#====================================================================================================
# STANDARD LIBRARIES IMPORT
#====================================================================================================
import math
import time
from os import name, system
import tracemalloc

#====================================================================================================
# IMPORT CUSTOM MODULES AND PACKAGES WITH INSTALLATION INSTRUCTIONS
#====================================================================================================
import numpy as np # pip install numpy or conda install numpy

#====================================================================================================
# FUNCTIONS DEFINITIONS
#====================================================================================================
# Define a function to clear the terminal prompt as a function of the OS
def clear():
    """ Clears the terminal screen. 
    
    Generally when a lot of informations is displayed on the terminal
    and when user input is required, the user can be confused and the 
    task can be a little bit more cognitively demanding.
    To avoid clutter and confusion it is necessary to clean the prompt
    for each required user input. This make easier for people to follows instructions.
    The command instruction depend on the OS. So it is important 
    to check the OS before running the command by using the os.name module.
    """
 
    # If code is running on Windows
    if name == 'nt':
        _ = system('cls')
 
    # If code is running on Mac or Linux
    else:
        _ = system('clear')
        
def get_fibonacci(n):
    """ Generates the nth fibonacci number.
    
    Mathematically the Fibnacci sequence 
    is expressed using the Euler-Binet formula:
    
    F(n) = (a^n - (-b)^n) / (a - (-b))
    
    Where n is the rank of the desired Fibonacci number 
    (in other term the n-th term in the sequence, for example the 100th term in our case). 
    a is called the golden ratio where:
    
    a = (1+5^0.5)/2
    
    and b is the negative inverse of a.

    Args:
        n (int or list): The rank of the desired Fibonacci number to generate.
                         It can be a single integer or a list of integers.

    Returns:
        The Fibonacci number at the rank n (int or list).
    """

    a = (1 + 5 ** 0.5) / 2 # golden ratio
    b = 1 - a # conjugate of a

    if isinstance(n, int):
        F = int(((a ** n) - (b ** n))/(5**0.5)) # Euler-Binet formula

    elif isinstance(n, list):
        F = []
        for i in n:
            F.append(int(((a ** i) - (b ** i))/(5**0.5)))

    return F

def find_n(a):
    """ Finds the closest Fibonacci number to a given number and its lower and upper Fibonacci numbers.
    
    First we need to find the rank of the closest Fibonacci number to a. Of course it will not be an integer.
    Based on the Euler-Binet formula, we can find the rank of the closest Fibonacci number to a by using the
    logarithmic function. Secondly, knowing n we can then round the result to get the rank 
    of the closest Fibonacci number to a.
    

    Args:
        a (int): The number to find the closest Fibonacci number to.

    Returns:
        F (int): The closest Fibonacci number to a.
        upper (int): The neighboring Fibonacci number immediately higher than F.
        lower (int): The neighboring Fibonacci number immediately lower than F.
    """
    
    n = (math.log(a*(5**0.5))/math.log((1+5**0.5)/2))
    F = get_fibonacci(round(n))

    if round(n) < n:
        upper = get_fibonacci(round(n)+1)
        lower = F

    else:
        upper = F
        lower = get_fibonacci(round(n)-1)

    return F, upper, lower

#====================================================================================================
# MAIN PROGRAM
#====================================================================================================

def main():
    a = ""

    # Loop to make sure the user enters a valid input (either 1 or 2)
    while a not in ['1', '2', '3']:
        clear()
        a = input('Enter a function you want to run\n    Enter 1 for finding the nth Fibnacci number\n    Enter 2 for finding the closest Fibonacci number\n')

        #____________________________________________________________________________________________________
        # OPTION 1: Find the nth Fibonacci number
        #____________________________________________________________________________________________________
        # If the user enters 1, the program will find the nth Fibonacci number
        if a == '1':
            clear()
            n = input('Enter the rank(s) you want to find the Fibonacci number(s) for. If you are looking for several ranks enter each one separated by a coma: ')
            
            # Formatting the input to transform into a list of integers
            n = n.split(',')
            n = [int(i) for i in n]
            
            # Run the function through the speed test
            times = []

            for i in range(10000):
                start = time.time()
                get_fibonacci(n)
                end = time.time()
                times.append(end - start)
            

            # Run the function again for memory test and to get the results
            tracemalloc.start()
            Fs = get_fibonacci(n)
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('traceback')
            
            # Print the result of the speed test and memory test
            print(f"\n================================================================")
            print(f"ELAPSED TIME:\nMEAN:{np.mean(times)} +/- {np.std(times)} SECONDS")
            print(f"MAX MEMORY USAGE:\n{top_stats[-1]}")
            print(f"================================================================\n")
            
            # Formating the output of the function for display to the terminal
            # and dealing with the english language exceptions (st,nd,rd)
            if len(n) > 1:
                n.insert(-1, 'and')
                Fs.insert(-1, 'and')
                numbers = ' '.join([str(i) for i in n])
                Fs = ' '.join([str(i) for i in Fs])
                conjunction = 'are'

                if (n[-1] - 1) % 10 == 0:
                    th = 'st'
                elif (n[-1] - 2) % 10 == 0:
                    th = 'nd'
                elif (n[-1] - 3) % 10 == 0:
                    th = 'rd'
                else:
                    th = 'th'
            
            else:
                numbers = n[0]
                Fs = Fs[0]
                conjunction = 'is'

                if numbers == 1:
                    th = 'st'
                elif numbers == 2:
                    th = 'nd'
                elif numbers == 3:
                    th = 'rd'
                else:
                    th = 'th'
            
            # Printing the results to the terminal
            print(f"The {numbers}{th} Fibonacci numbers {conjunction} {Fs}.")
        
        #____________________________________________________________________________________________________
        # OPTION 2: Find the closest Fibonacci number to a given number
        #____________________________________________________________________________________________________
        # If the user enters 2, the program will find the closest Fibonacci number to a given number
        elif a == '2':
            clear()
            n = int(input('Enter the number you want to find the closest Fibonacci number to: '))

            # Runnin the function through the speed test
            times = []
            for i in range(10000):
                start = time.time()

                F, lower,upper = find_n(n)
                end = time.time()
                times.append(end - start)
            
            # Runing the function again for memory test and getting the results
            tracemalloc.start()
            F, lower,upper = find_n(n)
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')

            # Print the result of the speed test
            print(f"\n================================================================")
            print(f"ELAPSED TIME:\nMEAN:{np.mean(times)} +/- {np.std(times)} SECONDS")
            print(f"MAX MEMORY USAGE:\n{top_stats[-1]}")
            print(f"================================================================\n")
            
            # Print the results of the function
            if n == lower or n == upper:
                print(f'{n} is a Fibonacci number\n')

            else:
                print(f'The closest number to {n} in the Fibonacci sequence is {F}.')
                print(f'The Fibonacci number immediately lower than {n} is {upper}.')
                print(f'The Fibonacci number immediately higher than {n} is {lower}.\n')
        
        #____________________________________________________________________________________________________
        # ERROR CASE: Invalid input from the user
        #____________________________________________________________________________________________________
        # Anticipate the user entering an invalid input
        else:
            clear()
            print('Invalid input. Needs to be either 1 or 2. Please try again.')
            time.sleep(3)

# This is the standard boilerplate that calls the main() function when calling this script from the command line.
if __name__ == '__main__':
    main()
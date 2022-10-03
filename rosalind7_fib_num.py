'''

Author: Jeremy Muriungi
CS 473-1 Algorithms
Dr. Kent Jones

Rosalind7 Fibonacci Numbers:
https://rosalind.info/problems/fibo/

Resources used:
https://www.cs.usfca.edu/~galles/visualization/DPFib.html
https://www.geeksforgeeks.org/python-lists/

Last Modified 09/16/2022

'''
# open file with dataset
f = open('rosalind_fibo.txt', 'r')
# save number of Fibonacci numbers to show in variable
n = f.readline()
n = int(n)          # convert from string to int
if(n == 0): print('0')
else:
    fib_list = []
    fib_list.append(0)
    fib_list.append(1)
    for i in range(2, 28):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list[4])

#Day_2:

"""
2.Ask the user to input a single digit integer to a variable 'n'. 
Then, print out all of the even numbers from 0 to n (including n).

"""

n = int(input("Please enter a single-digit integer: "))

numbers = range(n+1)
evens=list(filter(lambda i:i%2==0, numbers))
print(evens)



if n>9:
    raise Exception ("Single-digit!")
elif n<0:
    raise Exception ("Positive integer!")
    

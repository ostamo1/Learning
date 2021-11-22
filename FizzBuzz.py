#!/bin/python3
#still need to find out if this is the correct way to iterate from 1 to a number in python
def fizzbuzz(limit):
  list=[]
  for (x) in range(1,limit+1) :
    if((x % 3)== 0 and (x% 5)== 0):
      list.append('FizzBuzz')
    elif ((x) % 3) == 0 :
      list.append('Fizz') # Write your code here
    elif ((x) % 5)== 0 :
      list.append('Buzz')
    else :
      list.append(x) 
  print (list)
  
print(fizzbuzz(16))
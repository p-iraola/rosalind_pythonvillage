'''
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
'''

def sum_odd(a,b):
  x = 0
  for i in range(a,b+1):
    if i % 2 != 0:
      x += i

  return(x)


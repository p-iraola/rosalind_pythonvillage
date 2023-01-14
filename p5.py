'''
Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. 
Words are case-sensitive, and the lines in the output can be in any order.
'''
def num_occurences(string):
  words = string.split()
  count = dict()

  for word in words:
    if word in count:
      count[word] += 1
    else:
      count[word] = 1

  for key, value in count.items():
    print(f'{str(key)} {str(value)}')

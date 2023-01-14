'''
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices
a through b and c through d(with space in between), inclusively. 
In other words, we should include elements s[b] and s[d] in our slice.
'''


def string_slicer(my_string, a, b, c, d):
  return f'{my_string[a:b+1]} {my_string[c:d+1]}'

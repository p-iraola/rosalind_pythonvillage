'''
Given: Two positive integers a and b, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse
of the right triangle whose legs have lengths a and b.
'''


def hypotenuse_squared(a,b):
  a = a * a
  b = b * b
  c = a + b
  return c

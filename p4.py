'''
Given: A file containing at most 1000 lines.

Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''

with open('rosalind_ini5.txt', 'r') as f:
	data = f.readlines()

for i in range(1,len(data),2):
	print(data[i])
	

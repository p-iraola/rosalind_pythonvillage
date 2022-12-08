'''
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
'''

x = 0
for i in range(4932,8978):
	if i % 2 != 0:
		x = i + x

print(x)



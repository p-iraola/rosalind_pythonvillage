'''
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices
a through b and c through d(with space in between), inclusively. 
In other words, we should include elements s[b] and s[d] in our slice.
'''


string = 'YLobdshTCkBradyporuslckgeNkNoTmmhPn3uHpZ3vBZpcVzbqgJcusFeM4yLeqPBKCo3EmaihensishxtrHcL2Mv4n0vC7W8kVdFf24613TrdXscdGh209gPWO5l0Bhm3zcGaDTfHDEcJBLh72ph1ATXXF1vba8DGA7vH.'
ints = '10 19 70 78'

print(string[10:20] + ' ' + string[70:79])

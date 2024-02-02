import sys
string = sys.stdin.readline()

small = 'qwertyuiopasdfghjklzxcvbnm'
big = small.upper()
big_list ,small_list = sorted(big) , sorted(small)
len(big_list)

output = ''
for i in range(len(string)):
    if string[i] in small_list:
        idx = small_list.index(string[i])
        output += small_list[(idx+13)%26]
    
    elif string[i] in big_list:
        idx = big_list.index(string[i])
        output += big_list[(idx+13)%26]
    else:
        output += string[i]

print(output)

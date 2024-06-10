#1 : 1  : 1
#2 : 1 +1 ,2  :2
#3 : 1+1+1, 2+1, 1+2 : 3
#4 : 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2 : 5

# 주어진 수를 1, 2로 더해서 만드는 경우의 수
# n-2를 n으로 만드는 경우의 수 : n-2 + 2
# n-1을 n으로 만드는 경우의 수 : n-1 +1 

import sys

n = int(sys.stdin.readline())

dp = [0] * (n+1)
for i in range(1,n+1):
    if i == 1:
        dp[1] = 1
    elif i == 2:
        dp[2] = 2
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)


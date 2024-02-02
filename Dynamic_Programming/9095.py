import sys

# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

# 1
# 점화식으로 생각할 수 있음

# 2
# n을 만들기 위한 경우의 수는 아래와 같음.
# 정수 n-3 에 3을 더하기 : 경우의 수는 dp[n-3]
# 정수 n-2 에 2를 더하기 : 경우의 수는 dp[n-2]
# 정수 n-1 에 1를 더하기 : 경우의 수는 dp[n-1]
# dp[n] = dp[n-1] + dp[n-2] + dp[n-3]

input = sys.stdin.readline # 주어지는 값이 한줄로 이루어짐
T = int(input()) # 첫번쨰 등장 값은 테스트 케이스의 수

for j in range(T):
    n = int(input()) #다음부터 테스트케이스 수 만큼 주어지는 값들은 더할 값
    dp = [0] * (n+1) # 주어진 n +1 의 길이로 이루어진 리스트 생성, 초기 값 0
    for i in range(1,n+1):
        if i == 1:
            dp[1] = 1
        elif i == 2 :
            dp[2] = 2 # 1+1, 2
        elif i == 3:
            dp[3] = 4 # 1+1+1, 2+1, 1+2, 3
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])


        
    
    
   


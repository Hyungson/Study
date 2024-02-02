# 유클리드 호제법을 이용. 2개의 자연수 a ,b (a>b)에 대해서 
# a를 b로 나눈 나머지가 r 일 때, a,b의 최대 공약수는 b와 r의 최대공약수와 같다.

# a와 b의 최소 공배수는 a와 b의 곱을 a와 b의 최대공약수를 나눈 것과 같다.

import sys
input = sys.stdin.readline # 테스트 케이스 수
T = int(input())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    a, b = max(a,b), min(a,b)
    c = a*b
    while b != 0:
        r = a % b
        a = b
        b = r
    print(int(c/a))



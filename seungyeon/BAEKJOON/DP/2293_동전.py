# import sys
# input=sys.stdin.readline

# n,k=map(int,input().split())
# arr=[]
# for i in range(n):
#     arr.append(int(input()))

# arr.sort()
# dp=[0] * (k+1)
# dp[0]=1  # 하나도 안쓰는 경우 

# for i in arr:
#     for j in range(i,k+1):
#         dp[j] += dp[j-i]
# print(dp[k])


import sys
input=sys.stdin.readline

n,k=map(int,input().split(" "))
arr=[]
for i in range(n):
    arr.append(int(input()))

# 값이 k원이 될 수 있는 경우의 수 
dp=[0] * (k+1)

arr.sort()

dp[0] = 1

for i in arr:
    for j in range(i,k+1):
        dp[j] += dp[j-i]

print(dp[k])
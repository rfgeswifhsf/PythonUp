# dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]


s = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]


# 求和路径
[
 [1, 4, 5],
 [2, 7, 6],
 [6, 8, 7]
 ]


dp=[[0]*len(s[0]) for i in range(len(s))]

dp[0][0]=s[0][0]
for i in range(0,len(s)):
    for j in range(0,len(s[0])):
        if i ==0 and j!=0:
            dp[i][j]=dp[i][j-1]+s[i][j]
        elif i!=0 and j==0:
            dp[i][j]=dp[i-1][j]+s[i][j]
        elif i!=0 and j!=0:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + s[i][j]

print(dp)

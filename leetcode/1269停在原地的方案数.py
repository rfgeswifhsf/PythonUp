'''
其实就是 {（（））}  判断是不是完整括号

0,1,-1
输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动

'''


steps = 3
arrlen = 2


def numWays(steps, arrLen):
    dp = [[0,1] + [0]*min(steps, arrLen) for i in range(2)]
    print(dp)
    for i in range(steps):
        for j in range(1, min(min(steps, arrLen), steps-i+1)+1):
            dp[(i+1)%2][j] = (dp[i%2][j-1] + dp[i%2][j] + dp[i%2][j+1]) % (10**9+7)
    return dp[steps%2][1]


numWays(3,2)

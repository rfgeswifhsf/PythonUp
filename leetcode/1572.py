class Solution:
    def diagonalSum(self, mat) :
        lenth = len(mat)
        print(lenth)
        sum=0
        for i in range(0,len(mat)):
            sum+=mat[i][i]
            sum+=mat[i][len(mat)-1-i]
        if lenth%2==1:
            sum=sum-mat[int(lenth/2)][int(lenth/2)]

        return  sum
mat = mat = [[5]]

s = Solution()
a= s.diagonalSum(mat)

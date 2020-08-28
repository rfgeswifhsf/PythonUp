class Solution:
    def minEatingSpeed(self, piles, H):
        n = len(piles)
        left = 1
        right = max(piles)
        res = 1
        while left <= right:
            mid = (left + right) // 2
            tmp = 0
            for i in range(n):
                if 0 == piles[i] % mid:
                    tmp += piles[i] // mid
                else:
                    tmp += piles[i] // mid + 1
            if tmp <= H:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res

'''
输入: piles = [3,6,7,11], H = 8
输出: 4
'''
piles = [3,6,7,11]
H = 8
s= Solution()
a = s.minEatingSpeed(piles,H)
print(a)

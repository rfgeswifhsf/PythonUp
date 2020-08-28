class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:

            mid = (l + r) // 2
            print(l, r, mid, ans)
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

s = Solution()
ans = s.mySqrt(8)
print(ans)

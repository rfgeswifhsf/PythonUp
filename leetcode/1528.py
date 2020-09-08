class Solution:
    def restoreString(self, s, indices) -> str:
        # zipper = [list(t) for t in zip(s,indices)]
        zipper = list(zip(s,indices))
        zipper.sort(key=lambda x:x[1])
        return ''.join([i[0] for i in zipper])


sts = 'aaiougrt'
s = Solution()
a = s.restoreString(sts,[4,0,2,6,7,3,1,5])
print(a)

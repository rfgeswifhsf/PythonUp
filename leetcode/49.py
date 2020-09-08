class Solution:
    def groupAnagrams(self, strs):
        mapx = dict()
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            print(tmp)
            if tmp in mapx:
                mapx[tmp].append(i)
            else:
                mapx[tmp] = [i]
        return list(mapx.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
a = s.groupAnagrams(strs)
print(a)

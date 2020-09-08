class Solution:
    def rearrangeBarcodes(self, barcodes) :
        l = [barcodes[0]]
        m=0
        while m<len(barcodes):

            if l[-1]!=barcodes[m]:

                l.append(barcodes[m])
                barcodes.remove(barcodes[m])
                m=0

            m=m+1
        return l

barcodes = [1,1,1,2,2,2]
s = Solution()
a = s.rearrangeBarcodes(barcodes)

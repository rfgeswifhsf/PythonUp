class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        c=0
        for i in range(len(points)-1):
            c+=max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
            print(abs(points[i+1][0]-points[i][0]),abs(points[i+1][1]-points[i][1]))
            print(c)
        return c

s =Solution()
a =s.minTimeToVisitAllPoints( [[1,1],[3,4],[-1,0]])

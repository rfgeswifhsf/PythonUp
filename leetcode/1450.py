'''
示例 1：

输入：startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
输出：1
解释：一共有 3 名学生。
第一名学生在时间 1 开始写作业，并于时间 3 完成作业，在时间 4 没有处于做作业的状态。
第二名学生在时间 2 开始写作业，并于时间 2 完成作业，在时间 4 没有处于做作业的状态。
第三名学生在时间 3 开始写作业，预计于时间 7 完成作业，这是是唯一一名在时间 4 时正在做作业的学生。

示例 2：
输入：startTime = [4], endTime = [4], queryTime = 4
输出：1
解释：在查询时间只有一名学生在做作业。

示例 3：
输入：startTime = [4], endTime = [4], queryTime = 5
输出：0

示例 4：
输入：startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
输出：0
'''

startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4

class Solution:
    def busyStudent(self, startTime, endTime, queryTime) -> int:
        count =0
        a = [_ for _ in list(map(list,zip(startTime,endTime))) if _[1]>=queryTime and _[0]<=queryTime]

        # for i,j in zip(startTime,endTime):
        #     if queryTime>=i and queryTime<=j:
        #         count+=1
        return len(a)

s = Solution()
a = s.busyStudent(startTime,endTime,queryTime)
print(a)

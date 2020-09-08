'''
输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。

'''
class Solution:
    def twoCitySchedCost(self, costs) -> int:
        costs.sort(key = lambda x : x[0] - x[1])#差值排序
        print(costs)
        total = 0
        n = len(costs) // 2#a城市和b城市都去n個人
        cost=list(zip(*costs))#按照去a和b的分別分組..
        print(list(zip(*costs)))
        # print(costs)
        return sum(cost[0][:n]+cost[1][n:])


ss =[[10,20],[30,200],[400,50],[30,20]]
s =Solution()
a = s.twoCitySchedCost(ss)

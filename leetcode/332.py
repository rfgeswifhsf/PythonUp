'''
输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]

示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
'''

# print(min(["JFK","ATL","JFK","SFO","ATL","SFO"],["JFK","SFO","ATL","JFK","ATL","SFO"]))

class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        ticket_dict = defaultdict(list)
        for item in tickets:
            ticket_dict[item[0]].append(item[1])

        path = ['JFK']

        def backtrack(cur_from):
            if len(path) == len(tickets) + 1:  # 结束条件
                return True
            ticket_dict[cur_from].sort()
            for _ in ticket_dict[cur_from]:
                cur_to = ticket_dict[cur_from].pop(0)  # 删除当前节点
                path.append(cur_to)  # 做选择
                if backtrack(cur_to):  # 进入下一层决策树
                    return True
                path.pop()  # 取消选择
                ticket_dict[cur_from].append(cur_to)  # 恢复当前节点
            return False

        backtrack('JFK')
        return path

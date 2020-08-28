'''
移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。
如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。

输入: "UD"
输出: true
'''

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # for i in ('R','L','U','D'):
        #     if i in moves:
        #         moves.re
        moves = [_ for _ in moves]
        print(moves)
        dict_ = {'R':'L','L':'R','U':'D','D':'U'}
        flag = True
        while moves and flag:
            for i in ('R','L','U','D'):
                if i in moves:
                    moves.remove(i)
                    if dict_[i] in moves:
                        moves.remove(dict_[i])
                    else:
                        flag = False
                        break

            if flag is False:
                return False
                break
        return True

s = Solution()
a = s.judgeCircle('UD')
print(a)

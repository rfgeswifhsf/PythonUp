'''
给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。

示例 1:
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
["hit","hot","dot","lot","log","cog"]

示例 2:
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []
解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
'''

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        l =[beginWord]
        if endWord not in wordList:
            return []
        j=0
        while beginWord!=endWord and j<len(endWord):
            i=0

            # print('===')
            while wordList and i<len(wordList):
                j = 0
                # print(wordList[i])
                count=0
                while j <len(beginWord):
                    if beginWord[j]!=wordList[i][j]:
                        count+=1
                    if count>1 :
                        break
                    j+=1
                if count ==1:
                    beginWord=wordList[i]
                    wordList.remove(beginWord)
                    l.append(beginWord)
                    j=0
                else:
                    i+=1
            j+=1
        return l


# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList):
#
#         if endWord!=wordList:
#             return []
#         while beginWord!=endWord:
#            for i in range(len(beginWord)):
#                word = beginWord
#                if word[0:i]+word[i+1:] in wordList:



beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

s = Solution()
a = s.findLadders(beginWord,endWord,wordList)
print(a)
#
# a = list(filter( lambda x:x in beginWord,wordLists ) for wordLists in wordList)
#
# m = beginWord.find('h.t')
# print(m)
# cmp()

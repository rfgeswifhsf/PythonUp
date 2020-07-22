'''
s = "applepenapple", wordDict = ["apple", "pen"]
ture
'''

def pp():
    s = "applepenapple"
    wordDict = ["apple", "pen"]

    lent = [len(i) for i in wordDict]

    for w in wordDict:
        if w in s:
            s= s.replace(w,'')
    print(s)
    return 1==1
a= pp()
print(a)

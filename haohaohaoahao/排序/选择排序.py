'''
找最小放前面

'''
s = [7,2,1,4,3,6]

for i in range(0,len(s)):
    min_ = max(s)
    for j in range(i,len(s)):
        if s[j]<min_:
            min_=s[j]
            k=j
    s[i],s[k]=min_,s[i]
    print(s)

# print(s)
'''
[1, 2, 7, 4, 3, 6]
[1, 2, 7, 4, 3, 6]
[1, 2, 3, 4, 7, 6]
[1, 2, 3, 4, 7, 6]
[1, 2, 3, 4, 6, 7]
[1, 2, 3, 4, 6, 7]

'''

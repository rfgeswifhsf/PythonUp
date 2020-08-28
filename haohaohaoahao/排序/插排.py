s = [7,2,1,4,3,6]
for i in range(0,len(s)):
    current = s[i]
    index_pre = i-1

    while index_pre>=0 and s[index_pre]>current:
        s[index_pre+1]=s[index_pre]
        index_pre-=1
    s[index_pre+1] = current

    print(s)

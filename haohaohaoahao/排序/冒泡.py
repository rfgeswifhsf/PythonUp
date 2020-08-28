s = [7,2,1,4,3,6]
print('原始',s)
for i in range(0,len(s)):
    for j in range(0,len(s)-1-i):
        if s[j+1]<s[j]:
            s[j],s[j+1] = s[j+1],s[j]
        print(s)

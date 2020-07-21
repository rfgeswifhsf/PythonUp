'''
第i个元素与之前i-1个元素比较大小，插到合适位置

'''

lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]

i=0

while i<len(lists)-1 :

    while lists[i+1]<lists[i] and i>=0:
        lists[i],lists[i+1] = lists[i+1],lists[i]
        i =i-1

    i=i+1
print(lists)

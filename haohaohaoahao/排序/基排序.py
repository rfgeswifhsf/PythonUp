'''
基排序
根据个位，将数据分组
再根据十位，将数据依次分组
再根据百位，将数据依次分组，
。。。
最后依次输出
'''

s =  [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]

max_num = max(s)
l=len(str(max_num))


i=1
while i<l+1:
    list1 = [[] for _ in range(10)]
    list2 = []
    for j in s:
        # print(int(j/10**(i-1))%10)
        list1[int(j/(10**(i-1)))%10].append(j)

    # print(list1)
    for k in list1:
        for m in k:
            list2.append(m)

    s= list2
    i+=1

print(s)

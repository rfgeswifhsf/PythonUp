lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]


def quicksort(list,left,right):
    if list is None:
        return list
    '''
    注意这个限制条件，不然会超过最大迭代，报错
    '''
    if left >= right:
        return list
    low = left
    high = right
    pivot = lists[low]
    while left < right:
        while left<right and lists[right]>= pivot :
            right = right-1
        lists[right] ,lists[left] = pivot,lists[right]
        pivot = lists[right]

        while left<right and lists[left]<=pivot :
            left = left+1
        lists[left],lists[right] = pivot,lists[left]
        pivot = lists[left]
    quicksort(lists,low,left-1)
    quicksort(lists,left+1,high)
    return lists

print(lists)
aa= quicksort(lists,0,len(lists)-1)

print(aa)

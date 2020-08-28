s = 81

left = 0
right =s


while left<right:
    mid = (left+right)//2+1

    if mid*mid >s:
        right = mid-1
    elif mid*mid <s:
        left =mid+1
    else:
        print(mid)
        break
    # print('mid', mid, 'left', left, 'right', right)

    if abs(left-right)<=1:
        print(right)

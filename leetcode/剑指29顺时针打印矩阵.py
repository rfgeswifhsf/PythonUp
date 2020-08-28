from typing import List

matrix = [[1,2],[4,5],[7,8]]

# 顺时针旋转
# matrix[:] = map(list,zip(*matrix[::-1]))
# print(matrix)
# 逆时针旋转
# matrix[:] = map(list,zip(*matrix))
# matrix = matrix[::-1]
# print(matrix)
#
# matrix.remove(matrix[0])
# print(matrix)


re = []
while len(matrix)>0:
    re.extend(matrix[0])
    matrix.remove(matrix[0])
    matrix[:] =list(zip(*matrix))

    matrix = matrix[::-1]
print(re)



# print(list(map(list,zip(*matrix))))



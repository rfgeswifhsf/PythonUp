'''
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。


示例 1：
输入：1
输出：true

示例 2：
输入：10
输出：false

示例 3：
输入：16
输出：true

示例 4：
输入：24
输出：false

示例 5：
输入：46
输出：true

'''

l=[]
for i in range(100):
    if 2**i<10**9:
        l.append(2**i)
    else:
        break
print(l)

N=56635

a= [_ for _ in l if len(str(_))==len(str(N))]
print(a)
N = [_ for _ in str(N)]
i=0
while N and i<len(N):
    j=0
    print('N',N)
    while a and j<len(a):
        if N[i] not in str(a[j]) and str(a[j])!='?':
            a.remove(a[j])
            continue
        if N[i] in str(a[j]):
            a[j] = str(a[j]).replace(N[i],'?',1)
        j += 1
    print(N[i],a)
    i+=1
# print(a)
if len(a)>0:
    print(True)
else:
    print(False)

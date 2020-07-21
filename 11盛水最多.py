'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water


输入：[1,8,6,2,5,4,8,3,7]
输出：49
'''

a= [1,8,6,2,5,4,8,3,7]

max_area =0

i=0
j=len(a)-1
pivot_area=0


while i<j:
    area = min(a[i],a[j])*(j-i)
    pivot_area = max(pivot_area,area)

    if a[i]<=a[j]:
        i+=1
    else:
        j-=1

print(pivot_area)


# class Solution {
# public:
#     int maxArea(vector<int>& height) {
#         int l = 0, r = height.size() - 1;
#         int ans = 0;
#         while (l < r) {
#             int area = min(height[l], height[r]) * (r - l);
#             ans = max(ans, area);
#             if (height[l] <= height[r]) {
#                 ++l;
#             }
#             else {
#                 --r;
#             }
#         }
#         return ans;
#     }
# };





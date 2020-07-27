# 8/11




#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)

import sys

# def fun(array1,array2,array3):
#     line1 = sys.stdin.readline().strip(array1)  # 讀取每一行
#     list1 = list(map(int, line1.split()))  # 每一行轉換成數字
#     line2 = sys.stdin.readline().strip(array2)  # 讀取每一行
#     list2 = list(map(int, line2.split()))  # 每一行轉換成數字
#     line3 = sys.stdin.readline().strip(array3)
#     k = int(line3)
#     e=0
#     f=0
#     for a in range(len(list1)-1):
#         for b in range(len(list2)-1):
#             if list2[b] <= list1[a]:
#                 f += list2[b] + list1[a]
#                 e+=1
#                 if e>=k:
#                     print(f)
#                     return

# n = int(sys.stdin.readline().strip())
# list_all = []
# for i in range(n):
#     # 读取每一行
#     line = sys.stdin.readline().strip()
#     values = list(map(int, line.split())) #每一行轉換成列表的數字形式
#     list_all.append(values)
list1 = [1,2,3,4,5,67]
list2 = [1,1,2,2,2,2,2,2]
k = 5
e = 0
f = 0
for a in range(1,len(list1)):
    for b in range(len(list2)-1):
        if list2[b] <= list1[a-1]:
            f += list2[b] + list1[a-1]
            e += 1
            if e >= k:
                print(f)
                break

    if e >= k:
        break


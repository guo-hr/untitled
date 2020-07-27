# coding=utf-8
import sys
# from copy import deepcopy
# # line = sys.stdin.readline().strip(',')
# # values = list(map(int, line.split(',')))
# values= [3,1,2,2,2]
# b=deepcopy(values)
# b.sort(reverse=True)
# c=[]
# v = 1
# for i in range(1,len(values)):
#     k = b.index(values[i])
#     if values[i] == values[i-1]:
#         k +=v
#         v+=1
#     else:
#         v=1
#     c.append(k)
# ff = ''
# for i in range(len(c)):
#     if i!=len((c))-1:
#         ff+=str(c[i])+','
#     else:
#         ff+=str(c[i])
# print(ff)
import copy
def threeSum(nums):
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        if nums[k] > 0:
            print(nums[k])
            break # 1. because of j > i > k.
        # if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
        i, j = k + 1, len(nums) - 1
        while i < j: # 3. double pointer
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i - 1]: i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]: i += 1
                while i < j and nums[j] == nums[j + 1]: j -= 1
    return res

if __name__ == '__main__':
    nums = [5,1,3,5,6,72,0,-1,-2,-3,1,2,3,4,5,-1,-2,3,-5]
    print(threeSum(nums=nums))
    a = range(5)
    for i in a:
        print(i)
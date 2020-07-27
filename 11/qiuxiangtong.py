# coding=utf-8
#排序算法
#1、冒泡排序
#2、选择排序
#3、插入排序
#4、希尔排序
#5、堆排序
#6、归并排序
#7、快速排序




def maxVowels(s: str, k: int) -> int:
    res = cur = 0
    for i in range(len(s)):
        if s[i] in 'aeiou':
            cur += 1
        if i >= k:
            cur -= s[i-k] in 'aeiou'
        res = max (res,cur)
    return res

if __name__ == '__main__':
    s = 'abciiiidef'
    k = 3
    print(maxVowels(s,k))
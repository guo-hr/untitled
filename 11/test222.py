# coding=utf-8
#m个处理器，n个任务，已知每个任务的耗时，处理器处理原则是优先处理耗时低的任务，
#每次最多调入m个任务，计算处理完n个任务总的耗时是多少
# 问题：求一个字符串中不重复字符的最长子串，如字符串“abacdefgafg”,最长的不重复的子串为“bacdefg”,长度为7，当有两个长度相同的字符串，输出第一个最长的字符
#     print(fun(all_time,lst,m))
import copy
a = [1,1,1,1,1,1,1,1]
if set(a) == {1}:
    print(a)
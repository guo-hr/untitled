# coding=utf-8
# def fun(N,K):
#     if N == 1:
#         return range(1,9)
#     out_list = []
#     for i in range(N):
def quick_sort(b):
    if set(b) == {1}:
        return len(b)
    left, right = [], []
    for item in b:
        if item == 2:
            left.append(item - 1)
            right.append(item - 1)
            continue
        left.append(item-1)
        right.append(item-2)
        print(left,right)
    return quick_sort(left)  + quick_sort(right)

if __name__ == '__main__':
    b = [3]
    print(quick_sort(b))
#实现字符串反转，以逗号作为切割符，切割的子串以单词作为单元反转
# 输入：hello world，god bless you
# 输出：world hello，you bless god


def fun(a):
    c = []
    b = a.split(',')
    for i in b :
        k  = i.split(' ')
        c.append(k[::-1])
        c.append(',')
    return ''.join(c)

if __name__ == '__main__':
    a = 'hello world，god bless you'
    print(fun(a))
import  re
#他提供了科目号和关键字
text_id=1231321
text_1='吃饭,睡觉'
def func():
    new_text=[]
    with open('1.txt','r') as a:
        line = a.readline()
        while True:
            if line is None:
                break
            content=int(re.findall(r'1\d{9}',line)[0]) #这里是提取字符串中的科目号
            if content > text_id:
                line=a.readline()
            elif content == text_id:
                new_text.extend(line)
                line=a.readline()
            else:
                break
    #跳出这个循环的时候就应该获得了相应科目号的所有lines在new_text中
    #现在开始匹配关键字
    for i in new_text:
        newt_text_1=re.findall(r'[\u4e00-\u9fa5]+',i) #获取lines中的单行关键字,应该也是个列表
        for k in newt_text_1:
            for b in text_1:
                if b in k:
                    return re.findall(r'1\d*',line)[0]  #获取到第一个匹配成功的单行的最小的序列号







"""

                                        时间复杂度
                        算法的执行效率，算法的执行时间与算法输入值之间的关系
                                         大O表示法
       时间复杂度:
        O(1)        都是常量数据
        O(N)        存在 for 循环
        O(logN)     存在 while 循环
        O(M+N)      存在双循环，且并列执行
        O(NlogN)    for循环 嵌套 while循环  反之  while循环 嵌套 for循环
        O(N2)       for循环 嵌套 for循环

        对比：
             O(1) < O(logN) < O(N) <  O(NlogN) < O(N2)(N的二次方) < O(2N)（2的N次方） < O(N!)（N的阶乘）
                    二分查找              排序
"""
def O1(num):
    #  i 跟 j 都 固定的值
    #  算法 ： a+b 相当于一个常数
    #  所以 时间复杂度都是O（1） 因为跟num值无关都是只需要运行一次
    i = num
    j = num **2
    return i + j

def ON(num):
    #  for循环，当前num肯定不是常量了
    #  num 不是固定的值，那么就相当于N了
    #  O（N）
    total = 0
    for i in range(num):
        total += i
    return total

def OlogN(num):
    # while 循环，不是从0开始
    # i*2  logN
    i = 1
    while (i<num):
        i = i*2
    return i

def OMN(num1,num2):
    # 有双循环，并且都是并列的
    # i = M
    # j = N
    total = 0
    for i in range(num1):
        total += i
    for j in range(num2):
        total += j
    return total

def ONlogN(num1,num2):
    # for循环里面嵌套 while循环
    #
    total = 0
    j = 0
    for i in range(num1):
        while(j < num2):
            total += i + j
            j = j * 2
    return total

def ON2(num):
    # for循环 嵌套 for循环
    #
    total =0
    for i in range(num):
        for j in range(num):
            total += i+j
    return total

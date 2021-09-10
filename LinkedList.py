"""
     链表：
        线性的顺序存储数据，而是在每一个节点里存到下一个节点的指针(Pointer)。由于不必须按顺序存储
     特点：
        写入很快，读写很慢 ===> 读少写多
     优点：
        插入和删除的效率高，只需要改变指针的指向就可以进行插入和删除。
        内存利用率高，不会浪费内存，可以使用内存中细小的不连续的空间，
        只有在需要的时候才去创建空间。大小不固定，拓展很灵活。
    缺点：
        查找的效率低，因为链表是从第一个节点向后遍历查找
    单端列表
    双端列表

    访问 O（N）
    搜索 O（N）
    插入 O（1）
    删除 O（1）
"""
from collections import deque
# 创建链表
linkedlist = deque()
# 添加元素
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)     # O(1)
# [1,2,3]
linkedlist.insert(2,99)  # O(N)
# 访问元素
element = linkedlist[2]
# 99
# 搜索元素
index = linkedlist.index(99)
# 2
# 更新元素
linkedlist[2] = 88  # O(N)
# 1,2,88,3
# 删除元素
linkedlist.remove(88)
# [1,2,3]
# 链表长度
length = len(linkedlist)
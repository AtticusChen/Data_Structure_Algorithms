"""
Queue:
概念：  队列是由一系列对象组成的集合，这些对象插入和删除遵循先进先出的原则。
场景： 游乐场排队
特点： 先入先出（FIFO）

    单端队列：只有一个口可以进，一个口可以出
    双端队列：两个口都可以进，两个口都可以出

时间复杂度：
    访问 O（N）
    搜索 O（N）
    插入 O（1）
    删除 O（1）

"""
from collections import deque
# 创建队列
queue = deque()
# 添加元素
queue.append(1)
queue.append(2)
queue.append(3)
# [1,2,3]
# 获取即将出队的元素
temp = queue[0]
# 删除即将出队的元素
temp2 = queue.popleft()
# 判断队列是否为空，队列的长度
bool_queue = len(queue) == 0
# 遍历队列
while len(queue) !=0:
    temp = queue.popleft()
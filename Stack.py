"""
Stack：
概念：栈是由一系列对象组成的一个集合，这些对象的插入和删除操作遵循先进后出的原则
特点：先进后出（LIFO）
场景：浏览器的后退功能

时间复杂度：
    访问  O（1） 栈顶元素
    搜索  O（N）
    插入  O（1）
    删除  O（1） 栈顶元素
"""
# 创建栈
stack = []
# 添加元素
stack.append(1)
stack.append(2)
stack.append(3)
# 查看栈顶元素    即将出栈的元素
stack[-1]
# 删除栈顶元素    即将出栈的元素
temp = stack.pop()
# 栈的长度
len(stack)
# 栈是否为空
len(stack) ==0
# 遍历栈 边删除边遍历
while len(stack) >0:
    temp = stack.pop()



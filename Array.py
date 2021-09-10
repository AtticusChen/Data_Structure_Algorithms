"""
数组：在连续的内存空间，存储一组相同数据类型的元素

特点： 适合读，不适合写-->读多写少

区分：
     元素     [1,2,3]
     索引      1-->0  2-->1  3-->2
====================================
    数组访问（Access） a[0] --> 1 通过索引访问
    数组搜索（Search） 查看此数组中是否存在 1

======================================
数组        时间复杂度
    访问      O(1)
    n代表数组长度 ，考虑最坏的情况
    搜索      O(n)
    插入      O(n)
    删除      O(n)
"""
# 创建数组
import numpy as np
n = np.array([1,2,3,4])
print(n)
# 数组插入  insert(插入变量,变量索引，插入值)
n_insert = np.insert(n,0,[100])
print(n_insert )
# 数组插入  append 末尾插入，返回一个新数组，而原数组不变
n_insert_1 = np.append(n,100)
print(n_insert_1)
# 数组访问
n_Access = n[0]
print(n_Access)
# 修改数组

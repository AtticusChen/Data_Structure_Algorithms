"""
找出数组中重复的数字。


    在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
    数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
    请找出数组中任意一个重复的数字。

示例1：

输入：
    [2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""
#方法一：哈希表 / Set
# 利用数据结构特点，容易想到使用哈希表（Set）记录数组的各个数字，当查找到重复数字则直接返回
class Solution:
    def findRepeatNumber(self, nums):
        dic = set()
        for i in nums:
            if i in dic:
                return i
            else:
                dic.add(i)


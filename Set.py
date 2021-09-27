"""
Set
    无序，不重复

概念：
应用场景：
    1. 检查某一个元素是否存在
    2. 查询是否有重复元素

set: Hashset\Linklistset\TreeSet
    哈希集合

访问
搜索
    无哈希冲突    O（1）
    有哈希冲突    O（k）
插入
    无哈希冲突   O（1）
    有哈希冲突   O（k）
删除
    无哈希冲突   O（1）
    有哈希冲突   O（k）
"""
# 创建集合
s = set()
# 添加元素
s.add(10)
s.add(3)
s.add(5)
s.add(2)
s.add(2)
# 搜索元素
l = 2 in s
# 删除元素
s.remove(2)
# 长度
len(s)

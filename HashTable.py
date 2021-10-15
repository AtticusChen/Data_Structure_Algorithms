"""
Hash Table
    哈希表 = 散列表
概念：
    根据关键值（key Value）而直接进行访问的数据结构，通过把关键的码值映射到
    表中一个位置来访问记录，加快查找记录，
    这个映射函数叫散列函数，存放记录叫散列表

key:value 键值对

哈希碰撞：
    2个不同的key通过一个哈希函数得到相同的内存地址
    解决方法：链表方式解决
        简单来说，使用链表的方式进行解决，通过解析内存地址查看是否是对应的key，
            如果不是对应的key，那么直接next下一个继续查看是否是对应的key
时间复杂度：
    访问：哈希表中是不存在访问
    搜索：O（1） 碰撞O（k）k代表碰撞的次数
    插入：O（1）
    删除：O（1）
"""
# 应用：单词频率统计
"""
考虑统计一个文档中单词出现的频率的问题，以此作为使用映射研究实例

需求：
    一个统计单词出现频率并报告出现最频繁的单词程序
"""
freq = {}
for piece in open("").read().lower().split():
    word = ''.join(c for c in piece if c.isalpha())
    if word:
        freq[word] = 1 + freq.get(word,0)
max_word = ''
max_count = ''
for (w,c) in freq.items():
    if c > max_count:
        max_word = w
        max_count = c

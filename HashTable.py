"""
<<<<<<< HEAD
Hash Table 哈希表
哈希表 = 散列表
key:value 键值对


"""
=======
Hash Table
    哈希表 = 散列表
概念：
    根据关键码值（key Value）而直接进行访问的数据结构，通过把关键的码值映射到
    表中一个位置来访问记录，加快查找记录，
    这个映射函数叫散列函数，存放记录叫散列表

key:value 键值对

哈希碰撞：
    2个不同的key通过一个哈希函数得到相同的内存地址
    解决方法：
        简单来说，使用链表的方式进行解决，通过解析内存地址查看是否是对应的key，
            如果不是对应的key，那么直接next下一个继续查看是否是对应的key
时间复杂度：
    访问：哈希表中是不存在访问
    搜索：O（1） 碰撞O（k）k代表碰撞的次数
    插入：O（1）
    删除：O（1）
"""

# 创建哈希表
hashTable = [''] * 4  # 数组创建
mapping = {}          # 字典
# 添加元素  O[1]
    # 数组
hashTable[1] = 'lihua'
hashTable[2] = 'wangming'
hashTable[3] = 'hanmei'
    # 字典
mapping[1] = 'lihua_dict'
mapping[2] = 'wangming_dict'
mapping[3] = 'hanmei_dict'

# 删除元素 O[1]
    # 数组
hashTable[1] = ''
    # 字典
mapping.pop(1)  # 把key 1 删除
del mapping[1]

# 获取key的值
    # 数组
hashTable[3]
    # 字典
mapping[3]
# 检查key是否存在
    #字典
dict_key = 3
dict_key in mapping

# 哈希表长度
    #字典
len(mapping)
# 哈希表是否还有元素
    # 字典
len(mapping) ==0
>>>>>>> bac658492d37f11e2814da8f40992488ba925d6b

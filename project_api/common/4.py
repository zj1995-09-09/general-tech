def unique_chars(s):
    result = []
    for char in s:
        if char not in result:
            result.append(char)
    return ''.join(result)


s = input("请输入字符串：")
print(unique_chars(s))

"""输入一个字符串，求出该字符串包含的字符集合
输入描述:
每组数据输入一个字符串，字符串最大长度为100，且只包含字母，不可能为空串，区分大小写。
输出描述:
每组数据一行，按字符串原有的字符顺序，输出字符集合，即重复出现并靠后的字母不输出。用 Python 求解
"""

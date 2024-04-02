def replace_space(str, length):
    return str[:length].replace(" ", "%20")


str = input("请输入一个字符串：")
length = int(input("请输入长度："))
print(replace_space(str, length))

"""请编写一个方法，将字符串中的空格全部替换为“%20”,给定一个string iniString 为原始的串，以及串的长度 int len, 
返回替换后的string 同时保证字符串由大小写的英文字母组成。用 Python 求解"""
def remove_chars(s1, s2):
    for char in s2:
        s1 = s1.replace(char, '')
    return s1


s1 = input()
s2 = input()
print(remove_chars(s1, s2))

"""输入两个字符串，从第一字符串中删除第二个字符串中所有的字符。例如，输入”They are students.”和”aeiou”，
则删除之后的第一个字符串变成”Thy r stdnts.”
输入描述:
每个测试输入包含2个字符串
输出描述:
输出删除后的字符串 用 Python 求解"""
import re


def find_longest_digit_string(s):
    digit_strings = re.findall(r'\d+', s)
    longest_digit_string = max(digit_strings, key=len)
    return longest_digit_string


s = input()
print(find_longest_digit_string(s))
"""这段代码的功能是找出输入字符串中最长的连续数字串。

首先，它导入了Python的正则表达式模块re。

然后定义了一个函数find_longest_digit_string，这个函数接受一个参数s，即需要处理的字符串。

在函数内部，首先使用re.findall函数找出字符串s中所有的连续数字串，并将这些数字串存储在列表digit_strings中。这里的正则表达式'\d+'表示匹配一个或多个数字。

然后，使用max函数找出列表digit_strings中最长的字符串。max函数的key参数设置为len，表示比较的标准是字符串的长度。

最后，函数返回最长的数字串。

在主程序部分，首先使用input函数获取用户的输入，然后将这个输入传递给find_longest_digit_string函数，并打印出返回的结果。"""

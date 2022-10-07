"""
正则表达式：用来使用某种规则匹配字符串当中的子串。

YUze wang 123456

regular expression: 正则表达式
"""
import re

my_string = 'yuzewang123456'

pattern = 'wang'
result = re.search(pattern=pattern, string=my_string)
# 匹配对象
print(result)
# 得到最终的结果，默认值为0
# 要得到的匹配到的字符串，一定要加 group()
print(result.group(0))

# [abc123], 表示中括号当中任选其一。
my_string = 'yuzewang123456'
pattern = 'w[abc123]ng'
result = re.search(pattern=pattern, string=my_string)
print(result)

# . 只能匹配任意一个字符
my_string = 'yuzewang123456'
pattern = 'yuz.'
result = re.search(pattern=pattern, string=my_string)
print(result)

# ｛m,n｝匹配 m-n 次， 最少m 次，最多n次， 贪婪模式
my_string = 'yuzewang123456'
pattern = '.{6,9}?'
result = re.search(pattern=pattern, string=my_string)
print(result)


# ｛m｝匹配 m次
my_string = 'yuzewang123456'
# 匹配任意字符7次
pattern = '.{7}'
result = re.search(pattern=pattern, string=my_string)
print(result)

# *表示匹配0次或多次
# ?表示非贪婪模式
# .*? 常用组合：尽可能少的匹配任意字符
my_string = '{"mobile_phone": "#investor_phone#, "pwd": "#investor_pwd#"}'
pattern = '#.*?#'
result = re.search(pattern=pattern, string=my_string)
print(result)


my_string = '{"mobile_phone": "#investor_phone#, "pwd": "#investor_pwd#"}'
# 0次或1次
pattern = '.?'
result = re.search(pattern=pattern, string=my_string)
print(result)

# \w : 匹配一个字母
my_string = '{"mobile_phone": "#investor_phone#, "pwd": "#investor_pwd#"}'
pattern = '\w'
result = re.search(pattern=pattern, string=my_string)
print(result)

# \d : 匹配一个数字
my_string = '{"mobile_phone": "#i34nvestor_phone#, "pwd": "#investor_pwd#"}'
pattern = '\d'
result = re.search(pattern=pattern, string=my_string)
print(result)

# 分组
my_string = '{"mobile_phone": "#investor_phone#, "pwd": "#investor_pwd#"}'
pattern = '#.*?#'
result = re.search(pattern=pattern, string=my_string)
print(result.group())


class Data:
    investor_phone = '13788881111'
    investor_pwd = '123456'

# finditer 找多个匹配数据
# search 是只匹配一次
my_string = '{"mobile_phone": "#investor_phone#, "pwd": "#investor_pwd#"}'
pattern = '#(.*?)#'
results = re.finditer(pattern=pattern, string=my_string)
for result in results:
    old = result.group()
    #
    key = result.group(1)
    new = getattr(Data, key, '')
    my_string = my_string.replace(old, new)

print(my_string)

my_string = '{"mobile_phone": "#investor_phone#}'
pattern = '#(.*?)#'
result = re.search(pattern=pattern, string=my_string)
print(result.group())
# group(1) 获取括号当中的内容
# group(0) 获取整个匹配内容
# 有1个括号就有group(1), 有2个括号才有group(2), 有2个括号的情况很少。
print(result.group(1))


def count_uppercase(s):
    count = 0
    for char in s:
        if 'A' <= char <= 'Z':
            count += 1
    return count


while True:
    s = input("请输入一个字符串：")
    if not s:
        break
    print("大写字母的个数为：", count_uppercase(s))

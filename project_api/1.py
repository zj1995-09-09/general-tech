def sum_of_odd(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 != 0:  # 判断i是否为奇数
            total += i
    return total


# 调用函数并输出结果
result = sum_of_odd(2)
print("1到5之间所有奇数的和为：", result)
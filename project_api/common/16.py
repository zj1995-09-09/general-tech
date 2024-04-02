def singleNumbers(nums):
    xor = 0
    for num in nums:
        xor ^= num
    mask = 1
    while xor & mask == 0:
        mask <<= 1
    a = b = 0
    for num in nums:
        if num & mask == 0:
            a ^= num
        else:
            b ^= num
    return [a, b]


num = input()
nums = num.split()
# nums = [1, 2, 3, 3, 4, 4]
print(singleNumbers(nums))

"""一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字 用 Python 求解"""
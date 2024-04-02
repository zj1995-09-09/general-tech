def rotate_string(A, n, p):
    left = A[:p + 1]
    right = A[p + 1:]
    return right + left


# A = "abcdefg"
A = input("请输入：")
n = len(A)
# p = 3
p = int(input("请输入："))
result = rotate_string(A, n, p)
print(result)

"""对于一个字符串，和字符串中的某一位置，请设计一个算法，将包括i位置在内的左侧部分移动到右边，将右侧部分移动到左边。
给定字符串A和它的长度n以及特定位置p，请返回旋转后的结果。用 Python 求解"""
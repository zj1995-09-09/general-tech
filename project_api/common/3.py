class StringFormatter:
    @staticmethod
    def format_string(A: str, n: int, arg: list, m: int) -> str:
        res = ""
        if len(A) != n or len(arg) != m:
            return res
        i = 0
        while "%s" in A:
            A = A[:A.find("%s")] + arg[i] + A[A.find("%s") + 2:]
            i += 1
        while i < m:
            A += arg[i]
            i += 1
        return A


A = input("请输入字符串：")
# n = int(input("请输入整数："))
n = len(A)
arg = list(input("请输入列表："))
# m = int(input("请输入个数："))
m = len(arg)
print(StringFormatter.format_string(A, n, arg, m))

"""请你实现一个简单的字符串替换函数,函数参数包括任意字符串A,给定长度 n,以及参数字符数组 arg.
原串中需要替换的占位符为"%s",请按照参数列表的顺序一一替换占位符。若参数列表的字符数大于占位符个数。
则将剩下的参数字符添加到字符串的结尾。用 Python 求解"""
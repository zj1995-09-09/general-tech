N = int(input())
odd_count = 0
even_count = 0

for i in range(1, N+1):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(odd_count, even_count)

"""任意输入一个正整数N，统计1~N之间奇数的个数和偶数的个数，并输出。
输入描述：
一行，一个正整数N。（1≤N≤100,000）输出描述：
一行，1~N之间奇数的个数和偶数的个数，用空格分开。
示例1:
输入
5
输出
3 2 用 Python 求解"""
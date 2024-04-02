def reverse_words(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words


sentence = input()
result = reverse_words(sentence)
print(result)
"""将一句话的单词进行倒置，标点不倒置。比如 I like beijing. 经过函数后变为：beijing. like I
输入描述:
每个测试输入包含1个测试用例： I like beijing. 输入用例长度不超过100
输出描述:
依次输出倒置之后的字符串,以空格分割 用 Python 求解"""
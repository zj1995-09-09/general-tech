def reverse_words(sentence):
    words = sentence.split(' ')
    reversed_words = words[::-1]
    return ' '.join(reversed_words)


# sentence = "I am a boy"
sentence = input("请输入：")
result = reverse_words(sentence)
print(result)


"""将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符 用 Python 求解"""
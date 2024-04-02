def grade_description(grade):
    if grade == 'A':
        return '优秀'
    elif grade == 'B':
        return '良好'
    elif grade == 'C':
        return '及格'
    elif grade == 'D':
        return '不及格'
    else:
        return '未知等级'


grade = input("请输入成绩等级：")
print(grade_description(grade))

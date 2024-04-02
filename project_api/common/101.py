my_dict_1 = {'name': 'Niuniu', 'Student ID': 1}
my_dict_2 = {'name': 'Niumei', 'Student ID': 2}
my_dict_3 = {'name': 'Niu Ke Le', 'Student ID': 3}

dict_list = []
dict_list.append(my_dict_1)
dict_list.append(my_dict_2)
dict_list.append(my_dict_3)

for d in dict_list:
    # print(f"{d['name']}'s student id is {d['Student ID']}.")
    print(f"{d['name']}'s student id is {d['Student ID']}.")

"""创建一个依次包含键-值对{'name': 'Niuniu'和'Student ID': 1}的字典my_dict_1，创建一个依次包含键-值对{'name': 'Niumei'和'Student ID': 2}的字典my_dict_2，创建一个依次包含键-值对{'name': 'Niu Ke Le'和'Student ID': 3}的字典my_dict_3，
创建一个空列表dict_list，使用append()方法依次将字典my_dict_1、my_dict_2和my_dict_3添加到dict_list 里，
使用for循环遍历dict_list，对于遍历到的字典，使用print()语句一行输出类似字符串"Niuniu's student id is
1."的语句以打印对应字典中的内容。用 Python 求解"""
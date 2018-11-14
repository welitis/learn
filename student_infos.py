# 4.实现带有字符界面的学生信息管理系统
# 要求有如下的操作界面可以选择功能
# +-------------------------------+
# |1)添加学生信息                   |
# |2)显示学生信息                   |
# |3)删除学生信息                   |
# |4)修改学生成绩                   |
# |q)退出                          |
# +-------------------------------+
# 请选择：1<回车>
# 学生信息包括：姓名，年龄，成绩（与之前相同）
# 注：每个功能与一个函数与之相对应
def input_student():
    l = []  #所有字典放在一个列表中
    n = 0   #n为列表的索引
    while True:
        names = input('请输入姓名：')
        if not names:
            break
        ages = int(input('请输入年龄：'))
        if not ages:
            break
        scores = int(input('请输入成绩：'))
        if not scores:
            break
        l.append({})    #每次循环都添加一个新字典在列表中
        l[n]['names'] = names   #给列表中的字典通过赋值的方式增加键值对
        l[n]['ages'] = ages
        l[n]['scores'] = scores
        n += 1
    return l
# l = input_student()
def output_student(l):
    if l:
        sum_name = []   #给名字长度值建立一个列表以求取最大值
        for y in l:
            nam = y['names']
            sum_name.append(len(nam))
        name_max = max(sum_name)
        lan_1 = name_max+10
        lan_2 = 8
        lan_3 = 8
        print('+'+'-'*lan_1+'+'+'-'*lan_2+'+'+'-'*lan_3+'+')
        print('|'+'names'.center(name_max+10)+'|'+'ages'.center(lan_2)+'|'+'scores'.center(lan_3)+'|')
        print('+'+'-'*lan_1+'+'+'-'*lan_2+'+'+'-'*lan_3+'+') 
        for x in l:
            name = x['names'] #从列表中遍历字典，并打印每个字典键对应的值
            age = str(x['ages'])
            score = str(x['scores'])  
            sum_name.append(len(name))  #追加字典中名字的长度值到列表sum_name中
            print('|'+name.center(name_max+10)+'|'+age.center(8)+'|'+score.center(8)+'|')
        print('+'+'-'*lan_1+'+'+'-'*lan_2+'+'+'-'*lan_3+'+')   
    else:
        print('+'+'-'*10+'+'+'-'*8+'+'+'-'*8+'+')
        print('|'+'names'.center(10)+'|'+'ages'.center(8)+'|'+'scores'.center(8)+'|')
        print('+'+'-'*10+'+'+'-'*8+'+'+'-'*8+'+') 
        print('+'+'-'*10+'+'+'-'*8+'+'+'-'*8+'+')   

# infos = input_student()
# print(infos) #打印字典组成的列表
# output_student(infos)#打印表格
def del_infos(infos):#定义删除函数
    if infos:
        del_name = input('请输入删除学生姓名：')
        for x in infos:
            if del_name in x['names']:
                infos.remove(x)
                print('删除成功！')
                break
        else:
            print('你输入的名字不存在')
    else:
        print('暂无学生信息，无法删除！')
def remove_infos(infos):#定义修改函数
    if infos:#判断学生信息是否存在
        remove_name = input('请输入修改学生姓名：')
        for x in infos:
            if remove_name in x['names']:
                while True:
                    option = input('请选择修改选项：names(n) or ages(a) or scores(s)')
                    if option == 'n':
                        name = input('请输入姓名：')
                        x['names'] = name
                        print('修改成功！')
                        break
                    elif option == 'a':
                        age = input('请输入年龄：')
                        x['ages'] = age
                        print('修改成功！')
                        break
                    elif option == 's':
                        score = input('请输入分数：')
                        x['scores'] = score
                        print('修改成功！')
                        break
                    else:
                        print('你的输入有误，请重新选择！')
                        continue
                break        
        else:
            print('你输入的名字不存在')
    else:
        print('暂无学生信息，无法修改！')
def main():
    infos = []
    while True:
        print('+-------------------------------+ ')
        print('|1）添加学生信息                |')
        print('|2）显示学生信息                |')
        print('|3）删除学生信息                |')
        print('|4）修改学生成绩                |')
        print('|q）退出                        |')
        print('+-------------------------------+ ')
        n = input('请选择：')
        if n == '1':
            infos += input_student()
        elif n == '2':
            output_student(infos)
        elif n == '3':
            del_infos(infos)
        elif n == '4':
            remove_infos(infos)
        elif n == 'q':
            break
main()
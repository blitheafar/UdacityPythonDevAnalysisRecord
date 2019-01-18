# coding:utf-8
"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
call_by_080_list = []
# 遍历通话list，找到被主叫号码前为(080)的所有被叫号码
for call in calls:
    if call[0][:5] == "(080)":
        if call[1][:2] == '(0':
            # 固定电话，提取区号，有括号，0开头
            call_by_080_list.append(call[1].split(")")[0].split("(")[1])
        elif call[1][:3] == "140":
            # 促销员电话，提取区140
            call_by_080_list.append("140")
        else:
            # 移动电话，提取区号，前4位
            call_by_080_list.append(call[1].split(" ")[0][:4])

all_call_by_080_list = call_by_080_list

# 合并重复代号
call_by_080_list = list(set(call_by_080_list))
# 顺序排序
call_by_080_list.sort()
# 输出所有代号
print('The numbers called by people in Bangalore have codes:')
for item in call_by_080_list:
    print(item)

# 生成080到080的电话list
call_by080_to_080_list = []
for call in calls:
    if call[0][:5] == "(080)" and call[1][:5] == "(080)":
        call_by080_to_080_list.append(call)
    else:
        continue

num_all_call_by_080 = len(all_call_by_080_list)
num_call_by080_to_080 = len(call_by080_to_080_list)

call_rate=float(num_call_by080_to_080)/num_all_call_by_080

print('\n{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(
    round(call_rate,4)*100))

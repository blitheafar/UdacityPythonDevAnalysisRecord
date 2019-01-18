# coding: utf-8
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
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

# 生成所有主叫电话号码，除去会发送和接收短信和被叫电话的号码

# 生成主叫电话号码list，并去重
call_list = []
for call in calls:
    call_list.append(call[0])
call_list = set(call_list)
# print(len(call_list))

# 生成会发送和接收短信和被叫电话的号码list,并去重
texter_list = []
receive_text_list = []
be_called_list = []
for call in calls:
    be_called_list.append(call[1])

for text in texts:
    texter_list.append(text[0])
    receive_text_list.append(text[1])

not_telemarketers_list = set(texter_list + receive_text_list + be_called_list)

# print(len(not_telemarketers_list))

telemarketers_list = call_list - not_telemarketers_list
telemarketers_list=list(telemarketers_list)
telemarketers_list.sort()

# 循环输出所有可能推销电话
print("These numbers could be telemarketers: ")
for telemarketers in telemarketers_list:
    print(telemarketers)

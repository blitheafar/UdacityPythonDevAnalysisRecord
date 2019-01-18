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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
texts_phone_list = []
for text in texts:
    texts_phone_list.append(text[0])
    texts_phone_list.append(text[1])

calls_phone_list = []
for call in calls:
    calls_phone_list.append(call[0])
    calls_phone_list.append(call[1])

# 合并两个list后去除重复
phone_list = set(texts_phone_list + calls_phone_list)
print("There are {} different telephone numbers in the records.".format(len(phone_list)))

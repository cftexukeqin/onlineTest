import os
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd+'../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestOnline2.settings')

import django
django.setup()

from Exams.models import Question

question = Question()

with open('exams_question.csv','r',encoding='utf-8') as fp:
    lines = fp.readlines()
    for line in lines:
        fields = line.split(",")
        fields = [i.replace('"','') for i in fields]

        question.id = int(fields[0])
        question.questionType = fields[1]
        question.content = fields[2]
        question.answer = fields[3]
        question.choice_a = fields[4]
        question.choice_b = fields[5]
        question.choice_c = fields[6]
        question.choice_d = fields[7]
        question.choice_e = fields[8]
        question.choice_f = fields[9]
        question.note = fields[10]
        question.boolt = fields[11]
        question.boolf = fields[12]
        question.add_time = fields[13]
        question.choice_num = int(fields[14])
        question.course_id = int(fields[15])
        question.save()

print("数据导入成功!")
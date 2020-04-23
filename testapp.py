#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
score = int(raw_input('输入分数:\n'))
score = 10000
abac = 1000
ttaa = "what the fuck this is "

if score >= 90:
    grade = 'A'
elif score >= 60:
    grade = 'B'
else:
    grade = 'C'
 
print ttaa + "this is the result" + grade 
print str(score) 

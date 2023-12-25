#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:49:55 2023

@author: shenyuxiang
"""

r = 0.04
annual_salary = float(input("Enter your starting annual salary:"))#一年的工资
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))#工资的多少用来储存
total_cost = float(input("Enter the cost of your dream home:"))#想买的房子的费用
semi_annual_rise = float(input("Enter the semiannual raise, as a deci mal:"))#半年加薪百分比
portion_down_payment = 0.25 * total_cost  #首付
time = 0   #所需月数
current_savings = 0  #已攒下来的钱
month_salary = annual_salary / 12 #每个月的工资
while True:
    time += 1
    if (time-1) % 6 == 0 and time != 1:
        month_salary = month_salary * (1+ semi_annual_rise)
        current_savings += month_salary * portion_saved + current_savings*r/12
    else:
        current_savings += month_salary * portion_saved + current_savings*r/12  #每个月存下来的钱+之前存下来的钱+之前存下来的钱的利息
    if current_savings >= portion_down_payment:
        break
print("Number of months:",time)
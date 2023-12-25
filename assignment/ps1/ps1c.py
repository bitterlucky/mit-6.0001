#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:56:41 2023

@author: shenyuxiang
"""

r = 0.04#年利率
annual_salary = float(input("Enter the starting salary:"))#一年的工资
portion_saved = float(input("Best savings rate:"))#每个月储蓄的最佳储蓄率
total_cost = 1000000#想买的房子的费用
semi_annual_rise = 0.07#半年加薪百分比
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
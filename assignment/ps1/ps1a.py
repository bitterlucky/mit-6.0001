#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:29:06 2023

@author: shenyuxiang
"""

r = 0.04
annual_salary = float(input("Enter your annual salary:"))#一年的工资
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))#工资的多少用来储存
total_cost = float(input("Enter the cost of your dream home:"));#想买的房子的费用
portion_down_payment = 0.25 * total_cost  #首付
time = 0   #所需月数
current_savings = 0  #已攒下来的钱
month_salary = annual_salary / 12 #每个月的工资
while True:
    time += 1
    current_savings += month_salary * portion_saved + current_savings*r/12  #每个月存下来的钱+之前存下来的钱+之前存下来的钱的利息
    if current_savings >= portion_down_payment:
        break
print("Number of months:",time)
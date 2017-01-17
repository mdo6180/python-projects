#-------------------------------------------------------------------------------
# Name: Minh Quan Do
# G#: G00968110
# Project 1
# Lab Section 223
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Slide 7 of 02.basics.part1.pdf
#-------------------------------------------------------------------------------
# Comments and assumptions: All specifications are met. All tests passed.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#prints openning message
print('Welcome to the Scheduler!')

#inputs name as variable
name = input('What is your name? ')

#inputs number of chocolates,cakes, and ice cream
#used int() to change input from string to integer
choco = int(input('How many chocolates are there in the order? '))
cake = int(input('How many chocolate cakes are there in the order? '))
ice = int(input('How many chocolate ice creams are there in the order? '))

#calculates total time
tt = (choco * 1020) + (cake * 102) + (ice * 127)
#displays total time
print('Total time:',tt,'minutes')

#inputs customer's time
cust_time = int(input('How many minutes do you have before the order is due? '))

#calculates extra time
extra_time = cust_time - tt
#displays extra time
print('Your extra time for this order is',extra_time,'minutes:')

#1440 = number of minutes in 1 day
#divide extra_time by 1440 to get number of days
# // used to display whole number quotient
days = extra_time // 1440

#display days
print(days,'days')

# % used to find remainder after days.  
hours = extra_time % 1440
# uses remainding minutes after calculation of days to find hours left. 
# // used to find hours in whole numbers  
hours2 = hours // 60

#displays hours
print(hours2,'hours')

#minutes = remainder of hours
# % used to display remainder of hours
minutes = hours % 60

#displays minutes
print(minutes,'minutes')
#prints final message
print('Thank you,',name+'!')


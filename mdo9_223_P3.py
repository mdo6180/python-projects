#-------------------------------------------------------------------------------
# Name: Minh Quan Do
# G#: G00968110
# Project 3
# Lab Section 223
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: slides 9 and 20 of 05.sequences.part2.pdf
#             slides 22 and 23 of 05.sequences.part1.pdf
#-------------------------------------------------------------------------------
# Comments and assumptions: All specifications are met. All tests passed.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

def count_odd_digits(number):
	#number is converted into a string 
	#this is done in order for it to be broken up and put into a list
	number = str(number)
	
	#empty is created to be later appended
	list = []
	#answer = 0 serves as a placeholder
	answer = 0
	
	#for loop is used to append each element of number into list
	for i in range(len(number)):
		list.append(number[i])
	
	#this for loop is used to evaluate elements of list
	#elements in list are converted back into an integer 
	#then tested to find odd numbers
	#each time an odd number is encountered,
    #value of answer is increased by 1
	for i in range(len(list)):
		if int(list[i]) % 2 == 1:
			answer += 1
	return answer

def prime_divisors(num):	
	
	#empty lists are created to later be appended
	divisor_list = []
	answer_list = []
	
	#function is used to determine prime number
	#2 is the only even prime number so 2 is a good place to begin tests
	#loop divides number by i for when (i = 2) up to (number - 1) 
	#if number is divisible by i, answer is set to false and loop breaks
	#if loop completes all tests, answer is evaluated to false 
	def prime_number(number):
		answer = bool
		for i in range(2, number):
			if number % i == 0:
				answer = False
				break
			else:
				answer = True
		return answer
	
	#loop is used to find whole number divisors of num 
	#divisors are appended to divisor_list
	for i in range(2, num + 1):
		if num % i == 0:
			divisor_list.append(i)
	
	#loop feeds elements of divisor_list into funtion above to be tested
	#if function returns True, that element is appended into answer_list
	#if element is 2, it is automatically appended into answer_list
	for i in range(len(divisor_list)):
		if divisor_list[i] == 2:
			answer_list.append(divisor_list[i])
		elif prime_number(divisor_list[i]) == True:
			answer_list.append(divisor_list[i])
		
	return answer_list

def remove_repeat(msg):
	list = []
	str = ''
	#used a for loop to index msg and append the elements into list.
	#this for loop is used to split the msg string
	for i in range(0, len(msg) + 1):
		if msg[i:i + 1] != msg[(i + 1):(i + 2)]:
			list.append(msg[i:i + 1])
	#use a for loop to pull out the elements of list
	#elements are then concatenated into a string
	for i in range(0, len(list)):
		str += (list[i] + '')
	str = str[:]
		
	return str

def float_range(start,stop,step):
	#all values of start, stop, and step are converted into float
	#empty list is created to be appended later on 
	start = float(start)
	stop = float(stop)
	step = float(step)
	list= []
	
	#if start is less than stop, and step is more than 0, loop can begin 
	#if statement is used to ensure no infinite loops can occur
	#loop begins when i = start, stops at i = stop, and increments by step
	#loop appends i into list
	if (start < stop) and (step > 0):
		i = start
		while i < stop:
			list.append(i)
			i += step
	
	#this loop is used for a negative increment float_range
	if (start > stop) and (step < 0):
		i = start
		while i > stop:
			list.append(i)
			i += step
			
	return list

def replace(xs,old,new,limit):
	#count is defined
	count = 0
	
	#if statement is used to ensure loop only executes if limit > zero
	#loop iterates through entire list of xs
	#if element xs[i] is equal to the value of old, 
	#element xs[i] would be replaced with value of new
	#value of count inreases by 1 each time value of new is inputed into list
	#once the value of count reaches the limit, the loop breaks
	if limit > 0:	
		for i in range(len(xs)):
			if xs[i] == old:
				xs[i] = new
				count += 1
			if count == limit:
				break
			
	return xs

def sum_positive_2d(xss):
	#empty list is created to later be appended
	#zero is used as placeholder for answer 
	list = []
	answer = 0
	#outer loop is used to iterate through xss 
	#nested loop is used to iterate through each element of xss
	#if element xss[i][j] is more than 0, 
	#xss[i][j] is then appended into list
	for i in range(len(xss)):
		for j in range(len(xss[i])):
			if xss[i][j] > 0:
				list.append(xss[i][j])
	#for loop is used to iterate through list
	#the value of list[i] is added to answer
	for i in range(len(list)):
		answer += list[i]
		
	return answer
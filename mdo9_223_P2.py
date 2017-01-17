#-------------------------------------------------------------------------------
# Name: Minh Quan Do
# G#: G00968110
# Project 2
# Lab Section 223
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: slide 7 of 03.branching.pptx
#-------------------------------------------------------------------------------
# Comments and assumptions: All specifications are met. All tests passed.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#inputs the value of the angles and converts them into integers
ang1 = int(input('Please enter the 1st angle: '))
ang2 = int(input('Please enter the 2nd angle: '))
ang3 = int(input('Please enter the 3rd angle: '))

#defines largest, mid, and smallest	
largest = 0
mid = 0
smallest = 0 

#if angle 1 is smaller than angle 2 and angle 3, angle 1 is the smallest angle
if (ang1 <= ang2) and (ang1 <= ang3):
	
	#assigns smallest to the value of angle 1
	smallest = ang1
	
	#since angle 1 has already been determined to be the smallest angle,
	#angle 2 and angle 3 are compared against each other
	if (ang2 <= ang3):
	
		#if angle 2 is less than angle 3, angle 2 is the middle angle
		#and angle 3 is the largest angle
		mid = ang2
		largest = ang3
	else:
		#if angle 2 is not less than angle 3, angle 3 is the middle angle
		#and angle 2 is the largest angle
		mid = ang3
		largest = ang2

#if angle 2 is smaller than angle 3 and angle 1, angle 2 is the smallest angle
if (ang2 <= ang3) and (ang2 <= ang1):
	
	#assigns smallest to the value of angle 2 
	smallest = ang2
	
	#since angle 2 has already been determined to be the smallest angle,
	#angle 1 and angle 3 are compared against each other
	if (ang1 <= ang3):
	
		#if angle 1 is less than angle 3, angle 1 is the middle angle
		#and angle 3 is the largest angle
		mid = ang1
		largest = ang3
	else:
		#if angle 3 is not less than angle 1, angle 3 is the middle angle
		#and angle 1 is the largest angle
		mid = ang3
		largest = ang1

#if angle 3 is smaller than angle 1 and angle 2, angle 3 is the smallest angle
if (ang3 <= ang1) and (ang3 <= ang2):
	
	#assigns smallest to the value of angle 2 
	smallest = ang3
	
	#since angle 3 has already been determined to be the smallest angle,
	#angle 1 and angle 2 are compared against each other
	if (ang1 <= ang2):
		
		#if angle 1 is less than angle 2, angle 1 is the middle angle
		#and angle 2 is the largest angle
		mid = ang1
		largest = ang2
	else:
		#if angle 2 is not less than angle 1, angle 2 is the middle angle
		#and angle 1 is the largest angle
		mid = ang2
		largest = ang1

#prints list of angles
print('\nList of angles:',smallest,mid,largest)

#all the angles of a triangle must add up to 180 degrees 
#no angles can equal to 0 or negative
#therefore the bool operator, not, is used to evaluate any angle that is 
#negative or equal to 0 false  
if ((ang1 + ang2 + ang3) == 180) and not((ang1 and ang2 and ang3) <= 0):
	
	#all angles of equilateral triangles are 60 degrees 
	if ang1 == 60 & ang2 == 60 & ang3 ==60:
		print('This is an acute equiangular triangle!\n')
	
	#a triangle with any side that equals 90 degrees
	#is either a right triangle or a right isosceles triangle
	elif (ang1 == 90) or (ang2 ==90) or (ang3 == 90):
		
		#if the isosceles triangle has any side that equals 90 degrees
		#then the triangle is a right isosceles triangle 
		if (ang1 == ang2) or (ang1 == ang3) or (ang2 == ang3):
			print('This is a right isosceles triangle!\n')
		else:
			print('This is a right triangle!\n')
	
	#if a triangle has 2 equal angles, that triangle is an isosceles triangle
	elif (ang1 == ang2) or (ang1 == ang3) or (ang2 == ang3):
		
		#if the isosceles triangle has one side that is more than 90 degrees
		#that triangle is an obtuse isosceles triangle
		if (ang1 > 90) or (ang2 > 90) or (ang3 > 90):
			print('This is an obtuse isosceles triangle!\n')
		
		#if the isosceles triangle has one side that is less than 90 degrees
		#that triangle is an acute isosceles triangle
		elif (ang1 < 90) or (ang2 < 90) or (ang3 < 90):
			print('This is an acute isosceles triangle!\n')
		
	#an obtuse triangle only has to have at least one side 
	#that is more than 100 degrees
	elif (ang1 > 90) or (ang2 > 90) or (ang3 > 90):
		print('This is an obtuse triangle!\n')
	
	#by this point, all types of triangles have been defined
	#so whatever combination of angles that is left has to be an acute triangle
	else:
		print('This is an acute triangle!\n')
#any triangle that does not have all its angles add up to 180, 
#or has a negative angle, or a 0 degree angle, is not a triangle
else:
	print('This is not a triangle!\n')
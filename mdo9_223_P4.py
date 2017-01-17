#-------------------------------------------------------------------------------
# Name: Minh Quan Do
# G#: G00968110
# Project 4
# Lab Section 223
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: 06.functions.part1.pdf, 06.functions.part2.pdf 
#-------------------------------------------------------------------------------
# Comments and assumptions: All specifications are met. All tests passed.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#build_empty_board passed all tests
def build_empty_board(size):
	#False is appended into another_list
	#another_list is appended into list
	
	list = []
	another_list = []
	for i in range(size):
		another_list.append(False)
		list.append(another_list)
	return list

#build_board passed all tests
def build_board(coords, size):
	#test function used to test for negative values
	#if any x or y value is less than zero, value is set to False
	def test(num):
		value = True
		for i in coords:
			if (i[0] < 0) or (i[1] < 0):
				value = False
				break
		return value
	
	#if statment is used to determine whether to run tests or not
	if test(coords) == False:
		answer = None
	else:
		#build_small_board function is used to create a list of False values
		def build_small_board(num):
			small_list = []
			for i in range(num):
				small_list.append(False)
			return small_list
		#x_list is appended with x coordinates 
		x_list = []
		for i in coords:
				x = i[0]
				x_list.append(x)
		
		#for loop is used to modify true values into small_board
		#append_list is appended with modified small_board lists
		append_list = []
		for i in coords:
				small_board = build_small_board(size)
				y = i[1]
				small_board[y] = True
				append_list.append(small_board)
		
		#empty_board function creates empty board
		
		
		#empty board is created with dimensions of size
		#for loop takes x-coordinates from x_list 
		#Replaces the indexed value in answer with value in append_list
		#Code works because indexes of x-coordinates in x_list 
		#match up with values in append_list
		answer = build_empty_board(size)
		for i in range(len(x_list)):
			answer[x_list[i]] = append_list[i]
	
	return answer

#is_square passed all tests	
def is_square(board):
	#checks to see if the board should be tested
	if len(board) > 0:
		#rows and answer is defined
		#compare is set to length of zero-element of board 
		#because all elements after board[0] will have the same length
		rows = 0
		answer = bool
		compare = len(board[0])
		
		#for loop iterates through board
		#if elements = compare, element is a valid row
		#1 is added to rows to count the number of valid rows
		#if an element is not equal to length of board element zero, 
		#answer set to false, and loop breaks
		for i in range(len(board)):
			if len(board[i]) == compare:
				rows += 1
			else:
				answer = False
				break
		
		#if the number of rows = the length of zero-element of board
		#answer is set to True, otherwise answer is set to false
		if rows == compare:
			answer = True
		else:
			answer = False
			
	#for special case length of board = 0, answer = True 
	#otherwise answer = false, answer is returned
	elif len(board) == 0:
		answer = True
	else:
		answer = None
		
	return answer

#get_size passed all tests	
def get_size(board):
	#if is_square is evaluated to True, 
	#board_size is set to length of board and board_size is returned
	#otherwise board_size is set to None
	if is_square(board) == True:
		board_size = len(board)
	else:
		board_size = None
		
	return board_size

#get_coords passed all tests	
def get_coords(s):
	#defines x_coord, y_coord, and coordinate_list
	x_coord = 0
	y_coord = 0
	coordinate_list = []
	
	#i is row and j is column
	#coordinate is tuple with values x_coord and y_coord
	#tuple is then appended into coordinate_list
	for i in range(len(s)):
		for j in range(len(s)):
			if s[i][j] == True:
				x_coord = i
				y_coord = j
				coordinate = (x_coord,y_coord)
				coordinate_list.append(coordinate)
				
	return coordinate_list


#show_board passed all tests
def show_board(board, queen = 'Q', empty = '-'):
	#substr is defined as empty string
	substr = ''
	
	#if index i[j] of board is true
	#if board[i][j] is True, board[i][j] = queen or 'Q'
	#if board[i][j] is False, board[i][j] = empty or '-'
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == True:
				board[i][j] = queen
			
			elif board[i][j] == False:
				board[i][j] = empty
		#string is then joined together and set to value of substr
		substr += ''.join(board[i]) + '\n'
	return substr
	
#row_conflict passed all tests	
def row_conflict(board, r):
	#conflict is set to False as default
	#get_coords function is used to obtain list of coordinates
	#list of coordinates is then set equal to Q_coords
	#row_values is defined as empty list
	conflict = False
	Q_coords = get_coords(board)
	row_values = []
	
	#x-coordinates of Q_coords is appended into row_values
	for i in Q_coords:
		row_values.append(i[0])
		
	#loops through row_values to see if element in row_values equal r
	#if element is equal to r, value of conflict is changed to True
	for i in range(len(row_values)):
		if row_values[i] == r:
			conflict = True
			break
	return conflict


#column_conflict passed all tests
def column_conflict(board, c):
	#conflict is set to False as default
	#get_coords function is used to obtain list of coordinates
	#list of coordinates is then set equal to Q_coords
	#column_values is defined as empty list
	conflict = False
	Q_coords = get_coords(board)
	column_values = []
	
	#y-coordinates of Q_coords is appended into row_values
	for i in Q_coords:
		column_values.append(i[1])
		
	#loops through column_values to see 
	#if an element in column_values is equal to r
	#if element is equal to r, value of conflict is changed to True
	for i in range(len(column_values)):
		if column_values[i] == c:
			conflict = True
			break
	return conflict


#diagonal_conflict passed all tests	
def diagonal_conflict(board,r,c):
	#get_coords function is used to obtain a list of coordinates
	#list of coordinates is then appended to check
	check = get_coords(board)
	
	#tup is defined as empty tuple
	#if statement used to check for square, 
	#single-element lists and set ans to True
	#in order to determine diagonal conflict
	#loop is used to add or subtract column and row by 1 
	#tup is then defined as tuple containing variables row and column
	#check to see if tup is in list of coordinates
	
	#right_down used to determine diagonal conflict 
	#in downward right direction
	def right_down(row,column):
		
		tup = ()
		if (row,column) in check:
			ans = True
		else:
			for i in range(len(board)):
				column += 1
				row += 1
				tup = (row,column)
				if tup in check:
					ans = True
					break
				else:
					ans = False
		return ans
	
	#left_up is used to determine diagonal conflict 
	#in the upward left direction
	def left_up(row,column):	
		
		tup = ()
		if (row,column) in check:
			ans = True
		else:
			for i in range(len(board)):
				column -= 1
				row -= 1
				tup = (row,column)
				if tup in check:
					ans = True
					break
				else:
					ans = False
		return ans
	
	#right_up is used to determine diagonal conflict 
	#in the upward right direction
	def right_up(row,column):
		
		tup = ()
		if (row,column) in check:
			ans = True
		else:
			for i in range(len(board)):
				column += 1
				row -= 1
				tup = (row,column)
				if tup in check:
					ans = True
					break
				else:
					ans = False
		return ans
	
	#left_down is used to determine diagonal conflict 
	#in the downward left direction
	def left_down(row,column):
		
		tup = ()
		if (row,column) in check:
			ans = True
		else:
			for i in range(len(board)):
				column -= 1
				row += 1
				tup = (row,column)
				if tup in check:
					ans = True
					break
				else:
					ans = False
		return ans
	
	#answer is set default to False
	#first if statement used to check 
	#for negative row or column values
	#second if statement used to check 
	#for diagonal conflict in all four directions
	answer = False
	if (r >= 0) or (c >= 0):
		if (left_down(r,c) == True) or (right_down(r,c) == True) or (right_up(r,c) == True) or (left_up(r,c) == True):
			answer = True
			
	return answer

#is_solved passed all tests
def is_solved(board):

	#counts the number of queens
	#for each iteration, count() is used to count queens in element
	def Q_count(list):
		var = 0
		for i in list:
			var += i.count(True)
		return var
		
	ans = bool
	#checks to see if board is not square using is_square function
	if is_square(board) == False:
		ans = False
		
	else:
		#used get_coords to obtain a list of coordinates
		Q_coords = get_coords(board)
		
		#makes a list of all the row values
		row_values = []
		for i in Q_coords:
			row_values.append(i[0])
		
		#makes a list of all the column values
		column_values = []
		for i in Q_coords:
			column_values.append(i[1])
		
		#tests for row conflict 
		#by counting the occurences of row values
		def row_conflict_test(a):
			for i in range(len(row_values)):
				a = row_values.count(row_values[i])
				if a > 1:
					conflict = True
					break
				else:
					conflict = False
			return conflict
		
		#tests for column conflict 
		#by counting the occurences of column values
		def column_conflict_test(b):
			for i in range(len(column_values)):
				a = column_values.count(column_values[i])
				if a > 1:
					conflict = True
					break
				else:
					conflict = False
			return conflict
		
		#tests for diagonal conflict 
		#using diagonal_conflict function
		def diagonal_conflict_test(c):
			for i in Q_coords:
				row = i[0]
				column = i[1]
				c[row][column] = False
				if diagonal_conflict(c,row,column) == True:
					conflict = True
					break
				else:
					conflict = False
			return conflict		
	#is_square function is used to determine if board is a square
	if is_square(board) == False:
		answer = False
	
	else:
		#checks to see if number of queens 
		#is at least equal to the size of the board 
		#checks to see if there no row conflicts, 
		#or column conflicts, or diagonal conflicts
		if (Q_count(board) >= len(board)) and (row_conflict_test(board) == False) and (column_conflict_test(board) == False) and (diagonal_conflict_test(board) == False):
			answer = True
	
		else: 
			answer = False
	
	return answer

#place_one passed all tests	
def place_one(board,r,c):
	
	#checks to determine if coordinates 
	#are not negative and within the board
	if (r > len(board)) or (c > len(board)) or (r < 0) or (c < 0):
		answer = False
	else:
		
		if (column_conflict(board, c) == False) and (row_conflict(board, r) == False) and (diagonal_conflict(board, r, c) == False):
			board[r][c] = True
			answer = True
		else:
			answer = False
	return answer
	
#remove_one passed all tests
def remove_one(board, r, c):
	#determine if coordinates are not negative and within the board
	#if coordinates are negative or not within the board, answer = False 
	if (r > len(board)) or (c > len(board)) or (r < 0) or (c < 0):
		answer = False
	else:
		#if the coordinate in row r and column c of board is true
		#answer is set to True, board[r][c] is set to false and returned
		if board[r][c] == True:
			answer = True
			board[r][c] = False
		else:
			answer = False
	return answer
#-------------------------------------------------------------------------------
# Name: Minh Quan Do
# G#: G00968110
# Project 4
# Lab Section 223
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: 08.classes.part2.pdf, 08.classes.part1.pdf, Lab_12.pptx
#-------------------------------------------------------------------------------
# Comments and assumptions: All specifications are met. All tests passed.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

class GPS_Location:
	#instance variables created
	def __init__(self,x,y):
		#raises GPS_Error if x or y is less than 0
		if (x < 0) or (y < 0):
			raise GPS_Error("GPS_Location error: coordinate cannot be negative")
		self.x = x 
		self.y = y 
		
	def __str__(self):
		#.format() used to format string
		return '({},{})'.format(self.x,self.y)
		
	def __repr__(self): 
		#.format() used to format string
		return 'GPS_Location({},{})'.format(str(self.x),str(self.y))
		
	def __eq__(self,other):
		if str(other) == str(self):
			return True
		else:
			return False
			
	def dist(self,other):
		#(x2 - x1) + (y2 - y1)
		#other is coordinate 2, self is coordinate 1
		x_dist = abs(other.x - self.x)
		y_dist = abs(other.y - self.y)
		distance = x_dist + y_dist
		return distance

class GPS_POI:
	#instance variables created
	def __init__(self,location,name,kind):
		self.location = location
		self.name = name
		self.kind = kind
	
	def __str__(self):
		#.format() used to format string
		return '{}: {}, {}'.format(GPS_Location.__str__(self.location),self.name,self.kind)
		
	def __repr__(self):
		#.format() used to format string
		a = GPS_Location.__repr__(self.location)
		return "GPS_POI({},'{}','{}')".format(a,self.name,self.kind)
	
class GPS:
	def __init__(self,current,map = None):
		#instance variables created
		self.current = current
		self.map = map
		self.route = []
		if map == None:
			self.map = []
			#raise GPS_Error("gps_error('gps error')")
			
	def relocate(self,location):
		#sets current location equal to location
		self.current = location
		
	def add_dest(self,location): 
		#appends location coordinates to route
		self.route.append(location)
	
	def drop_dest(self,location): 
		#raises GPS_Error if location is not in route
		#else it removes location
		if location not in self.route:
			raise GPS_Error('GPS drop_dest error: not in route')
		else:
			self.route.remove(location)
	
	def arrive_first(self):
		#raises GPS_Error if no coordinates in route
		#sets self.current equal to 1st element in self.route
		#then it deletes the first element of self.route
		if self.route == []:
			raise GPS_Error('GPS arrive error: empty route')
		self.current = self.route[0]
		del self.route[0]
		
	def display_map(self): 
		#returns '' if no coordinates were inputted to self.map
		if self.map == None:
			return ''
		else:
			#string concatenation used to make map
			map_str = ''
			for i in self.map:
				map_str += (GPS_POI.__str__(i) + '\n')
			return map_str
	
	def display_route(self): 
		#if route is empty, return ''
		if self.route == []:
			return ''
		else:
			#string concatenation used to make string
			#.format() is used to input current location 
			#returns current location and route_str spliced from 0 to 2nd to last element
			#this is done to avoid the dash at the end 
			route_str = ''
			for i in self.route:
				route_str += GPS_Location.__str__(i) + '-'
			return '{}-'.format(GPS_Location.__str__(self.current)) + route_str[0:-1]
			
	def dist_to_travel(self):
		#self.add_dest is appended to self.route 
		#when self.add_dest is appended, 
		#the last value in the list cannot be inputted because it's the current location
		#therefore the last value in self.route is deleted
		#current location (self.current) is then inserted at element 0
		
		#for loop uses dist method in GPS_Location class to find distance between i and i + 1
		#the distance is then added to a_b
		
		self.route.append(self.add_dest)
		del self.route[-1]
		self.route.insert(0,self.current)
		
		a_b = 0
		for i in range(len(self.route) - 1):
			a_b += GPS_Location.dist(self.route[i + 1],self.route[i])
		return a_b
	
	def search_name_kind(self,name,kind):
		#if map equals None, [] is returned
		#else, if attributes name and kind match, i is appended to list
		if self.map == None:
			return []
		else:
			list = []
			for i in self.map:
				if (i.name == name) and (i.kind == kind):
					list.append(i)
			return list
			
	def search_within_dist(self,dist,kind=None):
		#if no values are in map, function automatically returns []
		#if kind is not inputted, for loop only finds locations based on distance
		#if kind is inputted, for loop finds locations based on kind and distance
		
		if (self.map == None):
			return []
			
		elif kind == None:
			list = []
			for i in self.map:
				if (GPS_Location.dist(self.current,i.location) <= dist):
					list.append(i)
			return list
			
		else:
			list = []
			for i in self.map:
				if (i.kind == kind) and (GPS_Location.dist(self.current,i.location) <= dist):
					list.append(i)
			return list
	
	def closest_kind(self,kind):
		#if no values in map, function automatically returns []
		if (self.map == None):
			return []
		else:
			#for loop loops through self.map to find locations that match kind
			#if locations match kind, i is appended to list
			list = []
			for i in self.map:
				if (i.kind == kind):
					list.append(i)
			
			if list == []: #if no locations match kind, function returns []
				return []
			else:
				#dictionary used to associate locations with distance
				#keys are GPS_POI, values are distance
				database = {}
				for i in list:
					database[i] = GPS_Location.dist(self.current,i.location)
				
				#min() used to find shortest distance
				smallest = min(database.values()) 
				
				#for loop loops through list to find locations with distances equal to smallest distance
				answer = []
				for i in list:
					if GPS_Location.dist(self.current,i.location) == smallest:
						answer.append(i)
				return answer

class GPS_Error(Exception): 						
	def __init__(self,msg):
		self.msg = msg
	def __str__(self):
		return self.msg
	def __repr__(self):
		#.format() used to format string
		return "GPS_Error('{}')".format(self.msg)
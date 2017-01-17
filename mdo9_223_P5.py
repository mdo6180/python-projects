def read_file(filename):
	f = open(filename)
	text = f.readlines()
	p_db = {}
	for i in range(1, len(text)):
		x = text[i].split('","')
		for j in x:
			pres = x[0].strip('"')
			year_inaug = int(x[1].strip('"'))
			in_office = int(x[2].strip('"'))
			age = int(x[3].strip('"'))
			state = x[4]
			party = (x[5].strip("\n"))
			tup = (year_inaug,in_office,age,state.strip('"'),party.strip('"'))
		p_db[pres] = tup
	
	return p_db
	
def youngest_at_inauguration(p_db):
	#inauguration age is appended to list and database
	#database is dictionary with president's name as keys and age as values
	list = []
	database = {}
	for keys, values in p_db.items():
		list.append(values[2])
		database[keys] = values[2]
	
	#list is sorted
	sorted_list = sorted(list)
	
	#ensures that age is youngest in case of a tie
	age = min(sorted_list)
	
	#if president's age is equal to variable age, his name is appended to names
	names = []		
	for keys in database.keys():
		if database[keys] == age:
			names.append(keys)
	
	#name is sorted in alphabetical order 
	#tuple of age and a list of the presidents is returned
	names = sorted(names)
	answer = (age, names)
	return answer
	
def oldest_at_retirement(p_db):
	#age at retirement is age at inauguration plus number of years in office
	#retirement age is appended to list and database
	#database is dictionary with president's name as keys and age as values
	
	list = []
	database = {}
	for keys, values in p_db.items():
		list.append(values[2] + values[1])
		database[keys] = (values[2] + values[1])
	
	#max() is used to find oldest age
	age = max(list) 	
	
	#if president's age is equal to variable age, his name is appended to names
	names = []		
	for keys in database.keys():
		if database[keys] == age:
			names.append(keys)
	
	#name is sorted in alphabetical order 
	#tuple of age and a list of the presidents is returned
	names = sorted(names)
	answer = (age, names)
	return answer

def presidents_by_state(p_db, state):
	#if president's state is equal to variable state,
	#his name is inputted as key and information is inputted as value into dictionary
	dictionary = {}
	for keys, values in p_db.items():
		if values[3] == state:
			dictionary[keys] = values
			continue
	return dictionary
	
def presidents_by_party(p_db, party):
	#if president's party is equal to variable party,
	#his name is inputted as key and tuple is inputted as value into dictionary
	dictionary = {}
	for keys, values in p_db.items():
		if values[4] == party:
			dictionary[keys] = values
			continue
	return dictionary

def avg_unemployment_for_month(u_db, month):
	#ensures that month is valid
	#month cannot have index of 12 because that would mean there are 13 months
	#if month is valid, code proceeds
	#each value in u_db is indexed for that particular month 
	#unemployment calculated by adding up all unemployment statistic of that month 
	#number of months is counted in order to calculate average
	if (month < 0) or (month > 11):
		return None
	else:
		unemployment = 0
		num_months = 0
		for values in u_db.values():
			unemployment += values[month]
			num_months += 1
		
		answer = unemployment//num_months
		return answer

def total_unemployment_for_year(u_db, year):
	#ensures year is in u_db
	#if year in u_db, value of that year is pulled out and set to data
	#answer is calculated by adding up all values of data 
	if year not in u_db:
		return None
	else:
		data = u_db[year]
		answer = 0
		for i in data:
			answer += i
		return answer

def avg_unemployment_for_president(p_db,u_db,president):
	#ensures president in p_db
	if president not in p_db:
		return None
	
	#last_year is inauguration year + number of years in office
	#for loop used to create a list of years in office
	year_inaug = p_db[president][0]
	in_office = p_db[president][1]
	last_year = year_inaug + in_office
	list = []
	
	for i in range((year_inaug),last_year):
		list.append(i)
	
	#function is used to ensure every year in list is in u_db
	def valid(years_list,dictionary):
		for i in years_list:
			if i not in dictionary:
				return None
			else:
				result = years_list
		return result
	
	#if any years in list is not in u_db, None automatically returned
	if valid(list,u_db) == None:
		return None
		
	#avg is appended with average of each year 
	#n is average of all years 
	avg = []
	for i in list:
		avg.append(sum(u_db[i])/len(u_db[i]))

	n = sum(avg) // len(list)
	return n

def unemployment_change_for_president(p_db,u_db,president):
	#year_inaug = p_db[president][0]
	#start_value = u_db[year_inaug][0]
	#year_retire = (p_db[president][0] + (p_db[president][1] - 1))
	#if inauguration year or retirement	year not in u_db or president not in p_db None is returned
	#None has to be returned before anything else to avoid errors 
	if (president not in p_db.keys()) or (p_db[president][0] not in u_db.keys()) or ((p_db[president][0] + (p_db[president][1] - 1)) not in u_db.keys()):
		return None
	else:
		#start_value is first month of inauguration
		#end_value is last month of retirement year
		year_inaug = p_db[president][0]
		start_value = u_db[year_inaug][0]
		year_retire = (p_db[president][0] + (p_db[president][1] - 1))
		end_value = u_db[year_retire][11]
		change_unemployment = end_value - start_value
		return change_unemployment
		
def president_lowest_avg_unemployment(p_db,	u_db):
	#pres_unemployed is dictionary with presidents as keys and his unemployment rate as values
	#his unemployment rate is calculated by calling avg_unemployment_for_president
	pres_unemployed = {}
	for keys in p_db.keys():
		pres_unemployed[keys] = avg_unemployment_for_president(p_db,u_db,keys)
	
	#if unemployment rate can be calculated, unemployment rate is appended to avg 
	avg = []
	for values in pres_unemployed.values():
		if values != None:
			avg.append(values)
	
	#if there are no values in avg, None is returned
	#else, min() used to find smallest unemployment rate 
	if avg == []:
		return None
	else:
		min_avg = min(avg)
	
	#for loop used to find president's name that corresponds to smallest unemployment rate
	#tuple is created and returned
	for keys in pres_unemployed.keys():
		if pres_unemployed[keys] == min_avg:
			tuple = (keys,min_avg)
			break
	return tuple
	
def president_lower_unemployment_most(p_db,	u_db):
	#pres_unemployed is dictionary with president as keys and change of unemployment as values
	#change of unemployment is calculated by calling unemployment_change_for_president
	pres_unemployed = {}
	for keys in p_db.keys():
		pres_unemployed[keys] = unemployment_change_for_president(p_db,u_db,keys)
		
	#change in unemployment has to less than 0 and calculated in order to be appended to change
	change = []
	for values in pres_unemployed.values():
		if (values != None) and (values < 0):
			change.append(values)
	
	#if no values is change, None automatically returned
	#else min_change is set to smallest value of change
	if change == []:
		return None
	else:
		min_change = min(change)
	
	#for loop used to find president with value equal to min_change
	for keys in pres_unemployed.keys():
		if pres_unemployed[keys] == min_change:
			tuple = (keys,min_change)
			break
	return tuple
	
def expand_database(p_db, u_db): 
	#tuple is converted to list using list()
	#avg_unemployment_for_president is called to calculate average unemployment rate for each president
	#average unemployment rate is appended to list
	#list converted back into tuple to update p_db
	for keys,values in p_db.items():
		conversion = list(values)
		conversion.append(avg_unemployment_for_president(p_db,u_db,keys))
		p_db[keys] = tuple(conversion)
		
	
	

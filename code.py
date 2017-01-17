alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
change = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

match = str(input('input letter (lowercase): '))
match2 = str(input('input another letter to match (lowercase): '))
message = str(input('input message (all letters lowercase): ')).lower()

tup = (match,match2)

def encoding(tuple):
	letter_dict = {}
	alphabet_index = alphabet.index(tup[0]) 				#index tup
	change_index = change.index(tup[1])
	new_list = change[:(change_index - alphabet_index)]		#saves a copy of letters taken out
	del change[:(change_index - alphabet_index)]			#deletes letters from change list
	final_list = change + new_list							#puts deleted letters at the end of the change list
	for i in range(len(alphabet)):							#returns dictionary with corresponding values
		letter_dict[alphabet[i]] = final_list[i]
	return letter_dict
	
a = encoding(tup)

complete = ''
for i in message:
	if i not in alphabet:
		complete += i
	else:
		complete += a[i]

print(complete)

#search entry

search_dict {}
for line in user_file:
	spiltline = line.spilt(':')
	search_dict[spiltline[0]] = spiltline[1]



print('To search for information in entry one the input format should be: (artist).')
print('To search for information in entry two the input format should be: (artist2.')

search_entry = input('Enter the entry you wish to search for example (artist) or (artist2): ')
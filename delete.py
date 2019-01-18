#delete entry
delete_entry = input('Do your wish to delete database save on your account yes/no: ')

if delete_entry == 'yes':
	os.remove(account_file)
	print('Your account and entry has been deleted')
	print('Thanks for being a valued user of the Music Legend!')

elif delete_entry == 'no':
	print('Your database was not deleted.')
	print('Your are still an authorized user of the Music Legend program.')

	
					
					
					
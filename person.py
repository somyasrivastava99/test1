import random

chars = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,./;'[]!@#$%^&*()_+~\|:"<>?'''
times = int(input('[.]Number of passwords?\n[.]'))
length = int(input('[.]Password length?\n[.]'))

f = open('C:\Users\DELL\Documents\GitHub\test1','w')

for i in range(times):
	password = ''
	for j in range(length):
		password += random.choice(chars)

	print('[.]',password,sep='')
	
	
	password = password + '\n'
	f.write(password)

f.close()
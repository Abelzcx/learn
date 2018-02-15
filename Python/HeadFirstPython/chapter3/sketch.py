import os

if os.path.exists('sketch.txt'):
	data = open('sketch.txt')
	
	for each_line in data:
		if each_line.find(':')>=0:
			(role, line_spoken) = each_line.split(':', 1)
			print(role, end = '')
			print(' said: ', end='')
			print(line_spoken, end='')
		else:
			print(each_line, end = '')
			
	data.close()
else:
	print('The data file is missing!')
	
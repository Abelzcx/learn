movies = ["The Holy Grail", 1975, "Terry Jones& Terry Gilliam", 91,
			["Graham Chapman", ["Michael Palin", "John Cleese",
				"Terry Gilliam", "Eric Idle", "Terry Jones"]]]
				

def print_list(the_list, control_list=[False, False, 0, 1]):
	for each_list in the_list:
		if isinstance(each_list,list):
			if control_list[1]:
				control_list[2]= control_list[2] + control_list[3];
			print_list(each_list,control_list)
		else:
			if control_list[0]:
				for tab_stop in range(control_list[2]):
					print("\t", end='')
			print(each_list)

	
print_list(movies,[True, True, 0, 1])

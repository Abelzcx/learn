movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
			["Graham Chapman", ["Michael Palin", "John Cleese",
				"Terry Gilliam", "Eric Idle", "Terry Jones"]]]

def print_lol(List):
	for each_list in List:
		if isinstance(each_list, list):
			print_lol(each_list)
		else:
			print(each_list)

def print_lol_while(List):
	count = 0
	while count < len(List):
		if isinstance(List[count], list):
			print_lol_while(List[count])
		else:
			print(List[count])
		count = count + 1

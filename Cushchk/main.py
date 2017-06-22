def read_file():	
	quotes= open("/media/sasidhar/DATA/GitHub/Cuschk/Cushchk/Test1.txt")
	contents = quotes.read()
	print(contents)
	quotes.close()

read_file()
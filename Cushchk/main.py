def read_file():	
	quotes= open("/media/sasidhar/DATA/GitHub/Cuschk/Test/Test1")
	contents = quotes.read()
	print(contents)
	quotes.close()

read_file()
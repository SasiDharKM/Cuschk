import urllib.request

def read_file():
	text = open("../Test/Test1")#defining a path
	contents = text.read()
	text.close()
	cuschk(contents)

def cuschk(text):
	con = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text.replace(' ','+'))#replacing <spc> with + to prevent bad requests
	bytes_output = con.read()
	output = bytes_output.decode("utf-8")
	#print(output)
	con.close()
	if 'true' in output:
		print("Are you sure you want to use PROFANE Words...?")
	elif 'false' in output:
		print("The text appears to be FREE from curse words")
	else:
		print("Scan of document is improper")

read_file()
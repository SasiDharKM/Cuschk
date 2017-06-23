import urllib.request

def read_file():
	text = open("../Test/Test1")#defining a path
	contents = text.read()
	print(contents)
	text.close()
	cuschk(contents)

def cuschk(text):
	con = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text.replace(' ','+'))#replacing <spc> with + to prevent bad requests
	output = con.read()
	#print(output)
	con.close()


read_file()
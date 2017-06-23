import urllib.request

def read_file():
	text = open("../Test/Test1")
	contents = text.read()
	print(contents)
	text.close()
	cuschk(contents)

def cuschk(text):
	con = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text.replace(' ','+'))
	output = con.read()
	print(output)
	con.close()


read_file()
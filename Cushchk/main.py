import urllib.request
import argparse as ap

def read_file():
	text = open("../Test/Test1")#defining a path
	contents = text.read()
	text.close()
	cuschk(contents)

def args():
	parser = ap.ArgumentParser(description = 'Take in text to detect curse words', prog = 'cuschk')
	parser.add_argument('-p', '--path', nargs = '?', type = string, const = "../Test/Test1", default="../Test/Test1", 
		help = 'Enter the path to the file to be tested' )
	parser.add_argument('-t', '--text', type = string, default= "Hi", help = 'Enter the raw text to be checked')
	args = parser.parse_args()
	return args.path


def cuschk(text):
	
	#replacing <space> with + to prevent bad requests
	con = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text.replace(' ','+'))
	byte_output = con.read()
	output = bytes_output.decode("utf-8")#decoding the byte object to a string
	#print(output)
	con.close()
	if 'true' in output:
		print("Are you sure you want to use PROFANE Words...?")
	elif 'false' in output:
		print("The text appears to be FREE from curse words")
	else:
		print("Scan of document is improper")

read_file()
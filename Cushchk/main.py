import urllib.request
import argparse as ap

def read_file(input_text):
	text = open(input_text)#defining a path
	contents = text.read()
	text.close()
	cuschk(contents)

def args():
	parser = ap.ArgumentParser(description = 'Take in text to detect curse words', prog = 'cuschk')
	parser.add_argument('-p', '--path', nargs = '?', type = string, const = "../Test/Test1", default="../Test/Test1", 
		help = 'Enter the path to the file to be tested' )
	args = parser.parse_args()
	return args.path


def cuschk(text):
	
	#replacing <space> with + to prevent bad requests
	con = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text.replace(' ','+'))
	byte_output = con.read()
	output = bytes_output.decode("utf-8")#decoding the byte object to a string
	#print(output)
	con.close()
	return output

def main():
	input_text = args() #get the path from the user
	output = read_file(input_text)
	if 'true' in output:
		print("Are you sure you want to use PROFANE Words...?")
	elif 'false' in output:
		print("The text appears to be FREE from curse words")
	else:
		print("Scan of document is improper")


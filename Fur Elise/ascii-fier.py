#!/bin/python
import sys

def convert(a):
	b = []
	for i in a:
		b.append(chr(i))
	
	return b

# Change the value of array here.
if (len(sys.argv) < 2):
	print("usage ./ascii-fier.py <string containing numbers seperated by commas>")
	print("Example: ./ascii-fier.py 45,67,29,117")
	sys.exit()
usr = sys.argv[1]
arr = [i for i in map(int, usr.split(','))]
print(f"Output: {''.join(convert(arr))}")

#!/usr/bin/python

#import sys
#sys.path.insert('path') for importing in its in another folder

'''
testing map, filter, lambda
'''

items = [1, 2, 3, 4, 5]

def sqr(x):
	return x**2

print map(sqr, items)
print filter(lambda x:x**3, items)

if __name__ == "__main__":
	print map(sqr, items)
	print filter(lambda x:x**3, items)
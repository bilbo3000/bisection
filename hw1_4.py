'''
hw1_4.py
This Python program computes the depth a ball is 
submerged when floating in water using bisection
method. 

Author: Dongpu Jin
Date: 9/10/2011
'''

import sys
import math

# Function used to calculate the depth
def f(x):
	return math.pow(x, 3) - 0.165 * math.pow(x, 2) + 3.993 * math.pow(10, -4)

# Start of the bisection method
# x is in (0.1, 11) cm
a = 0.01 
b = 0.11
N = 30 #maximum number of iteration is 30
TOL = 0.001 # tolerance is 10^-3

for i in range(0, N): 
	print "Iteration: %d"%(i + 1)
	a_err = b - a # approximate absolute error
	r_err = (b - a)/a # approximate relative error
	print "Absolute error < %f"%a_err, 
	print "Relative error < %f"%r_err
 
	p = a + (b-a)/2.0 # find middle point p
	if f(p) == 0 or (b-a)/2.0 <= TOL: 
		print "Depth is %f"%p
		sys.exit(0) # Stop
	if(f(a)*f(p) > 0): 
		a = p # update a
	else: 
		b = p # update b

print "Method failed after %d iterations" %N


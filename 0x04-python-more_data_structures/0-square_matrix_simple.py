#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	cpy = []
	
	if matrix == None:
		return
	for row in matrix:
		cpy.append(list(map(square, row)))
	return cpy

def square(x):
	return x*x	

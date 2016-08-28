

def reverse_string(input=''):
	if(type(input) is not str):
		raise ValueError('Not a string')
	return input[::-1]
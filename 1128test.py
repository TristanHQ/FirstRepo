def test(*args):
	print(args)
	return args

print(type(test(1,2,3,4)))

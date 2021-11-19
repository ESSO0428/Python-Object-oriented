# %%
def decorator_function(original_function):
	def wrapped_function(*argss, **kwargss):
		print(argss)
		print('--------------------------------')
		print(kwargss)
		print('--------------------------------')
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*argss, **kwargss)
	return wrapped_function

@decorator_function
def display():
	print('display function ran')

@decorator_function
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('John', 25)
print('=====================================')
display()

# %%
def decorator_function(original_function):
	def wrapped_function():
		"""
		print(args)
		print('--------------------------------')
		print(kwargs)
		print('--------------------------------')
		"""
		print('wrapper executed this before {}'.format(original_function.__name__))
		original_function
		# return original_function(*args, **kwargs)
	return wrapped_function

@decorator_function
def display():
	print('display function ran')

display()

# %%
def decorator_function(original_function):
	def wrapped_function(*args, **kwargs):
		print(args)
		return(args)
	return wrapped_function
print(decorator_function(('hellow', 'test')))
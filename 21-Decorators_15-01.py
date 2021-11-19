# %%
def be_polit(fn):
	def wrapper():
		print('what a pleasure to meet you !')
		fn()
		print('Have a great day !')
	return wrapper
@be_polit
def great():
	print('My name is Thomas.')

great()

# %%
def be_polit(fn):
	def wrapper():
		print('what a pleasure to meet you !')
		fn()
		print('Have a great day !')
	return wrapper

def great():
	print('My name is Thomas.')

# great()
great = be_polit(great)
great()
# %%[markdown]
# # @property
# %%
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age

	@property
	def age(self):
		return self._age

superstar = Human('Thomas', 'Wei', 18)
print(superstar.age)
# %%[markdown]
# # @attribue.setter
# %%
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age
	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self, value):
		self._age = value

superstar = Human('Thomas', 'Wei', 18)
superstar.age = 19
print(superstar.age)
# %%
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self._age = age
	@property
	def age(self):
		return self._age
	
	@property
	def full_name(self):
		return f'{self.first} {self.last}'
	
	@age.setter
	def age(self, value):
		self._age = value

	@full_name.setter
	def full_name(self, value):
		self.first, self.last = value.split(' ')

superstar = Human('Thomas', 'Wei', 18)
superstar.full_name = 'David Wang'
print(superstar.age)
print(superstar)
print(superstar.__dict__)
# %%[markdown]
# # 繼承 (Inheritance)
# * ## 直接繼承 (不新增任何屬性)
# * ## `__init__`
# * ## super()
# %%
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

class Cat(Animal):
	pass
a_cat = Cat('apple', 'male')
print(a_cat.name)
# %%
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		Animal.__init__(self, name, species)
		self.breed = breed
		self.toy = toy

a_cat = Cat('apple', 'male', 'beef', 'panda')
print(a_cat.name, a_cat.species, a_cat.breed, a_cat.toy)
# %%
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

class Cat(Animal):
	def __init__(self, name, species, breed, toy):
		super().__init__(name, species)
		self.breed = breed
		self.toy = toy

a_cat = Cat('apple', 'male', 'beef', 'panda')
print(a_cat.name, a_cat.species, a_cat.breed, a_cat.toy)
# %%
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species = 'Cat')
		self.breed = breed
		self.toy = toy

a_cat = Cat('apple', 'beef', 'panda')
print(a_cat.name, a_cat.species, a_cat.breed, a_cat.toy)
# %%[markdown]
# # 多重繼承
# %%
class Aquatic:
	def __init__(self, name):
		print('AQUATIC INIT')
		self.name = name
	def swim(self):
		return f'{self.name} is swiming'
	def great(self):
		return f'I am {self.name} of the sea !'

class Ambulatory:
	def __init__(self, name):
		print('AMBULAOTRY INIT')
		self.name = name
	def walk(self):
		return f'{self.name} is walking'
	def greet(self):
		return f'I am {self.name} of the land !'
	
class Penguin(Ambulatory, Aquatic):
	def __init__(self, name):
		print('PENGUIN INIT')
		super().__init__(name = name)

a_penguin = Penguin('Hello')
print(a_penguin.swim())
print(a_penguin.walk())
# %%
class Aquatic:
	def __init__(self, name):
		print('AQUATIC INIT')
		self.name = name
	def swim(self):
		return f'{self.name} is swiming'
	def great(self):
		return f'I am {self.name} of the sea !'

class Ambulatory:
	def __init__(self, name):
		print('AMBULAOTRY INIT')
		self.name = name
	def walk(self):
		return f'{self.name} is walking'
	def greet(self):
		return f'I am {self.name} of the land !'
	
class Penguin(Aquatic, Ambulatory):
	def __init__(self, name):
		print('PENGUIN INIT')
		super().__init__(name = name)

a_penguin = Penguin('Hello')
print(a_penguin.swim())
print(a_penguin.walk())
# %%[markdown]
# # MRO (Method Resolution Order)
# %%
class A:
	def do_something(self):
		print('Method Defined in A')
class B(A):
	def do_something(self):
		print('Method Defined in B')
class C(A):
	def do_something(self):
		print('Method Defined in C')
class D(B, C):
	def do_something(self):
		print('Method Defined in D')

d = D()

d.do_something()

print(D.__mro__)
print(D.mro())
# %%
class A:
	def do_something(self):
		print('Method Defined in A')
class B(A):
	def do_something(self):
		print('Method Defined in B')
class C(A):
	def do_something(self):
		print('Method Defined in C')
class D(B, C):
	pass
	#def do_something(self):
	#	print('Method Defined in D')

d = D()

d.do_something()

print(D.__mro__)
print(D.mro())
help(D)
# %%
class A:
	def do_something(self):
		print('Method Defined in A')
class B(A):
	def do_something(self):
		print('Method Defined in B')
class C(A):
	def do_something(self):
		print('Method Defined in C')
class D(C, B):
	pass
	#def do_something(self):
	#	print('Method Defined in D')

d = D()

d.do_something()

print(D.__mro__)
print(D.mro())
help(D)
# %%
class A:
	def do_something(self):
		print('Method Defined in A')
class B(A):
	def do_something(self):
		print('Method Defined in B')
class C(A):
	'''def do_something(self):
		print('Method Defined in C')'''
	pass
class D(C, B):
	pass
	#def do_something(self):
	#	print('Method Defined in D')

d = D()

d.do_something()

print(D.__mro__)
print(D.mro())
help(D)
# %%
class A:
	def do_something(self):
		print('Method Defined in A')
class B(A):
	'''def do_something(self):
		print('Method Defined in B')'''
	pass
class C(A):
	'''def do_something(self):
		print('Method Defined in C')'''
	pass
class D(C, B):
	pass
	#def do_something(self):
	#	print('Method Defined in D')

d = D()

d.do_something()

print(D.__mro__)
print(D.mro())
help(D)
# %%[markdown]
# # 複寫 (`__add__`)
# %%
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
	
	def __repr__(self):
		return f'Human named {self.first} and {self.last}'
	
	def __add__(self, other):
		if isinstance(other, Human):
			return Human(first = 'NewBorn', last = self.last, age = 0)

		return "You can't add that !"


superstar = Human('Thomas', 'Wei', 18)
superstarplus = Human('Thomas', 'Wei', 18)

new_superstar = superstar + superstarplus

print(new_superstar.first)

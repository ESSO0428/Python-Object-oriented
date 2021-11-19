# %%
class SomeClass:
	pass
some_thng = SomeClass()
# %%[markdown]
# # 基本用法 (初始化 & 定義屬性 & 呼叫)
# %%
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		self.name = 'Hello'
		# private 寫法 (限定該屬性不能修改，實際上可以 [約定成俗的寫法])
		self._nam = 'Heo'
		self.__name = 'lol'
user1 = User('Joe', 'Smith', 68)
print(user1.last)
print(user1.name)
print(user1._nam)
# 如上所述，這個 private 還是可以修改內容
user1._nam = 'Hello World'
print(user1._nam)
# print(user1.__name) # erro
print(user1._User__name)
user1._User__name = 'lolllllllllllll'
print(user1._User__name)

# %%[markdown]
# # 基本用法 (定義方法 & 呼叫方法)
# %%
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f'{self.first} {self.last}'
	def likes(self, thing):
		return f'{self.first} likes {thing}'
	
user1 = User('Joe', ' Smith', 68)
print(user1.full_name())
print(user1.likes('Music'))
# %%
class User:
	active_users = 0

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def full_name(self):
		return f'{self.first} {self.last}'
	def likes(self, thing):
		return f'{self.first} likes {thing}'
	
# active_users 該屬性 將會在底下引用時共用記憶體位置
# 引用第 1 次 active_users : 0 + 1 = 1
user1 = User('Joe', ' Smith', 68)
# 引用第 2 次 active_users : 上次引用的值 (1)  + 1 = 2
user2 = User('David', 'Tao', 40)

print(User.active_users)
print(user1.active_users)
print(user2.active_users)

# 這裡 user1 重新定義 active_users
# 1. user1.active_users 的 值 改變
# 2. user1.active_users  的 記憶體外置也改變
# 3. 其他物件的 active_users 值不改變 (user1 的 .. 改變)
user1.active_users = 300

user1.sex = 'male'
print(user1.sex)

print('################################')
print(User.active_users)
print(user1.active_users)
print(user2.active_users)
# %%[markdown]
# # 限制屬性值定義
# %%
class Pet:
	allowed = ['cat', 'dog', 'fish', 'rat']

	def __init__(self, name, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet !")
		self.name = name
		self.species = species

	def set_species(self, species):
		if species not in Pet.allowed:
			raise ValueError(f"You can't have a {species} pet !")
		self.species = species

cat = Pet('Blue', 'cat')
dog = Pet('Wyatt', 'dog')

print(dog.allowed)
print(Pet.allowed)
print('{}, {}'.format(cat.name, cat.species))
print('{}, {}'.format(dog.name, dog.species))
# %%[markdown]
# # @classmethod
# %%
class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		# cls 即 classmethod 想要定義的簡稱
		return f'There are currently {cls.active_users} active_users !'

	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(',')
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		self.__nickname = 'Jo Jo'
		User.active_users = 1

	def full_name(self):
		return f'{self.first} {self.last}'

	def likes(self, thing):
		return f'{self.first} likes {thing}'

user1 = User('Joe', 'Smith', 68)
user2 = User('David', 'Tao', 40)
user3 = User.from_string('Helen,Wang,68')
print(user3.first, user3.last, user3.age)
# %%
class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		# cls 即 classmethod 想要定義的簡稱
		return f'There are currently {cls.active_users} active_users !'

	@classmethod
	def from_string(cls, data_str):
		first, last, age = data_str.split(',')
		return cls(first, last, int(age))
	
	# string representation
	#""" please print(user1)
	def __repr__(self):
		return f'{self.first} is my name'
	#"""

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		self.__nickname = 'Jo Jo'
		User.active_users = 1

	def full_name(self):
		return f'{self.first} {self.last}'

	def likes(self, thing):
		return f'{self.first} likes {thing}'

user1 = User('Joe', 'Smith', 68)
user2 = User('David', 'Tao', 40)
user3 = User.from_string('Helen,Wang,68')
print(user3)

print(user1) # test : __repr__ (Before, Aftore)
print(str(user1)) # test : __repr__ (Before, Aftore)
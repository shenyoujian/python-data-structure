#coding:utf8
#浅谈yield和yield from.py

# 例1：简单输出斐波那契数列前N个数，使用print打印
# 缺点：该函数的可复用性较差，因为fab函数返回None(没有返回值)，其他函数无法获取该函数生成的数列
# 如果要提高fab函数的可复用性，最好不要print打印出数列，而是返回一个List列表。

def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a+b
		n = n + 1

fab(5)

# 1
# 1
# 2
# 3
# 5

# 例2：输出斐波那契数列前N个数，返回List
# 优点：通过返回List能满足复用性的要求
# 缺点： 运行中占用的内存会随着参数max的增大而增大
# 最好不要用List来保存中间结果，而是通过iterablle对象来迭代

def fab(max):
	n, a, b = 0, 0, 1
	L = []
	while n < max:
		L.append(b)
		a, b = b, a+b
		n = n + 1
	return L

f = fab(5)
for n in f:
	print(n)

# 1
# 1
# 2
# 3
# 5


# 例3：输出斐波那契数列前N个数，使用iterable对象
# 优点：在每次迭代中返回下一个数值，内存空间占用很小
# 缺点： 没有第一版的fab函数简洁，因为要使用可迭代对象就得先构建class，并且实现__iter__()和next()方法
# python2的next不是魔法函数，不用加下划线，在python3中没加会ypeError: iter() returned non-iterator of type 'Fab'

class Fab(object):

	def __init__(self, max):
		self.max = max
		self.n, self.a, self.b = 0, 0, 1

	def __iter__(self): 
		return self

	def __next__(self):
		if self.n < self.max:
			r = self.b
			self.a, self.b = self.b, self.a + self.b
			self.n = self.n + 1
			return r
		raise StopIteration()

f = Fab(5)			# 实例化可迭代对象
for n in f:
	print(n)

# 1
# 1
# 2
# 3
# 5


# 例4：输出斐波那契数列，使用yield
# 优点：简洁性，并且获得了iterable的效果
# yield的作用就是把一个函数变成一个generator，带有yield的函数不再是一个普通函数，而是一个generator。
# 调用fab(5)不会执行fab函数，而是返回一个iterable对象。就像上面例3一样的可迭代对象。
# 然后当for循环执行时，每次循环才会执行fab函数内部的代码，并且执行到yield b，fab函数就会返回一个迭代值b赋值给n
# 当返回迭代值后，函数才继续往下执行，直到再次遇到yield。

def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

for n in fab(5):
	print(n)


# 1
# 1
# 2
# 3
# 5



# https://blog.csdn.net/nightcharm/article/details/78964676
# https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
# https://blog.csdn.net/liangjisheng/article/details/79776008
# https://www.jb51.net/article/117554.htm
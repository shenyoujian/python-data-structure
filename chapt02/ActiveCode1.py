
'''
计算前n个整数的和
该算法使用初始化值为0的累加器变量
然后迭代n个整数
'''

import time

def sumofN(n):
	start = time.time()

	theSum = 0
	for i in range(1, n+1):
		theSum = theSum + i

	end = time.time()

	return theSum, end-start

for i in range(5):
	print("Sum is %d required %10.7f seconds"%sumofN(10000))
	# print("Sum is %d required %10.7f seconds"%sumofN(100000))
	# print("Sum is %d required %10.7f seconds"%sumofN(1000000))


'''
使用封闭方程计算前n个整数的和。
'''
def sumofN3(n):
	start = time.time()

	theSum = (n*(n+1))/2
	
	end = time.time()
	return theSum, end-start

for i in range(5):
	print("Sum is %d required %10.7f seconds"%sumofN3(10000))
	# print("Sum is %d required %10.7f seconds"%sumofN(100000))
	# print("Sum is %d required %10.7f seconds"%sumofN(1000000))


'''
迭代方案执行所需的时间随n递增，而封闭方程几乎不受n的影响
上面这些执行时间会根据机器，程序，编译器等发生变化，所以它不能提供给我们一个有用的度量。
我们使用大O符号来比较，T()函数是执行语句进行计数，函数的数量级表示随着n的值
增加最快的那些部分。
T(n) = n+1
T(n) 的数量级为 O（f(n)） = n
运行时间是O(n)
'''

a = 5
b = 6
c = 10
for i in range(n):
	for j in range(n):
		x = i * i
		y = j * j
		z = i * j
for k in range(n):
	w = a*k + 45
	v = b*b
d = 33

'''
1、第一项三个赋值语句所以常项数是3
2、第二项由于嵌套迭代，有三个语句执行n^2次，所以是3n^2
3、第三项两个语句迭代n次，所以2n
4、第四项常数1表示最终赋值语句。
最后得出T(n) = 3+3n^2+2n+1 = 3n^2+2n+4
通过查看指数我们可以看到n^2项是显性的，所以代码段是O(n^2).当n增大时，所有其他项以及主项上的系数都可以忽略。
'''

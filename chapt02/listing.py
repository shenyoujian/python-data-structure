'''
1、列表两个常见的操作是索引和分配到索引位置。无论列表有多大，这两个操作都需要相同的时间。
当这样的操作和列表的大小无关时，它们都是O(1)
2、还有一个常见的编程任务是增加一个列表，有两种方法可以创建更长的列表，一是使用append方法二是拼接运算符。
append方法是O(1),拼接是O(k),其中k是要拼接列表的大小。
'''

'''
目标：生成一个从0到n个数字的列表
'''


'''
解法1：for循环并且通过拼接创建列表
'''
def test1():
	l = []
	for i in range(1000):
		l = l + [i]

'''
解法2：for循环并且使用append创建列表
'''
def test2():
	l = []
	for i in range(1000):
		l.append(i)

'''
解法3:列表生成器创建列表
'''
def test3():
	l = [i for i in range(1000)]

'''
解法4：调用列表构造函数包装range函数
'''
def test4():
	l = list(range(1000))

'''
测试
'''
from timeit import Timer
t1 = Timer("test1()", "from __main__ import test1")
print("concat", t1.timeit(number=1000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append", t2.timeit(number=1000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("comprehension", t3.timeit(number=1000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("list range", t4.timeit(number=1000), "milliseconds")

'''
结果：列表最快，append比拼接快得多。
'''


'''
目标：验证从列表从末尾pop元素和从开始pop元素的性能
'''
popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")

x = list(range(2000000))
print(popzero.timeit(number=1000))

x = list(range(2000000))
print(popend.timeit(number=1000))

'''
2.0300190599425636
0.00010814151809235284
对于一个200万的元素列表，两者的时间相差16000倍
因为当列表末尾调用pop是，它需要O(1)
但是在列表中第一个元素或者中间任何地方调用pop它是O(n),当一个项从列表前面取出，列表其他元素都会移动一个位置。
'''

'''
上面这个测试并不能证明pop(0)是O(n),pop()是O(1)
得通过改变列表的大小才能判断
'''
for i in range(1000000, 100000001, 1000000):
	x = list(range(i))
	pz = popzero.timeit(number=1000)

	x = list(range(i))
	pt = popend.timeit(number=1000)
	print("%15.5f, %15.5f" %(pz,pt)) 


'''
这就可以看出随着列表边长，pop(0)时间增加，而pop()时间保持非常平坦。
这就是我们希望看到的O(n)和O(1)
		0.90918,         0.00011
        1.93313,         0.00011
        2.96813,         0.00011
        3.94720,         0.00011
        5.03681,         0.00011
        5.89796,         0.00012
        7.01634,         0.00023
        7.83021,         0.00012
        9.03938,         0.00024
       10.80322,         0.00024
       11.36888,         0.00011
       11.73429,         0.00011
'''

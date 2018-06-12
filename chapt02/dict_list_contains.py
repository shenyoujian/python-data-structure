'''
目标：比较列表和字典之间的contains操作的性能。
结论：列表的contains操作符是O(n),而字典的contains操作符是O(1)
也就是说列表越大，确定列表中是否包含任意一个数字应该花费的时间越长，字典越大，花费的时间相差无几。
'''

import timeit
import random

for i in range(1000000, 100000001, 1000000):
	t = timeit.Timer("random.randrange(%d) in x"%i,					# Timer传入两个参数，第一个是想要执行时间的python语句，第二个参数是一个将运行一次以设置测试的语句
					"from __main__ import random,x")

	x = list(range(i))												#生成一个1000000，2000000，3000000...100000000个数的列表
	lst_time = t.timeit(number=1000)								# 最后调用timeit，执行1000次random.randrange(%d) in x,返回总时间
	x = {j:None for j in range(i)}
	d_time = t.timeit(number=1000)
	print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))


'''
证明了列表的contains操作为O(n),字典为O(1)
1000000,    11.297,     0.002
2000000,    21.030,     0.002
3000000,    32.245,     0.004
4000000,    41.810,     0.004
5000000,    50.808,     0.004
6000000,    65.147,     0.004
7000000,    74.984,     0.004
8000000,    85.718,     0.002
'''
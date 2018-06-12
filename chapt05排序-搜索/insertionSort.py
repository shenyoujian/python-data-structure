# coding utf8

'''
插入排序：算法O(n^2)
概述：
把列表分为两部分，一部分是排序好的，另一部分是待插入的
每次插入一个待插入的，并与排序好的部分进行比较，然后插入到正确位置上。
思路：
首先传入一个数组，从下标1开始到数组的长度-1进行遍历,因为0被当成已排序
把要插入的值视为当前值，下表视为当前下标。
循环判断该下标是否大于0并且下标为0到当前下标-1的值是否大于当前值
如果是就交换位置，并且当前下标-1，如果不是就说明当前比前面的值都大。
'''

def insertionSort(alist):
	for index in range(1, len(alist)):
		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
			alist[position] = alist[position-1]                   # 不用交换只是把比当前值大的值放到当前值的位置，当前值还没有插入
			position = position-1								  # 小的值的位置为空

		alist[position]=currentvalue							  # 最后才插入


alist = [54,26,93,17,77,31,4,55,20]
insertionSort(alist)
print(alist)

# [4, 17, 20, 26, 31, 54, 55, 77, 93]


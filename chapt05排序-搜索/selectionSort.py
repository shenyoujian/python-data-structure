# 选择排序，在每一次遍历中找到最大值并把它放到正确的位置。

def selectionSort(alist):
	for fillslot in range(len(alist)-1, 0, -1):
		positionofMax = 0
		for location in range(1, fillslot+1):
			if alist[location] > alist[positionofMax]:
				positionofMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionofMax]
		alist[positionofMax] = temp


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
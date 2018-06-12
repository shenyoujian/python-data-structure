# -*- utf8 -*-
# Deque.py


'''
Deque（双端队列）：
特点：有序集合，有两个端部, 首部和尾部，可以在前面或后面添加新项，也可以在任一端移除现有项。
Deque抽象数据类型
Deque()创建一个空的新deque。它不需要参数，返回空的deque。
addFront(item)将一个新项添加到deque的首部。它需要item参数并不返回任何内容。
addRear(item) 将一个新项添加到 deque 的尾部。它需要 item 参数并不返回任何内容。
removeFront() 从 deque 中删除首项。它不需要参数并返回 item。deque 被修改。
removeRear() 从 deque 中删除尾项。它不需要参数并返回 item。deque 被修改。
isEmpty() 测试 deque 是否为空。它不需要参数，并返回布尔值。
size() 返回 deque 中的项数。它不需要参数，并返回一个整数。
'''

'''
用Python实现一个Deque
底层同样使用列表
假定deque的尾部在列表中的位置为0
在removeFront中，我们使用pop方法从列表中删除最后一个元素。
但是，在removeRear中，pop(0)方法必须删除列表的第一个元素。因为deque的末尾是列表的开头，开头是列表的结尾。
所以deque从前面添加(列表的末尾)是O(1)，在后面添加(列表的前面)是O(n)
'''

class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)



'''
Deque的实际应用：回文检查
规则：对称然后首尾相同的字符串就是回文例如 radar toot madam
大概思路：把字符串从左到右每个字符添加到deque的尾部，全部添加后，再利用deque的双重功能，
把deque的前后两边的第一个字符移除并且判断是否相同，如果相同就继续取剩下的前后两边的字符继续判断，
直到不相同即不是回文，或者deque大小为1或者为0，即回文。
'''

def palchecker(aString):
	chardeque = Deque()

	for ch in aString:
		chardeque.addRear(ch)

	stillEqual = True

	while chardeque.size() > 1 and stillEqual:
		first = chardeque.removeFront()
		last = chardeque.removeRear()
		if first != last:
			stillEqual = False

	return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))

# False
# True
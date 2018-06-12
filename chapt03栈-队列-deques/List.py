# -*- utf8 -*-
# List.py


'''
UnorderedList (无序列表)：
特点：是项的集合，其中每个项保持相对于其他项的相对位置。
UnorderedList抽象数据类型：
List()创建一个新的空列表。它不需要参数，并返回一个空列表。
add(item)向列表中添加一个新项。它需要item作为参数，并不返回任何内容。假定该item不在列表中。
remove(item)从列表中删除该项。它需要item作为参数并修改列表。假设项存在于列表中。
search(item)搜索列表中的项目。它需要item作为参数，并返回一个布尔值。
isEmtry()检查列表是否为空。它不需要参数，并返回布尔值。
size()返回列表中的项数。它不需要参数，并返回一个整数。
append(item)将一个新项添加到列表的末尾，使其成为集合中的最后一项。它需要 item
作为参数，并不返回任何内容。假定该项不在列表中。
index(item) 返回项在列表中的位置。它需要 item 作为参数并返回索引。假定该项在列表
中。
insert(pos，item) 在位置 pos 处向列表中添加一个新项。它需要 item 作为参数并不返回
任何内容。假设该项不在列表中，并且有足够的现有项使其有 pos 的位置。
pop() 删除并返回列表中的最后一个项。假设该列表至少有一个项。
pop(pos) 删除并返回位置 pos 处的项。它需要 pos 作为参数并返回项。假定该项在列表中。
'''

'''
实现无序列表：链表
# 链表实现的基本构造块是节点，每个节点对象至少保存两个信息，数据字段(列表项本身data)和下一个节点的引用(next)。
# 节点类
# 在构造函数中，最初创建的节点next被设置为None，代表没有下一个节点，也称接地节点。
'''

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

temp = Node(93)
print(temp.getData())

# 93

'''
UnorderedList类本身有个head，它必须保持对第一个节点的引用。
即head指向第一个节点，然后第一个节点的next又继续指向下一个节点。
'''

class UnorderedList:
	'''
	head = None说明空链表，链表头部head不引用任何节点。
	'''
	def __init__(self):
		self.head = None


	'''
	只是检查链表头部是否是None的引用。
	'''
	def isEmpty(self):
		return self.head == None


	'''
	由于链表是无序的，所以新项可以在任何位置。
	链表结构只提供了一个入口点链表的头部，所以添加新节点的地方就在链表的头部。
	当调用add(31),需要三个步骤：
	 - 创建一个新节点并将该项作为其数据
	 - 更改新节点的下一个引用以引用旧链表的第一个节点head所引用的，所以31节点的引用指向None
	 - 然后把链表的头部head指向31节点。
	'''
	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp


	'''
	从链表的头head开始，获取每个节点的引用，如果不是None就+1，直到None就退出
	'''
	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()

		return count


	'''
	从链表的头部开始，这次是遍历每个节点的数据，如果与item相当就found就True并且退出，否则获取下一个节点引用
	'''
	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

	'''
	remove需要三个逻辑步骤
	 - 遍历列表寻找我们要删除的项(类似搜索的步骤)
	 - 如果当前节点的数据不是目标，就把当前节点赋值给previous
	 - 最后判断previous是否None，如果是None说明第一个节点就找到了目标，然后把第一个节点的引用赋值给链表的头部head
	 	这样第一个节点就相当于删除了，否则把当前节点的引用赋值给上一个节点的引用
	'''
	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())



'''
OrderedList(有序列表)
特点：是项的集合，其中每个项保存基于项的一些潜在特性的相对位置。排序通常是升序或降序。
例如，有一个集合里面有17，93，26，31，77，54，则它的有序列表(升序)为17，26，31，54，77，93
有序列表抽象数据结构：
OrderedList() 创建一个新的空列表。它不需要参数，并返回一个空列表。
add(item) 向列表中添加一个新项。它需要 item 作为参数，并不返回任何内容。假定该
item 不在列表中。
remove(item) 从列表中删除该项。它需要 item 作为参数并修改列表。假设项存在于列表
中。
search(item) 搜索列表中的项目。它需要 item 作为参数，并返回一个布尔值。
isEmpty() 检查列表是否为空。它不需要参数，并返回布尔值。
size（）返回列表中的项数。它不需要参数，并返回一个整数。
index(item) 返回项在列表中的位置。它需要 item 作为参数并返回索引。假定该项在列表
中。
pop() 删除并返回列表中的最后一个项。假设该列表至少有一个项。
pop(pos) 删除并返回位置 pos 处的项。它需要 pos 作为参数并返回项。假定该项在列表
'''

'''
实现有序列表
'''

class OrderedList:
	def __init__(self):
		self.head = None

	'''
	有序列表的isEmpty和size方法和无序列表一样
	因为它们只处理链表中的节点数量，而不考虑实际项值。
	remove方法也一样相同，因为我们仍然需要找到该项，然后删除它。
	'''

	'''
	search方法
	有序列表也可以像无序列表那样寻找节点，但是我们可以利用顺序来尽快停止搜索。
	例如17，26，31，54，77，93中，要查找45，当我们找到54不等于45的时候就可以停止了。
	'''
	def search(self,item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()

		return found


	'''
	现在链表是有序，所以添加项不在是从把新节点放置在链表的头部
	而是需要在现有的有序列表中查找新项所属的特定位置
	例如17，26，31，54，77，93，当我们要添加40不在是添加到93后面，而是添加到31和54中间
	'''
	def add(self,item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()
		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)



'''
考虑具有 n 个节点的链表，isEmpty 方法是 O(1)。
因为它需要一个步骤来检查头的引用为 None 。另一方面， size 将总是需要 n 个步骤，
因为不从头到尾地移动没法知道有多少节点在链表中。因此，长度为O(n)。
将项添加到无序列表始终是O(1)，因为我们只是将新节点放置在链表的头部。但是，
搜索和删除，以及添加有序列表，都需要遍历过程。虽然平均他们可能只需要遍历节点的一
半，这些方法都是 O(n)，因为在最坏的情况下，都将处理列表中的每个节点。
'''




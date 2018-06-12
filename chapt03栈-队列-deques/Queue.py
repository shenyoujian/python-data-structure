# -*- utf8 -*-
# Queue.py

'''
队列：
特点：先进先出，有序集合，添加新项的一端为队尾，移除项的一端称为队首。
排序原则为：FIFO，先进先出
队列的抽象数据类型：
Queue() 创建一个空的新队列。它不需要参数，并返回一个空队列。
enqueue(item) 将新项添加到队尾。它需要item作为参数，并不返回任何内容。
dequeue() 从队首移除项。它不需要参数并返回item。队列被修改。
isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
size() 返回队列中的项数。它不需要参数，并返回一个整数。
'''

'''
用python实现一个Queue
实现一个Queue类，底层使用列表集合作为构建队列的内部表示
假定队尾在列表中的位置为0，使用列表的插入函数向队列添加新元素，弹出可用于删除队首的元素(列表的最后一个元素)
入队O(n),列表所有元素移动一个位置，出队O(1)，直接删除列表最后一个元素。
'''

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


q = Queue()
q.enqueue(4)
q.enqueue(5)
print(q.size())
print(q.isEmpty())
q.enqueue(8.4)
print(q.dequeue())
print(q.size())

# 2
# False
# 4
# 2


'''
队列的实际应用，烫手山芋
游戏规则：孩子们围成一个圈，并尽可能快的将一个山芋递给旁边的孩子。在某一个时间，
动作结束，有山芋的孩子从圈中移除，游戏继续直到剩下最后一个孩子。

模拟这个游戏的过程的大概思路：使用队列来模拟这个圈，先假设所有的孩子都在队列里，拿着山芋的孩子在队列的前面，当拿到山芋的时候，
这个孩子将先出列，再把他放到队列的最后。然后山芋又回到队列前的孩子，继续重复刚才的操作。但是我们先得给定一个num，表示经过第num次的
出队入队后，前面的孩子将被永久移除队列。直到最后只剩下一个孩子(队列大小为1).

注意：num要大于列表中的名称数，因为队列像一个圈，计数会重新回到开始，直到达到计数值。
'''

def hotPotato(namelist, num):
	simqueue = Queue()
	for name in namelist:					
		simqueue.enqueue(name)

	while simqueue.size() > 1:
		for i in range(num):
			simqueue.enqueue(simqueue.dequeue())

		simqueue.dequeue()

	return simqueue.dequeue()					# 打印最后一个

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))


'''
队列的实际应用：模拟打印机

规则，一台共享打印机，10个同学排队打印，计算平均的等待时间。

模拟主要步骤：
 1、创建打印任务的队列，每个任务都有个时间戳（任务从创建到入队的时间）。队列启动的时候为空。
 2、每秒(currentSecond)
 	- 是否创建新的打印任务？如果是，将currentSecond（任务加入队列的时间）作为时间戳添加到队列。
 	- 如果打印机不忙并且有任务在等待
 	  - 从打印机队列中删除一个任务并将其分配给打印机
 	  - 从currentSecond中减去时间戳，以计算该任务的等待时间。（也就是任务从进入到队列到开始打印之间的等待时间）
 	  - 将该任务的等待时间附件到列表中稍后处理。	
	- 打印机需要一秒打印，所以得从该任务的所需的等待时间减去一秒。 （从给定的numSecond开始倒数，并且倒数一秒就代表打印了一秒）
	- 如果任务已经完成，换句话说，所需的时间已经达到零，打印机空闲。
3、模拟完成后，从生成的等待时间列表中计算平均等待时间。
'''

'''
创建三个类:Printer, Task, PrintQueue
Printer，打印机类。
- 需要跟踪它当前是否有任务，如果有则它处于busy状态
- 可以从任务的页数计算所需的时间。
- 构造函数允许初始化每分钟页面的配置
- tick方法将内部定时器递减直到打印机设置为空闲
'''
class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm;													# 设置每分钟打印多少张
		self.currentTask = None													# 当前任务
		self.timeRemaining = 0													# 打印当前任务所需的时间


	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1							# 当计时器在走，打印当前任务也在走
			if self.timeRemaining <= 0:											# 判断是否打印完成
				self.currentTask = None

	def busy(self):
		if self.currentTask !=None:
			return True
		else:
			return False

	def startNext(self, newtask):												
		self.currentTask = newtask												
		self.timeRemaining = newtask.getPages() * 60/self.pagerate				# 因为timeRemaining是秒，而pagerat是每分钟打印的页数



'''
Task， 任务类。
- 创建任务时，随机数生成器将提供1到20页的长度。使用随机模块中randrange函数
- 每个任务保存一个时间戳用于计算等待时间。此时间戳表示任务被创建并放到打印机队列的时间。
- waitTime方法检索在打印开始之前队列中花费的时间。
'''
import random

class Task:
	def __init__(self, time):	
		self.timestamp = time                                                   # 任务创建的时间
		self.pages = random.randrange(1,21) 									# 随机生成1到20之间的数字


	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):											# 返回任务从创建到入队的等待时间
		return currenttime - self.timestamp



'''
PrintQueue :等待队列类，上面已经实现
simulation：模拟打印方法
newPrintTask: 决定是否创建新的打印任务,打印任务每180秒我们就创建一个新的。
'''

import random

def simulation(numSeconds, pagePerMinute):									# numSeconds为打印机会运行的总时间

	labprinter = Printer(pagePerMinute)										# 打印机传入每分钟打印的页数
	printQueue = Queue()
	waitingtimes = []														# 等待时间列表

	for currentSecond in range(numSeconds):

		if newPrintTask():													# 3分钟就会有一个打印任务生成
			task = Task(currentSecond)
			printQueue.enqueue(task)


		if (not labprinter.busy()) and (not printQueue.isEmpty()):
			nexttask = printQueue.dequeue()
			waitingtimes.append(nexttask.waitTime(currentSecond))
			labprinter.startNext(nexttask)


		labprinter.tick()													# 计时器，numSeconds之后开始倒计时

	averageWait = sum(waitingtimes)/len(waitingtimes)
	print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))





def newPrintTask():
	num = random.randrange(1,181)
	if num == 180:
		return True
	else:
		return False


# 每分钟5页，运行60分钟
for i in range(10):
	simulation(3600,5)


# Average Wait  38.60 secs   1 tasks remaining.
# Average Wait  76.05 secs   2 tasks remaining.
# Average Wait  55.87 secs   3 tasks remaining.
# Average Wait  79.60 secs   0 tasks remaining.
# Average Wait  76.12 secs   0 tasks remaining.
# Average Wait  90.53 secs   0 tasks remaining.
# Average Wait  98.25 secs   1 tasks remaining.
# Average Wait  48.13 secs   0 tasks remaining.
# Average Wait  87.52 secs   0 tasks remaining.
# Average Wait 262.91 secs   3 tasks remaining.
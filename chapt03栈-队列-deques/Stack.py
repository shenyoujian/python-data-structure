# -*- utf8 -*-
# Stack.py
'''
栈：
特点：后进先出，有序集合，添加移除总发生在同一端。这一端称为顶部，对应端称为底部。
排序原则为：LIFO,后进先出。
栈抽象数据类型：
Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
size() 返回栈中的 item 数量。不需要参数，并返回一个整数。
'''

'''
用python实现栈
实现一个栈类，用列表做底层实现
'''

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.size())
print(s.peek())
print(s.isEmpty())
print(s.pop())
print(s.size())

'''
栈的实际应用，简单括号匹配
匹配
(()()()())
(((())))
(()((())()))
不匹配
((((((())
()))
(()()(()
大概思路就是把括号们从左到右先判断，如果是左括号{，就入栈
如果是}就出栈，从内到外匹配。例如{}这个，先是{入栈，然后是}就把栈里的{出栈与}匹配
最后所有符号都被处理后并且栈也是空就说明匹配成功了。
'''

def parChecker(symbolString):
	# 先实例化一个空栈
	s = Stack()
	balanced = True
	index = 0
	while index < len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol == '{':
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				s.pop()

		index = index + 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

print(parChecker('{{{}}}'))
print(parChecker('{{}'))

# True
# False

'''
栈的实际应用，符号匹配。
不仅每个开始符号都有对应的结束符号，而且符号的类型也匹配。
匹配
{ { ( [ ] [ ] ) } ( ) }
[ [ { { ( ( ) ) } } ] ]
[ ] [ ] [ ] ( ) { }
不匹配
( [ ) ]
( ( ( ) ] ) )
[ { ( ) ]
大概思路就是每个开始符号入栈，当出现结束符号，检查该结束符号
是否正确匹配栈顶部开始符号的类型。如果两个符号不匹配，则整个字符串不匹配，
如果整个字符串都被处理完并且空栈，则字符串匹配。
'''
def parChecker2(symbolString):
	s = Stack()
	balanced = True
	index = 0
	while index > len(symbolString) and balanced:
		symbol = symbolString[index]
		if symbol in "{[(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top, symbol):
					balanced = False

		index = index + 1
	if balanced and s.isEmpty():
		return True
	else:
		return False

def matches(open, close):
	opens = "{[("
	closers = "}])"
	return opens.index(open) == closers.index(close)



'''
栈的实际应用：十进制转换二进制
计算机内的所有值都是以0和1存储的，例如：十进制 233 对应的二进制表示 11101001， 
2*10^2 + 3*10^1 + 3*10^0
1*2^7 + 1*2^6 + 1*2^5 + 1*2^4 + 1*2^3 + 1*2^2 + 1*2^1 + 1*2^0
计算机使用除2算法，并且用栈来跟踪二进制结果的数字
大概思路就是：传入一个十进制的参数，并重复除以2，然后使用内置%提取余数，把余数入栈，当除到0后，再出栈构造二进制字符串
'''

def divideBy2(decNumber):
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber//2


	binString = ""
	while not remstack.isEmpty():
		binString = binString + str(remstack.pop())

	return binString

print(divideBy2(42))

# 101010


'''
栈的实际应用：十进制和基数的转换
例如：233对应的八进制351和十六进制E9
3*8^2 + 5*8^1 + 1*8^0
14*16^ + 9*16^0
大概思路：增加一个基数的参数，把除2换成除基数，然后余数继续入栈，除到0就开始出栈，
不同的是余数会大于9，然后先创建一组数字来表示超过9的余数，在下标取值。
'''

def baseConverter(decNumber, base):
	digits = "0123456789ABCDEF"

	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % base
		remstack.push(rem)
		decNumber = decNumber // base

	newString = ""
	while not remstack.isEmpty():
		newString = newString + digits[remstack.pop()]

	return newString

print(baseConverter(25,2))
print(baseConverter(25,16))

# 11001
# 19


'''
栈的实际应用：中缀转后缀
先从左到右看，如果遇到运算符就放到两个操作数的后面，然后再看成一个整体操作数，以此类推。
例如：A+B*C，转换成ABC*+
(A+B)*C,转换为AB+C*
大概思路：
1、创建一个名为opstack的空栈以保存运算符。给输出创建一个空列表。
2、使用字符串拆分方法将输入的中缀字符串转换为标记列表。
3、从左到右扫描标记列表
	- 如果标记是操作数，将其附加到输出列表末尾
	- 如果标记是左括号，将其入栈
	- 如果标记是右括号，则弹出栈，循环判断是否是左括号，如果不是左括号就附加到输出列表末尾，直到是左括号，删除左括号退出循环
	- 如果标记是运算符*/+-，则入栈，但是首先得先删除已经在栈中具有更高或相等优先级的任何运算符，将它们加到输出列表中。
4、当输入表达式被完全处理时，检查栈，仍然在栈上的任何运算符都可以删除并加到输出列表的末尾。
'''

def infixToPostfix(infixexpr):
	prec = {}												# 使用一个字典来保存操作符的优先级，左括号被赋予最低的值，
	prec["*"] = 3											# 这样与其进行比较的任何运算符将具有更高的优先级，将被放置在它的顶部
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	opStack = Stack()										# 中间件
	postfixList = []										# 最终表达式的存储列表
	tokenList = infixexpr.split()							# 把传进来表达式进行拆分

	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfixList.append(token)
		elif token == '(':
			opStack.push(token)
		elif token == ')':									# 遇到右括号就出栈
			 topToken = opStack.pop()		
			 while topToken != '(':							# 出栈的如果不是左括号就添加到输出列表
			 	postfixList.append(topToken)
			 	topToken = opStack.pop()					# 直到出栈是左括号为止
		else:
			while(not opStack.isEmpty()) and \
				(prec[opStack.peek()] >= prec[token]):		# 如果是运算符，就去判断栈是否为空，不为空就判断栈顶与token的优先级
					postfixList.append(opStack.pop())		# 栈顶的运算符比token高就出栈加入输出列表

			opStack.push(token)								# 否则入栈

	while not opStack.isEmpty():
		postfixList.append(opStack.pop())
	return "".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))

# AB*CD*+
# AB+C*DE-FG+*-

'''
栈的实际应用：后缀表达式求值
做完上面的中缀转换后缀之后，就可以来求表达式的值，选择的数据结构还是栈。
大概思路：遇到操作数就入栈，遇到运算符就出栈两个然后运算后再入栈。注意除法不是交换运算符，先出栈的为被除数，后出栈的为除数。
1、创建一个名为operandStank的空栈
2、拆分字符串转换为标记列表。
3、从左到右扫描标记列表
	- 如果标记是操作数，将其从字符串转换为整数，并将值压到operandStack。
	- 如果标记是运算符 *，/，+ 或 - ，它将需要两个操作数。弹出operandStack 两次。
		第一个弹出的是第二个操作数，第二个弹出的是第一个操作数。执行算术运算后，
		将结果压到操作数栈中。
4. 当输入的表达式被完全处理后，结果就在栈上，弹出 operandStack 并返回值。
'''

def postfixEval(postfixExpr):
	operandStack = Stack()
	tokenList = postfixExpr.split()

	for token in tokenList:
		if token in "0123456789":
			operandStack.push(int(token))
		else:
			operand2 = operandStack.pop()
			operand1 = operandStack.pop()
			result = doMath(token, operand1, operand2)	
			operandStack.push(result)				
	return operandStack.pop()

def doMath(token, operand1, operand2):
	if token == "*":
		return operand1 * operand2
	elif token == "/":
		return operand1 / operand2
	elif token == "+":
		return operand1 + operand2
	else:
		return operand1 - operand2

print(postfixEval('7 8 + 3 2 + /'))

# 3.0
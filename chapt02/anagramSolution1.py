'''
乱序字符串检查,例如'heart'和’earth'
目标写一个布尔函数，将两个字符串做参数并返回它们是不是乱序
'''

'''
解法1：检查
思路：检查第一个字符串的每个字符是否出现在第二个字符串中，那么这两个字符串一定是乱序的。
算法复杂度O(n^2)
'''

def anagramSolution1(s1,s2):
	alist = list(s2)									# 步骤一，先把第二字符串转换为列表，因为字符串是不可变

	post1 = 0
	stillOK = True

	while post1 < len(s1) and stillOK:
		post2 = 0
		found = False
		while post2 < len(alist) and not found:			
			if s1[post1] == alist[post2]:				# 步骤二：把字符串1中的字符与列表的每个元素比较，比较次数从1到len(alist)次
				found = True
			else:
				post2 = post2 + 1

		if found:
			alist[post2] = None							# 步骤三：当在list中找到的时候，找到这个元素并且设置为None(字符串2转换列表的原因)
		else:											
			stillOK = False

		post1 = post1 + 1								# 接着下一个字符的比较

	return stillOK

print(anagramSolution1('abcd','dcba'))


'''
s1每个字符都会在s2中进行最多n个字符的迭代
s2列表中的n个位置将被访问一次来匹配来自s1的字符。访问次数写成1到b整数的和。
(n(n+1))/2 = 1/2*n^+1/2*n不太理解
'''

'''
解法2：排序和比较
思路：两个字符串都是由a到z这些字符串组成的，所以我们把这两个字符串的字符从a到z排列，
然后再比较这两个字符串是否相同,如果相同就乱序。
算法复杂度： O(n^2)或O(nlogn)
'''

def anagramSolution2(s1, s2):
	alist1 = list(s1)									# 步骤一：转换为列表
	alist2 = list(s2)

	alist1.sort()										# 步骤二：对列表进行排序
	alist2.sort()

	pos = 0
	matches = True

	while pos < len(s1) and matches:
		if alist1[pos] == alist2[pos]:					# 步骤三：对排序后的两个列表的每个元素一一对应比较
			pos = pos + 1
		else:
			matches = False								# 当有一个不相等就不是乱序

	return matches

print(anagramSolution2('abcde','edcba'))

'''
这个理解起来就简单，但是这个算法复杂度不是O(n),虽然只有一个简单的迭代来比较排序后的n个字符，
但是调用排序也有算法复杂度。排序通常是O(n^2)或O(nlogn)
'''


'''
解法3：穷举法
思路：生成s1的所有乱序字符串列表，然后查看是不是有s2。
意思就是[a,b,c],[a,c,b],[b,a,c],[b,c,a],[c,b,a],[c,a,b]总共有
6种，然后把列表二与这6种分别比较。当列表元素为n时，第一个位置有n种可能，第二位置有n-1种等等
总数为n*(n-1)*(n-2).....3*2*1 即n!。n!比n^2增长还快，这不是很好的解决方案。
'''


'''
解法4：计数和比较
思路：先用一个长度为26的列表，a到z各占一个位置
然后把两个列表的每个元素与这26个元素比较，如果相等，该位置的计数器+1，
最后比较两个列表的计数器是否一样。
算法复杂度：O(n)
'''

def anagramSoulution4(s1, s2):
	c1 = [0]*26											# 步骤一：生成两个计数器列表，每个列表26个计数器
	c2 = [0]*26

	for i in range(len(s1)):
		pos = ord(s1[i])-ord('a')						# 步骤二：把列表的每个元素与a比较，相差数就在对应的计数器上加1
		c1[pos] = c1[pos] + 1

	for i in range(len(s2)):
		pos = ord(s2[i])-ord('a')
		c2[pos] = c2[pos] + 1

	j = 0
	stillOK = True
	while j<26 and stillOK:								# 步骤三：比较两个列表的计数器
		if c1[j] == c2[j]:
			j = j + 1
		else:
			stillOK = False

	return stillOK

print(anagramSoulution4('apple','pleap'))


'''
前面两个迭代都是n，第三个迭代比较两个计数列表，需要26步
T(n) = 2n+26
O(n) = n
我们找到了一个线性量级的算法解决这个问题，但是它需要花费额外的存储来保存两个字符计数列表，也就是说该算法牺牲了空间获取时间。
'''
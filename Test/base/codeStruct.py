'''
程式結構
'''

def 串列生成式():
	number_list = []
	for number in range(1,6):
		number_list.append(number)
	print (number_list)

	#也等於
	number_list = list(range(1,6))
	print (number_list)

	#串列生成式
	number_list = [ number for number in range(1,6)]
	print (number_list)

	a_list = [number for number in range(1,6) if number%2 == 1]
	print(a_list)

	#make cells
	rows = range(1,5)
	cols = range(1,3)
	cells = [(row , col) for row in rows for col in cols]
	print(cells)

def 字典生成式():
	word = 'letters'
	letter_counts = {letter:word.count(letter) for letter in word}
	print(letter_counts)

	#提生效能
	letter_counts = {letter:word.count(letter) for letter in set(word)}
	print(letter_counts)

def 集合生成式():
	a_set = {number for number in range(1,6) if number%3 ==1 }
	print (a_set)

if __name__ == "__main__":
	串列生成式()
	字典生成式()
	集合生成式()
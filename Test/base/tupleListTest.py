#List
def listTest():
	#一個單字元字串串列
	print( list('cat') )

	birthday = '1/6/2016'
	print(birthday.split('/')) 

	#slice取出項目
	marxes = ['Groucho','Chico' , 'Harpo']
	print(marxes[0:2])
	print(marxes[::2])

	#append
	marxes.append('Zeppo')
	print(marxes)

	#extend , +=
	others = ['Gummo' , 'Karl']
	marxes += others
	print(marxes)

	#insert 位移值0會在開頭處插入 ，超過位移值則插至結尾
	marxes.insert(3 , 'Johnny')
	marxes.insert(10, 'Mary')
	print(marxes)

	#del
	del marxes[-1]
	print(marxes)
	del marxes[2]
	print(marxes)

	#remove 指定key刪除
	# marxes.remove('JohnnyX') will throw Exception
	marxes.remove('Johnny')
	print(marxes)

	#pop 取位移值一個項目，並刪除它
	print(marxes.pop())
	print(marxes)
	print(marxes.pop(1))
	print(marxes)

	#index
	print(marxes.index('Zeppo'))
	# print(marxes.index("johnnyx"))  with throw exception

	#in

	#count
	print(marxes.count('Zeppo'))
	
def zipTest():
	'''
	zip 會在最短的序列結束時停止
	'''
	days = ['Monday' , 'Tuesday' , 'Wednesday']
	fruits = ['banana' , 'orange' , 'peach']
	drinks = ['coffee' , 'tea' , 'beer']
	desserts = ['tiramisu' , 'ice cream' , 'pie' , 'pudding']

	for day , fruit , drink , dessert in zip(days, fruits , drinks , desserts):
		print (day, ": drink" , drink , "- eat" , fruit , "- enjoy" , dessert)



if __name__ == "__main__":
	# listTest()
	zipTest()
	
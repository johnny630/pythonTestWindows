
def enumerate_test():
	'''優先選用 enumerate 而非range'''
	flavor_list = ['vanilla' , 'chocolate' , 'pecan' , 'strawberry']
	for i , flavor in enumerate (flavor_list):
		print('%d: %s' %(i+1 , flavor))

	for i , flavor in enumerate (flavor_list , 1):
		print('%d: %s' %(i , flavor))

def index_words(text):
	result = []
	if text:
		result.append(0)
	for index , letter in enumerate(text):
		if letter == ' ':
			result.append(index+1)
	return result

def index_words_iter(text):
	if text:
		yield 0
	for index, letter in enumerate(text):
		if letter == ' ':
			yield index+1

def 考慮使用產生圖而非回傳串列():
	address = "Four score and seven years ago ..."
	# result = index_words(address)
	result = list(index_words_iter(address))
	print(result[:3])

if __name__ == "__main__":
	enumerate_test()
	考慮使用產生圖而非回傳串列()
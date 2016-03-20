
def enumerate_test():
	'''優先選用 enumerate 而非range'''
	flavor_list = ['vanilla' , 'chocolate' , 'pecan' , 'strawberry']
	for i , flavor in enumerate (flavor_list):
		print('%d: %s' %(i+1 , flavor))

if __name__ == "__main__":
	enumerate_test()
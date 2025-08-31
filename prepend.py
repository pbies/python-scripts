# prepend('01','0',64)

def prepend(data, char, count):
	return char*(count-len(data))+data

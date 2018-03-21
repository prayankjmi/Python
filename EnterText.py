while True:
	reply = input("enter text:")
	try:
		print (reply)
		num = int(reply)
		print('text')
	except:
		print("Bad")
	else:
		print (num ** 2)


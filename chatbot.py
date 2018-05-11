import random
def main():
	item_list = ['t-shirt','pants']
	agree_list = ['yes','sure','of course']
	hello_list = ['Hi!','halo','hello','bello','yo']
	no_list = ['no','not yet','not now','next time','no,']
	
	endConversation = False

	print("Shop: Hi, I'm a bot. Call me SellingBot.")
	print("Shop: How can I help you.")
	
	while endConversation == False:
		text = input('Me: ') #What products are you have?
		proc = text.split(' ')
		retCheck = contextCheck(proc)
		# print (retCheck)
		if retCheck == 'greeting':
			helloIndex = random.randint(1,len(hello_list)-1)
			print('Shop: ' + hello_list[helloIndex] + ', please say what you need.')
			
		elif retCheck == 'ordering':
			for i in proc:
				if i.lower() == 'something' or i.lower() == 'product':
					print("Now we have : ")
					print("ID	 Product	Size 	 Color	 	Quantity")
					print("001	 T-shirt 	S,M,L    Black	 	10")
					print("002	 Pants 		S,M,L   red,blue 	10")
					
		elif retCheck == 'suggesting':
			x = random.randint(0,len(item_list)-1)
			print("Shop: " + item_list[x] + ' is suggested for you.')
			print("Shop: Do you like it ?")
			ans = input('Me: ')

			if ans.lower() in agree_list :
				print("Shop: Do you like to order now?")
				ans = input('Me: ')
				ans_proc = ans.split(' ')
				for j in ans_proc:
					if j in agree_list:
						print("Shop:  Order me")
						ans2 = input('Me: ')
						ans_proc2 = ans.split(' ')
						for k in ans_proc2 :
							if k in item_list:
								print("You order for " + k + ", What shipping method do you prefer?")
								ans_shippping = input('Me: ')
								shipping_proc = ans_shippping.split(' ')
								shipping_check = 1
								while shipping_check == 1:
									for l in shipping_proc:
										if l in shipping_list:
											print('I will send you in 2 days. Thanks for coming.')
											shipping_check = 0
										else :
											print('We only have 3 shipping method. EMS, KERRY and DHL ')														
			else :
				print ("Shop: Okay, I'm sorry")
		elif retCheck == 'notUnderstand':
			print ('Shop: Sorry, I cannot understand it.')
		elif retCheck == 'ending':
			print('Shop: see you later')
			endConversation = True
			exit(0)
		
def contextCheck(wordProc):
	# Variable declaration
	hello_list = ['Hi!','halo','hello','bello','yo']
	shipping_list = ['kerry','ems','dhl']
	notUnderstandCount = 0
	
	# for check
	for i in wordProc:
		if i.lower() in hello_list :
			return 'greeting'
		elif i.lower() == 'buy' or i.lower() == 'what':
			return 'ordering'
		elif i.lower() == 'suggest':
			return 'suggesting'
		elif i.lower() == 'goodbye':
			return 'ending'
		else :
			notUnderstandCount += 1
	if notUnderstandCount == len(wordProc):
		return 'notUnderstand'
		
def soundex_input(name):
	name = name.upper()
	soundex = ""
	soundex += name[0]
	dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

	for char in name[1:]:
		for key in dictionary.keys():
			if char in key:
				code = dictionary[key]
				if code != soundex[-1]:
					soundex += code
	soundex = soundex.replace(".", "")
	soundex = soundex[:4].ljust(4, "0")
	return soundex
		
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print ('Interrupted ..')
	try:
		sys.exit(0)
	except SystemExit:
		os._exit(0)


# findShowTime = "รอบกี่โมง"
# findShowTimeToken = word_tokenize(findShowTime, engine='newmm')
# findShowTimeCount = 0

# findMovieName = "กับตันอเมริกาไอร่อนแมน"
# findMovieNameToken = word_tokenize(findMovieName, engine='newmm')
# findMovieNameCount = 0


# for i in range(len(proc)):
#     for j in range(0, len(findShowTimeToken)):
#         if LK82(proc[i]) == LK82(findShowTimeToken[j]):
#             findShowTimeCount = findShowTimeCount+1;


# for i in range(len(proc)):
#     for j in range(0, len(findMovieNameToken)):
#         if LK82(proc[i]) == LK82(findMovieNameToken[j]):
#             findMovieNameCount = findMovieNameCount+1


# if findShowTimeCount > findMovieNameCount:
#     print("ShowTime")
# else:
#     print("Avenger")
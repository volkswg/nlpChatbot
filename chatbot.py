import random
import re
import operator

def main():
	item_list = ['t-shirt','pants']
	agree_list = ['yes','sure','of course']
	hello_list = ['halo','hello','bello','yo','hi']
	no_list = ['no','not yet','not now','next time','no,']
	shipping_list = ['ems','kerry','dhl']
	
	endConversation = False

	print("Shop: Hi, I'm a bot. Call me SellingBot.")
	# print("Shop: How can I help you.")
	
	while endConversation == False:
		text = input('Me(Home): ')
		text = re.sub('[!@#$,]', '', text) # clean sentence (not alphabet)
		proc = text.split(' ')
		retCheck = contextCheck(proc, hello_list)
		# print (retCheck)
		
		# for i in proc:
			# print (soundex_input(i))
		if retCheck == 'greeting':
			helloIndex = random.randint(0,len(hello_list)-1)
			print('Shop: ' + hello_list[helloIndex] + ', can I help you?')
			
		elif retCheck == 'ordering':
			print("Shop: Okay Good, then you can look at the store and copy the item code and I will send you a detail.")
			# print("Now we have: ")
			# print("ID	 Product	Size 	 Color	 	Quantity")
			# print("001	 T-shirt 	S,M,L    Black	 	10")
			# print("002	 Pants 		S,M,L   red,blue 	10")
			# print("Shop:  Order me")
			# ans2 = input('Me(Order): ')
			# ans_proc2 = ans2.split(' ')
			# for k in ans_proc2 :
				# if k in item_list:
					# print("You order for " + k)
					
					# shipping_check = 1
					# count = 0
					# while shipping_check == 1:
						# print("How can I send you our products?")
						# ans_shippping = input('Me: ')
						# shipping_proc = ans_shippping.split(' ')
						# for l in shipping_proc:
							# count = count + 1
							# if l.lower() in shipping_list:
								# print('I will send you in 2 days. Thanks for coming.')
								# shipping_check = 0
							# else :
								# if count == len(shipping_proc):
									# print('We only have 3 shipping method. EMS, KERRY and DHL ')														
					
		elif retCheck == 'suggesting':
			x = random.randint(0,1)
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
						ans2 = input('Me(Order): ')
						ans_proc2 = ans2.split(' ')
						for k in ans_proc2 :
							if k in item_list:
								print("You order for " + k)
								
								shipping_check = 1
								count = 0
								while shipping_check == 1:
									print("How can I send you our products?")
									ans_shippping = input('Me: ')
									shipping_proc = ans_shippping.split(' ')
									for l in shipping_proc:
										count = count + 1
										if l.lower() in shipping_list:
											print('I will send you in 2 days. Thanks for coming.')
											shipping_check = 0
										else :
											if count == len(shipping_proc):
												print('We only have 3 shipping method. EMS, KERRY and DHL ')														
			else :
				print ("Shop: Okay, I'm sorry")
		elif retCheck == 'notUnderstand':
			print ('Shop: Sorry, I cannot understand it.')
		elif retCheck == 'ending':
			print('Shop: see you later')
			endConversation = True
			exit(0)
		else :
			checkItemCodeDetail(retCheck)
			
def cleanWord(sentence):
	for alpha in sentence:
		if not alpha.isalpha():
			print(alpha)
			sentence.replace('!','')
	print (sentence)
	
def checkItemCodeDetail(itemCode):
	item_list = [['IC1234','T-shirt','S,M,L','Red'],['IC2341','Pant','S,M,L','Blue'] ]
	for i in range(0,len(item_list)):
		if itemCode == item_list[i][0]:
			print ('Shop: This item is a' + item_list[i][1] + ' and we have size ' + item_list[i][2] + ' and we have color in ' + item_list[i][3])
			answer = input('      What do you want (Example: size: m , color: red, quantity: 3)\nMe:')
	# print ('test item.' + itenCode + str(item_list[1]))

def orderCheck(answer):
	orderDetail = answer.split(',')
	print(orderDetail)
	
def contextCheck(wordProc, hello_list):
	# Variable declaration

	shipping_list = ['kerry','ems','dhl']
	ordering_list = ['buy','order','purchase']
	itemCode_list = ['IC1234','IC1244']
	
	# itemCode_list = {
		# "IC1234": {
			# "products": "T-shirt",
			# "size": "S M L",
			# "color": "Red"
		# }
	# }
	
	# itemCode_list.update({
		# "IC1244": {
			# "products": "T-shirt",
			# "size": "S M L",
			# "color": "Red"
		# }
	# })
	
	# for key,value in itemCode_list.items():
		# print('Code: ' + str(key) + ',' + str(value))
	
	# print(itemCode_list)
	
	retProcess = {}
	
	notUnderstandCount = 0
	
	# for check
	for i in wordProc:
		if i.lower() in hello_list :
			retProcess.update({1:'greeting'})
		elif i.lower() in ordering_list:
			retProcess.update({3:'ordering'})
		elif i.lower() == 'suggest':
			retProcess.update({4 : 'suggesting'})
		elif i.lower() == 'goodbye':
			retProcess.update({2 : 'ending'})
		elif i in itemCode_list:
			retProcess.update({99:i})
		else :
			notUnderstandCount += 1
	if notUnderstandCount == len(wordProc):
		retProcess.update({5:'notUnderstand'})
	# print(retProcess)
	return max(retProcess.items(), key=operator.itemgetter(1))[1]
		
def soundex_input(name):
	name = name.upper()
	soundex = ""
	if len(name) > 0:
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
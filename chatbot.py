import random
import re
import operator

def main():
	# item_list = ['t-shirt','pants']s
	hello_list = ['halo','hello','bello','yo','hi']
	item_list = [['IC1234','T-shirt','S,M,L','Red'],['IC2341','Pant','S,M,L','Blue'] ]
	# shipping_list = ['ems','kerry','dhl']
	
	endConversation = False

	print("Shop: Hi, I'm a bot. Call me SellingBot.")
	# print("Shop: How can I help you.")
	
	while endConversation == False:
		text = input('Me(Home): ')
		print()
		
		text = re.sub('[!@#$,]', '', text) # clean sentence (not alphabet)
		proc = text.split(' ')
		retCheck = contextCheck(proc,item_list)
		# print (retCheck)
		
		# for i in proc:
			# print (soundex_input(i))
		if retCheck == 'greeting':
			helloIndex = random.randint(0,len(hello_list)-1)
			print('Shop: ' + hello_list[helloIndex] + ', can I help you?')
		elif retCheck == 'agree':
			print('Shop: what?')
		elif retCheck == 'no':
			print('Shop: What?')
		elif retCheck == 'ordering':
			print("Shop: Okay Good, then you can look at the store and copy the item code and I will send you a detail.")
		elif retCheck == 'suggesting':
			print('Shop: Sorry, this feature is not available now (Upgrade to vip to unlock)')
			# x = random.randint(0,1)
			# print("Shop: " + item_list[x] + ' is suggested for you.')
			# print("Shop: Do you like it ?")
			
			# retVal = ''
			# while retVal != 'agree' and retVal != 'no':
				# comfirmCheck = input('Me: ')
					
				# retVal = contextCheck(comfirmCheck.split(' '))
				# if retVal == 'agree':
					# print('Shop: Okay, I recorded it, the owner will contract you shortly, thank you :)')
					# print('Shop: Tell me if you want anything')
				# if retVal == 'no':
					# print('Shop: Okay, tell me if you want some thing')

			# if ans.lower() in agree_list :
				# print("Shop: Do you like to order now?")
				# ans = input('Me: ')
				# ans_proc = ans.split(' ')
				# for j in ans_proc:
					# if j in agree_list:
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
			# else :
				# print ("Shop: Okay, I'm sorry")
		elif retCheck == 'notUnderstand':
			print ('Shop: Sorry, I cannot understand it.')
		elif retCheck == 'ending':
			print('Shop: see you later')
			endConversation = True
			exit(0)
		else :
			checkItemCodeDetail(retCheck,item_list)
			
def cleanWord(sentence):
	for alpha in sentence:
		if not alpha.isalpha():
			print(alpha)
			sentence.replace('!','')
	print (sentence)
	
def checkItemCodeDetail(itemCode,item_list):
	# item_list = [['IC1234','T-shirt','S,M,L','Red'],['IC2341','Pant','S,M,L','Blue'] ]
	check = -1
	for i in range(0,len(item_list)):
		if itemCode == item_list[i][0]:
			print ('Shop: This item is a ' + item_list[i][1] + ' and we have size ' + item_list[i][2] + ' and we have color in ' + item_list[i][3])
			while check == -1:
				answer = input('      What do you want (Example: size: m , color: red, quantity: 3)\nMe:')
				print()
				check = orderCheck(itemCode,item_list[i][1],answer)
	# print ('test item.' + itenCode + str(item_list[1]))

def orderCheck(itemcode,products,answer):
	orderDetail = [x.strip() for x in answer.split(',')]
	# print(orderDetail)
	if len(orderDetail) != 3:
		print('Shop: Invalid Input please input like the example')
		return -1
	else:
		eachDetail = []
		for each in orderDetail:
			eachDetail.append(each.split(':'))
		# print (eachDetail)
		print('Shop: You odered ' + products + ' with size ' + eachDetail[0][1].upper() + ' color ' + eachDetail[1][1].upper() + ' amount ' + eachDetail[2][1])
		# comfirmCheck = input('Shop: That right?\nMe:')
		retVal = ''
		while retVal != 'agree' and retVal != 'no':
			if retVal == '':
				comfirmCheck = input('Shop: That right?\nMe:')
				print()
			else:
				comfirmCheck = input('Shop: What did you say?\nMe:')
				print()
				
			retVal = contextCheck(comfirmCheck.split(' '))
			if retVal == 'agree':
				print('Shop: Okay, I recorded it, the owner will contract you shortly, thank you :)')
				print('Shop: Tell me if you want anything')
			if retVal == 'no':
				print('Shop: Okay, tell me if you want some thing')
		return 1
	
def contextCheck(wordProc,itemCode_list):
	# Variable declaration
	agree_list = ['yes','sure','of course']
	hello_list = ['halo','hello','bello','yo','hi']
	no_list = ['no','not yet','not now','next time','nothing']
	
	shipping_list = ['kerry','ems','dhl']
	ordering_list = ['buy','order','purchase']
	itemCode_list = ['IC1234','IC2341']
	
	# print(itemCode_list)
	
	retProcess = {}
	
	notUnderstandCount = 0
	
	# for check
	for i in wordProc:
		if i.lower() in hello_list :
			retProcess.update({1:'greeting'})
		elif i.lower() in agree_list:
			retProcess.update({1:'agree'})
		elif i.lower() in no_list:
			retProcess.update({1:'no'})	
		elif i.lower() in ordering_list:
			retProcess.update({3:'ordering'})
		elif i.lower() == 'suggest':
			retProcess.update({4 : 'suggesting'})
		elif i.lower() == 'goodbye':
			retProcess.update({2 : 'ending'})
		elif i in itemCode_list	:
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
from tkinter import *
import random
import re
import operator

hello_list = ['halo','hello','bello','yo','hi']
item_list = [['IC1234','T-shirt','S,M,L','Red'],['IC2341','Pant','S,M,L','Blue'] ]

window = Tk()
messages = Text(window)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)
frame = Frame(window) 
messages.insert(INSERT,"Shop: Hi, I'm a bot. Call me SellingBot.\n")

def Enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    messages.insert(INSERT, 'ME: %s\n' % input_get)
    input_user.set('')
    check = contextCheck(input_get.split(' '),item_list)
    messages.insert(INSERT, 'ME: %s\n' % check)
    replys = reply(check)
    messages.insert(INSERT, 'Shop: %s\n' % replys)
    return "break"

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
		
def reply(inputs):
	if inputs == 'greeting':
		helloIndex = random.randint(0,len(hello_list)-1)
		return (hello_list[helloIndex] + ', can I help you?')
	elif inputs == 'agree':
		return (' what?')
	elif inputs == 'no':
		return (' What?')
	elif inputs == 'ordering':
		return (" Okay Good, then you can look at the store and copy the item code and I will send you a detail.")
	elif inputs == 'suggesting':
		return (' Sorry, this feature is not available now (Upgrade to vip to unlock)')
	elif inputs == 'notUnderstand':
		return ('Shop: Sorry, I cannot understand it.')
	elif inputs == 'ending':
		return ('Shop: see you later')
		endConversation = True
		exit(0)
	else :
		checkItemCodeDetail(inputs,item_list)

def checkItemCodeDetail(itemCode,item_list):
	# item_list = [['IC1234','T-shirt','S,M,L','Red'],['IC2341','Pant','S,M,L','Blue'] ]
	check = -1
	for i in range(0,len(item_list)):
		if itemCode == item_list[i][0]:
			messages.insert(INSERT,'Shop: This item is a ' + item_list[i][1] + ' and we have size ' + item_list[i][2] + ' and we have color in ' + item_list[i][3] + '\n')
			while check == -1:
				messages.insert(INSERT, '      What do you want (Example: size: m , color: red, quantity: 3\n')
				answer = input('')
				print()
				check = orderCheck(itemCode,item_list[i][1],answer)
	# print ('test item.' + itenCode + str(item_list[1]))

def orderCheck(itemcode,products,answer):
	orderDetail = [x.strip() for x in answer.split(',')]
	# print(orderDetail)
	if len(orderDetail) != 3:
		messages.insert(INSERT,'Shop: Invalid Input please input like the example\n')
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

input_field.bind("<Return>", Enter_pressed)
frame.pack()
window.mainloop()
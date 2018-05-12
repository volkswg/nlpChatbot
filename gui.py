from tkinter import *
import random
import re
import operator

global chatState
global itemcodeRe
global product
chatState = 'home'

hello_list = ['halo','hello','bello','yo','hi']
agree_list = ['yes','sure','of course','okay','ok','yep']
no_list = ['no','not yet','not now','next time','nothing']

item_list = [['IC1234','T-shirt','S,M,L','Red'],['IC2341','Pant','S,M,L','Blue'] ]

window = Tk()
messages = Text(window)
messages.pack()

input_user = StringVar()

input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)
frame = Frame(window) 

def insertWord(input):
	messages.configure(state="normal")
	messages.insert(INSERT, '%s' % input)
	messages.configure(state="disabled")
insertWord("Shop: Hi, I'm a bot. Call me SellingBot.\n")


def Enter_pressed(event):
	global itemcodeRe
	global product
	input_get = input_field.get()
	messages.configure(state="normal")
	messages.insert(INSERT, 'ME: %s\n\n' % input_get)
	messages.configure(state="disabled")
	# print(input_get)
	if chatState == 'home':
		check = contextCheck(input_get.split(' '),item_list)
		itemcodeRe,product = reply(check)
	elif chatState == 'orderDetail':
		print('hey' + itemcodeRe + product)
		orderCheck(itemcodeRe,product,input_get)
	elif chatState == 'confirmOrder':
		confirmOrder(input_get)
		print ('confirmOrder')
	input_user.set('')
	return "break"

def contextCheck(wordProc,itemCode_list):
	# Variable declaration
	
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
	global chatState
	if inputs == 'greeting':
		helloIndex = random.randint(0,len(hello_list)-1)
		insertWord('Shop: '+hello_list[helloIndex] + ', can I help you?\n')
	elif inputs == 'agree':
		insertWord('Shop: what?\n')
	elif inputs == 'no':
		insertWord('Shop: What?\n')
	elif inputs == 'ordering':
		insertWord("Shop: Okay Good, then you can look at the store and copy the item code and I will send you a detail.\n")
	elif inputs == 'suggesting':
		insertWord('Shop: Sorry, this feature is not available now\n')
	elif inputs == 'notUnderstand':
		insertWord('Shop: Sorry, I cannot understand it.\n')
	elif inputs == 'ending':
		insertWord('Shop: see you later')
		endConversation = True
		exit(0)
	else :
		chatState = 'orderDetail'
		print(chatState)
		check = checkItemCodeDetail(inputs)
		if check != None:
			return inputs,check
	return None,None
		

def checkItemCodeDetail(itemCode):
	check = -1
	for i in range(0,len(item_list)):
		if itemCode == item_list[i][0]:
			insertWord('Shop: This item is a ' + item_list[i][1] + ' and we have size ' + item_list[i][2] + ' and we have color in ' + item_list[i][3] + '\n')
			insertWord('      What do you want (Example: size: m , color: red, quantity: 3)\n')
			return item_list[i][1]

def orderCheck(itemcode,products,answer):
	global chatState
	orderDetail = [x.strip() for x in answer.split(',')]
	if len(orderDetail) != 3:
		insertWord('Shop: Invalid Input please input like the example\n')
		return -1
	else:
		eachDetail = []
		for each in orderDetail:
			eachDetail.append(each.split(':'))
		insertWord('Shop: You odered ' + products + ' with size ' + eachDetail[0][1].upper() + ' color ' + eachDetail[1][1].upper() + ' amount ' + eachDetail[2][1])
		insertWord('\nShop: That right?\n')
		chatState = 'confirmOrder'
		return
		
def confirmOrder(input):
	global chatState
	retVal = contextCheck(input.split(' '),item_list)
	if retVal == 'agree':
		insertWord('Shop: Okay, I recorded it, the owner will contract you shortly, thank you :)\n')
		insertWord('Shop: Tell me if you want anything\n')
		chatState = 'home'
		return 1
	if retVal == 'no':
		insertWord('Shop: Okay, tell me if you want some thing\n')
		chatState = 'home'
		return 1
	else:
		insertWord('Shop: What did you say? Please confirm to me\n')
	

input_field.bind("<Return>", Enter_pressed)
# input_field.config(state=DISABLED)
frame.pack()
window.mainloop()
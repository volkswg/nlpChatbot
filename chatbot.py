import random

no_list = ['no','not yet','not now','next time','no,']
hello_list = ['hi','halo','hello','bello','yo']
item_list = ['t-shirt','pants']
agree_list = ['yes','sure','of course']
print("Hi, I'm a bot. Call me SellingBot.")
print("How can I help you.")
while True:
	text = input('Enter: ') #What products are you have?
	proc = text.split(' ')
	for i in proc:
		if i.lower() in hello_list :
			print("Hello ")
		if i.lower() == 'buy':
			for i in proc:
				if i.lower() == 'something' or i.lower() == 'product':
					print("Now we have : ")
					print("ID	 Product	Size 	 Color	 	Quantity")
					print("001	 T-shirt 	S,M,L    Black	 	10")
					print("002	 Pants 		S,M,L   red,blue 	10")
		if i.lower() == 'suggest':
			x = random.randint(1,3)
			print(item_list[x] + ' is suggested for you.')
			print("Do you like it ?")
			ans = input('Enter: ')
			if ans.lower() in agree_list :
				print("Do you like to order now?")
				ans = input('Enter: ')
				ans_proc = ans.split(' ')
				for j in ans_proc:
					if j in agree_list:
						print("Order me")
						ans2 = input('Enter: ')
						ans_proc2 = ans.split(' ')
						for k in ans_proc2 :
							if k in item_list:
								 

				



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
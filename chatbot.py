print("Hi, I'm a bot. Call me SellingBot.")
print("How can I help you.")
while True:
 text = input('Enter: ') #What products are you have?
 proc = text.split(' ')
 for i in proc:
  if i.lower() == 'hello' or i.lower() == 'hi' :
   print("Hello")
  if i.lower() == 'buy':
   for i in proc:
    if i.lower() == 'something' or i.lower() == 'product':
     print("Now we have : ")
     print("ID  Product Size   Color   Quantity")
     print("001  T-shirt  S,M,L    Black   10")
     print("002  Pant   S,M,L   red,blue  10")
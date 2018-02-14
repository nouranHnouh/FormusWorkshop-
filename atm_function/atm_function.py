#this program is atm that withdraw any money amount 
#allowed papers: 100,50,10,5, and the rest of requests 
def withdraw(balance,request):
	if request>balance:
		print "can`t give you all this money"
	while request>0:
		if request>=100:
			request-=100
			print "give 100"
		elif request>=50:
			request-=50
			print "give 50"
		elif request>=10:
			request-=10
			print "give 10"
		elif request>=5:
			request-=5
			print "give 5"
		elif request<5:
			request-=3
			print "give 2"
	return balance-request

balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)




			





		
	
	



	
     



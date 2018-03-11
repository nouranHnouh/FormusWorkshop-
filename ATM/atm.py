#this program is atm that withdraw any money amount 
#allowed papers: 100,50,10,5, and the rest of requests 
money_amount=500 #balance in atm 
request=int(raw_input("enter your request :"))
if request<=0:
	print "Invalid request"
while request>0:
	#your request should be less than your balance
	if request<=money_amount:

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
		
			



		
	
	



	
     



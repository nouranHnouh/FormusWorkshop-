class Atm():
	"""class Atm has information about Atm such as balance and the name of the bank"""
	#define constructor that set balance to givin account balance
	#and set the name of the bank 
	def __init__(self,balance,name_of_bank):
		self.balance=balance
		self.nameBank=name_of_bank
	#withdraw method takes the request of money, print how much mony the atm will give you
	#return the current balance after withdraw 
	def withdraw(self,request):
		#check if request of mony is less than balnace print an error message 
		if request>self.balance:
			print "can`t give you all this money"
		elif request<=0:
			print "More than Zero" 
		else:
			self.balance-=request 
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
				else:
					print "give"+str(request)
					request=0
					
		print "--------------------------------------"
		return self.balance
#define balance		
balance1=500
balance2=1000
#instnaces of class atm
print "\n" 
atm1=Atm(balance1,"Smart Bank")
print ("Welecom to "+ atm1.nameBank)
print ("current blanace "+str(atm1.balance))
atm1.withdraw(200)

atm2=Atm(balance2," TD Bank")
print ("Welecom to "+ atm2.nameBank)
print ("current blanace "+str(atm2.balance))

atm2.withdraw(500)
atm2.withdraw(500)







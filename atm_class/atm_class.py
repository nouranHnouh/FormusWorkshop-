class Atm():
	def __init__(self,balance,name_of_bank):
		self.balance=balance
		self.nameBank=name_of_bank
	
	def withdraw(self,request):
		if request>self.balance:
			print "can`t give you all this money"
		else:
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
		return self.balance-request

balance1=500
balance2=1000

#instnaces of class atm
atm1=Atm(balance1,"Smart Bank")
print ("Welecom to "+ atm1.nameBank)
print ("current blanace "+str(atm1.balance))
atm1.withdraw(277)

atm2=Atm(balance2," TD Bank")
print ("Welecom to "+ atm2.nameBank)
print ("current blanace "+str(atm2.balance))
atm2.withdraw(800)
atm2.withdraw(2000)


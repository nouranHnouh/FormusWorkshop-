#prime function take number as input and return if the number is 
#prime or not 
def primality(num):
	if num>1:
		for i in range (2,num):
			if (num%i)==0:
				number= str(num)+"  is not a prime number "
				break
			else:
				number=str(num)+"  is a prime number"
	else:
		number=str(num)+"  is not a prime number"
	return number
	#get the number from the user
number=int(raw_input("Enter a number :"))
print primality(number)
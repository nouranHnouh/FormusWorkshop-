class Memberstore():
	#store members
	members=[]
	
	def add(self,member):
		#add the members 
		return Memberstore.members.append(member)
				
	def get_all(self):
		#get all the members
		return Memberstore.members
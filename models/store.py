class Memberstore():
	#store members
	members=[]
	las_id=1
	def __str__(self):
		return "From str method of Memberstore :members is %s, b is %s" %(Memberstore.members,Memberstore.las_id)
	def __repr__(self):
		return "<Memberstore members:%s las_id %s>"%(Memberstore.members,Memberstore.las_id)
		
	def add(self,member):
		#add the members and their id to the list 
		member.id=Memberstore.las_id
		Memberstore.members.append(member)
		Memberstore.las_id+=1 
	

	def get_all(self):
		#get all the members
		#print (Memberstore.members)
		return Memberstore.members

	"""method that return member id """
	def get_by_id(self,id):
		all_members=self.get_all()
		result=0
		for member in all_members:
			if member.id==id:
				result=member 
				break 
		return result 

	"""method check if member exist in the list"""
	def entity_exist(self,member):
		result = False
		if self.get_by_id(member.id) is None:
			result = True
		return result


	def delete(self,id):
		all_members=self.get_all()
		id_member=self.get_by_id(id)
		all_members.remove(id_member)

			






class Memberstore():
	#store members
	members=[]
	las_id=1
	
	def add(self,member):
		#add the members and their id to the list 
		member.id=Memberstore.las_id
		Memberstore.members.append(member)
		Memberstore.las_id+=1 
	

	def get_all(self):
		#get all the members
		return Memberstore.members

	"""method that return member id """
	def get_by_id(self,id):
		all_members=self.get_all()
		result=0
		for m in all_members:
			if m.id==id:
				result=m
				break 
		return result 

	"""method check if member exist in the list"""
	def entity_exist(self,member):
		result=True 
		all_members=self.get_all()
		if member in all_members:
			result=True 
		else:
			result=False
		return result 

	def delete(self,id):
		all_members=self.get_all()
		id_member=self.get_by_id(id)
		if id in id_member:
			all_members.remove(id_member)

			






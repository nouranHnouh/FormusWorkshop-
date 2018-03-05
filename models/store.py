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
		result=None
		for member in all_members:
			if member.id==id:
				result=member 
				break 
		return result 
	"""get member by name,and return it """
	def get_by_name(self,name):
		all_members=self.get_all()
		result=[]
		for member in all_members:
			if member.name==name:
				result.append(member)
		return result 
    #update post data
	def update(self,member):
		member_id=member.id 
		for m in Memberstore.members:
			if m.id==member_id: 
				m.name=member.name
				m.age=member.age
				print "your profil has been updated "

	"""method check if member exist in the list"""
	def entity_exist(self,member):
		result = True 
		if self.get_by_id(member.id) is None:
			result = False
		return result


	def delete(self,id):
		all_members=self.get_all()
		id_member=self.get_by_id(id)
		all_members.remove(id_member)


class Poststore():
	"""class poststore has store the members posts in posts list"""
	posts=[] 
	last_id=1 # get post by id 

	#get all method get all the post 
	def get_all(self):
		return Poststore.posts
    #add the posts
	def add(self,post):
		post.id=Poststore.last_id
		Poststore.posts.append(post)
		Poststore.last_id+=1
		
		#returns posts id 
	def get_by_id(self,id):
		all_post=self.get_all()
		result=None 
		#loop through all the posts
		for post in all_post:
			if post.id==id:
				result=post
				break
		return result
    
	
    #delete post by id 
	def delete(self,id):
		all_post=self.get_all()
		post_id=self.get_by_id(id)
		all_post.remove(post_id) 
	#update post data
	def update(self,post):
		post_id=post.id 
		for p in Poststore.posts:
			if p.id==post_id:
				p.title=post.title
				p.content=post.content
				print "you have updated your post"














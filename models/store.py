import itertools

class Memberstore():
	#store members
	members=[]
	last_id=1
	def __str__(self):
		return "From str method of Memberstore :members is %s, b is %s" %(Memberstore.members,Memberstore.las_id)
	def __repr__(self):
		return "<Memberstore members:%s las_id %s>"%(Memberstore.members,Memberstore.las_id)
		
	def add(self,member):
		#add the members and their id to the list 
		member.id=Memberstore.last_id
		Memberstore.members.append(member)
		Memberstore.last_id+=1 
	

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
		for member in all_members: 
			if member.name==name:
				yield member 
    #update post data
	def update(self,member):
		result=member
		all_members=self.get_all()
		for m,current_member in enumerate(all_members):
			if member.id==current_member.id: 
				all_members[m]=member 
				break
		return result 


	"""method check if member exist in the list"""
	def entity_exist(self,member):
		result = True 
		if self.get_by_id(member.id) is None:
			result = False
		return result

    #delete member 
	def delete(self,id):
		all_members=self.get_all()
		id_member=self.get_by_id(id)
		all_members.remove(id_member)
    
    #get_members_with_post method returns the member with their corresponding post
	def get_members_with_posts(self,all_posts):
		all_members=self.get_all()
		for member,post in itertools.product(all_members,all_posts):
			if member.id==post.member_id:
				member.posts.append(post)
		for member in all_members:
			yield member 
	
	#get top 2 people who wrote more posts 
	def get_top_two(self,posts):
		#create list
		storted_members=list(self.get_members_with_posts(posts))
		#sort list, from members with most written posts
		storted_members.sort(key=lambda member:member.posts,reverse=True)
		yield storted_members[0]
		yield storted_members[1]

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
		all_post=self.get_all()
		result=post 
		for p,current_post in enumerate(all_post):
			if post.id==current_post.id:
				all_post[p]=post
				break
		return result

   
















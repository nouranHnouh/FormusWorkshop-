class Member():
	
	""" this class has the following members attributes:
	name of the member and age of the member"""
	def __init__(self,name,age):
		self.name=name
		self.age=age 
		#list of the post 
		self.posts=[]
		self.id=0
	def __str__(self):
		return 'Name:{}\nAge: {}'.format(self.name,self.age)
	def __repr__(self):
		return "<name:%s age %s>"%(self.name,self.age)
		
class Post():
	def __init__(self,title,content,member_id):
		self.title=title
		self.content=content
		self.member_id=member_id
		self.id=0

	def __str__(self):
		return 'Title: {} \nContent: {}'.format(self.title, self.content)
	def __repr__(self):
		return "<title:%s content %s>"%(self.title,self.content)	


		


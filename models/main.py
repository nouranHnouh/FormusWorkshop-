import models
import store

"""function create members takes three members as input 
and create them using Member class."""

def create_members():
	member1=models.Member("Karen",19)
	member2=models.Member("Jhon",23)
	member3 =models.Member('Nour', 28)
	return member1,member2,member3

"""add_members takes two list and use for loop to add members
one by one"""
def add_members(members,store_members):
	for m in members:
		store_members.add(m) 
	return store_members

"""get_members get all members in the list"""
def get_members():
	get_member=store.Memberstore()
	print (get_member.get_all()) 


"""create instances and call functions"""
member_instances=create_members()
members_store=store.Memberstore()
add_members(member_instances,members_store)
get_members() 


post1=models.Post("python list", "python list offers a way to structure data")
post2=models.Post("writing algorithm", "writing alogarithm is very effective when it comes to analyzing problems")
post3=models.Post("classes in python ", " classes is a template that has information like variables and functions")
post4=models.Post("Inheretance", "How can I inherete a class in python ")

#testing 
"""print member1.name
print member1.age
print member2.age
print post1.title
print post1.content
print post2.content"""







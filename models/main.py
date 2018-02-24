import models
import store

"""function create members takes three members as input 
and create them using Member class."""

def create_members():
	member1=models.Member("Karen",19)
	member2=models.Member("Jhon",23)
	member3 =models.Member('Nour', 28)
	print(member1)
	print(member2)
	print(member3) 
	return member1,member2,member3

"""add_members takes two list and use for loop to add members
one by one"""
def add_members(members,store_members):
	for m in members:
		store_members.add(m)
	#print store_members 
	return store_members

"""get_members get all members in the list"""
def get_members():
	get_member=store.Memberstore()
	print (get_member.get_all()) 

"""get id function takes list and id as input 
it gets the id in the list"""
def get_id(member,id): 
	print (member.get_by_id(id)) 
def delete(all_member,member):
	if all_member.entity_exist(member):
		all_member.delete(member.id) 
	else:
		print (all_member.entity_exist(member))


"""create instances and call functions"""
member_instances=create_members()
#testing 
member1=member_instances
member2=member_instances
members_store=store.Memberstore()
add_members(member_instances,members_store)
get_members() 
get_id(members_store,3)
delete(members_store,member2)



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







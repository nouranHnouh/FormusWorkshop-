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
def get_members(memeber_store):
	print (memeber_store.get_all()) 

"""get id function takes list and id as input 
it gets the id in the list"""
def get_id(member_store,id): 
	print (member_store.get_by_id(id))
"""check if entity exist, it takes two input a list and a string member
check if entity exist in a list"""
def check_entity(member_store,member):
        print (member_store.entity_exist(member))

def delete (all_member,id):
	all_member.delete(id) 
	


	
"""create instances and call functions"""
member_instances=create_members()

#testing 
#member1 = models.Member("Hamed", 22)
member1,member2,member3=member_instances
members_store=store.Memberstore()
add_members(member_instances,members_store)
get_members(members_store) 
get_id(members_store,1)
get_id(members_store,2)
check_entity(members_store,member1)
<<<<<<< HEAD
delete(members_store,2)

check_entity(members_store,member2)
get_members(members_store) 
||||||| update
delete(members_store,member1)
get_members(members_store)
=======
delete(members_store,1)
get_members(members_store)
>>>>>>> master


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







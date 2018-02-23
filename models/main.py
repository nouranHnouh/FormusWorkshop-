import models
import store 
#returns members 
def create_members():
	member1=models.Member("Karen",19)
	member2=models.Member("Jhon",23)
	return member1,member2

#add members takes two lists
def add_members(members_list,members_store):
	for x in members_list:
		member_store.add(x) 
def print_list(member):
	#print members list
	for i in member:
		print (i)
def get_all_members(mylist):
	#get members 
	#call print list
	print_list(mylist.get_all())





	


member_instances=create_members()
member_store=store.Memberstore()
add_members(member_instances,member_store)
get_all_members(member_store) 


#testing 
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



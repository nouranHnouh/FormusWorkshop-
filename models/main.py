import models
import store

member1=models.Member("Karen",19)
member2=models.Member("Jhon",23)
member3 = models.Member('Nour', 28)


member_store = store.Memberstore()
member_store.add(member1)
member_store.add(member2)
member_store.add(member3)
print (member_store.get_all())


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







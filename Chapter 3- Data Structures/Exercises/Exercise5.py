guests=['shahul', 'adhil', 'abdu'] 

name = guests[0].title()
print(name + ",can u come for dinner.") 

name = guests[1].title() 
print(name + ",can u come for dinner.") 

name = guests[2].title() 
print(name + ",can u come for dinner.") 

name = guests[1].title() 
print(" Sorry, + name + can't make it to dinner.") 

#Jack can't make it! Let's invite Gary instead. 
del(guests[1]) 
guests.insert(1, 'tom shelby') 

# Print the invitations again. 
name = guests[0].title() 
print("\n" + name + ", can u come for dinner.") 

name = guests[1].title() 
print (name + ", can u come for dinner.") 

name = guests[2].title() 
print(name + ", can u come for dinner.")

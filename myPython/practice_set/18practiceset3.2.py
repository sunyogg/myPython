#3.4
'''invitation=['nana','dada','dadi','nani']
print("hello",invitation[0],invitation[1],"i would like to invite you to my birthday,please come")
print("hello",invitation[2],invitation[3],"please come to my birthday party")

#3.5
guest=['aman','raman','chaman','pawan','suman','suyog']
rejectguest=guest.pop(-2)
guest.insert(4,'shubham')
print(guest)
print("hello",guest[0],"please come to my party")
print("hello",guest[1],"please come to my party")
print("hello",guest[2],"please come to my party")
print("hello",guest[3],"please come to my party")
print('hello',guest[4],"please come to my party")
print('hello',guest[5],'please come to my party')
print(rejectguest,'will not be able to come to the party')

#3.6 shrinking list
guest=['aman','raman','chaman','pawan','suman','suyog']
print("hello guys i just found a bigger dinning table, so more people will be coming")
guest.insert(0,'prasoon')
guest.insert(4,'mohit')
guest.append('kapil')
print("so the names of people are",guest)
print("hello",guest[0],"please come to my party\nhello",guest[1],"please come to my party\nhello",guest[2],"please come to my party\nhello",guest[3],"please come to my party\nhello",guest[4],"please come to my party\nhello",guest[5],"please come to my party\nhello",guest[6],"please come to my party\nhello",guest[7],"please come to my party")'''

#3.7 expanding list
guest=['prasoon', 'aman', 'raman', 'chaman', 'mohit', 'pawan', 'suman', 'suyog', 'kapil']
print("sorry i guys the new dinning table wont be ready in time, i can only invite two people now")
poppedguest1=guest.pop(1)
print("i am really sorry",poppedguest1,"but i cant invite you due space issue")
poppedguest2=guest.pop(2)       
print("i am really sorry",poppedguest2,"but i cant invite you due space issue")    
poppedguest3=guest.pop(3)          
print("i am really sorry",poppedguest3,"but i cant invite you due space issue")
poppedguest4=guest.pop(3)                                                                          
print("i am really sorry",poppedguest4,"but i cant invite you due space issue")
poppedguest5=guest.pop(2)    
print("i am really sorry",poppedguest5,"but i cant invite you due space issue")
poppedguest6=guest.pop(1)         
print("i am really sorry",poppedguest6,"but i cant invite you due space issue")
poppedguest7=guest.pop(2) 
print("i am really sorry",poppedguest7,"but i cant invite you due space issue") 

#TRICKY SITUATION(index error, pop index out of range)
#solution=harr ek baar item pop karne ke baad index number change ho jata hai  
#to list ko har ek item pop karne ke baad print kar liya karo taaki naye
#index number pata chal jaaye

print("however",guest[0],"is still coming")
print("and also",guest[1],"is still coming")

del guest[0]
del guest[0]

print(guest)

#8.9
def show_messages(lists):
    for list in lists:
        print("->",list.title())

messages = ['hi','hello','hru','hey','supp']

show_messages(messages)

#---------------------------------------------------------------------------------------

# 8.10
# moving elements of one list to another
def sendmessages(messages,sentmessages):
    while messages:
        current_message = messages.pop()
        sentmessages.append(current_message)
    print('sent_messages:',sentmessages)
    

messages = ['hi','hello','hru','hey','supp']
sent = []

sendmessages(messages[:],sent)
print(messages) # see how the original list has now become empty

#---------------------------------------------------------------------------------------
# sending a copied list into the function, by using '[:]' in the function call
#8.11
def sendmessage(messages,sent):
    while messages:
        currentmessage = messages.pop()
        sent.append(currentmessage)
    print(sent)


messagess = ['hi','hello','hru','hey','supp']
sentt = []
sendmessage(messagess[:],sentt)
print(messagess)

#---------------------------------------------------------------------------------------







#8.3

def make_tshirt(size,message):
    print("We'll print a shirt of size",size,"and with message",'"'+message+'"')

make_tshirt(36,'fake nike') #positional argument
make_tshirt(message = 'h!', size = 38)
#------------------------------------------------------------------------------------------------

#8.4
def make_tshirt(message, size = 'large'):
    print('size: ',size)
    print('message:',message)
    
make_tshirt('i love Python')
make_tshirt('i love julia','small')
#------------------------------------------------------------------------------------------------

#8.5
def describe_city(city,country = 'india'):
    print(city.title(),'is in',country.title())

describe_city('jabalpur')
describe_city('mumbai')
describe_city('los angeles','usa')
describe_city(city = 'sydney', country = 'australlia')
#------------------------------------------------------------------------------------------------

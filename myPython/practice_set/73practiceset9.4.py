
# 9.10

from restaurant import Restaurant as rst

#creating instance
restron = rst('simpsons palace','american')

#calling method
restron.describe_restaurant()
restron.open_restaurant()
restron.read_customer()
restron.set_customer_served(30)
restron.read_customer()
restron.increment_customer_served(2)
restron.read_customer()

#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# 9.11 and # 9.12

from adminalone import Admin

admin1 = Admin('sanyog','lodhi','jabalpur','indian')
admin1.describe_user()
admin1.privilege.show_privileges()


#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––




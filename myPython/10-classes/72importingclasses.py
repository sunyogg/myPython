
from caralone import Car # a separate module containing only Car class
from electriccar import ElectricCar as EC # a separate module containing ElectricCar which inherits from Car and Battery class

my_car = Car('volkswagen','beetle',2019)

my_car.get_descriptive_name()
my_car.read_odometer()
my_car.fill_gas_tank()



my_tesla = EC('tesla','model l',2020)

my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()



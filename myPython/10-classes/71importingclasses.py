from car import Car,ElectricCar
# no need to call battery since no instance will be created from Battery and if any
# it'll be stored in a variable in any of these classes

mynewcar = Car('audi','r8',2019)

mynewcar.get_descriptive_name()
mynewcar.read_odometer()
mynewcar.update_odometer(500)
mynewcar.read_odometer()
mynewcar.increment_odometer(200)
mynewcar.read_odometer()
mynewcar.fill_gas_tank()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

mynewelectric = ElectricCar('tesla','model s',2019)

mynewelectric.read_odometer()
mynewelectric.update_odometer(500)
mynewelectric.read_odometer()
mynewelectric.increment_odometer(200)
mynewelectric.read_odometer()
mynewelectric.fill_gas_tank()
mynewelectric.battery.describe_battery()
mynewelectric.battery.get_range()
mynewelectric.battery.upgrade_battery()
mynewelectric.battery.describe_battery()
mynewelectric.battery.get_range()

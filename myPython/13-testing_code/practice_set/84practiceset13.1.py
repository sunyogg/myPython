# test cities

# 11.1

import unittest
from city_functionmodule import city_country

class Testcitycountry(unittest.TestCase):
    """Test for city_country()."""


    def test_city_country(self):
        """Does names like city country work?"""
        formatted_name = city_country('california','united states')
        self.assertEqual(formatted_name,'California, United States')


if __name__ == '__main__':
    unittest.main()

#-----------------------------------------------------------------------------------------------------
# commment out 11.1 to use 11.2
# 11.2

import unittest
from city_functionmodule import city_country_pop

class Testcitycountry(unittest.TestCase):
    """Test for city_country()."""


    def test_city_country(self):
        """Does names like city country work?"""
        formatted_name = city_country_pop('california','united states')
        self.assertEqual(formatted_name,'California, United States')


    def test_city_country_pop(self):
        """Does names like city country population work?"""
        formatted_name = city_country_pop('california','united states',1000000)
        self.assertEqual(formatted_name,'California, United States - population 1000000')


if __name__ == '__main__':
    unittest.main()

#-----------------------------------------------------------------------------------------------------















# for 11.1
def city_country(city,country):
    formatted_name = f"{city}, {country}"
    return (formatted_name.title())


# for 11.2
def city_country_pop(city,country,population = ''):
    if population:
        formatted_name = f"{city.title()}, {country.title()} - population {population}"
        return (formatted_name)
    else:
        formatted_name = f"{city}, {country}"
        return (formatted_name.title())
        






#! /usr/bin/python3
def city_country(name, country):
    city_country_name = f"{name.title()}, {country.title()}"
    return city_country_name

print(city_country('santiago','chile'))
print(city_country('frankfurt','germany'))
print(city_country('madrid','spain'))
print(city_country('montreal','canada'))
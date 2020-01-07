#! /usr/bin/python3 
def describe_city(name, country="mexico"):
    print(f"{name.title()} is in {country.title()}.")

describe_city('Mexico city')
describe_city('Klamath Falls','the United States')
describe_city('trier','germany')

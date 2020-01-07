#! /usr/bin/python3 
def describe_pet(animal_type, pet_name):
    """ Display information about a pet.
    This function uses positional arguments."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'arthur')

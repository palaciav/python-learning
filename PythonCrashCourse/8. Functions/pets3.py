#! /usr/bin/python3 
def describe_pet(pet_name, animal_type='dog'):
    """Display informatoin about a pet.
    This function uses default values."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet('arthur')
describe_pet('timmy','tiger')

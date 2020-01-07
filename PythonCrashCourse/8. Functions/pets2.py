#! /usr/bin/python3
def describe_pet(animal_type, pet_name):
    """Display information about a pet.
    This script uses keyword arguments."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='emu', pet_name='ethan')

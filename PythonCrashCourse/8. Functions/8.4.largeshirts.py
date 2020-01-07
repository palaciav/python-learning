#! /usr/bin/python3
def make_shirt(size="L", message_text="I Love Python"):
    print(f"Making a shirt of size {size.upper()}, with a printed message of '{message_text.title()}'.")

make_shirt()
make_shirt('m')
make_shirt('m','Try Catch Yourself')

# Formula for Celsius to Fahrenheit:
# F = C * 9/5 + 32
def c_to_f(temp):
    return int(temp) * (9/5) + 32

print(c_to_f(input("Please enter temp in Celsius: ")))

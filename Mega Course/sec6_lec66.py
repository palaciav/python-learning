temperatures = [10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9/5 + 32
        return f

with open("temps.txt","w+") as file:
    for t in temperatures:
        temp = c_to_f(t)
        if type(temp) == float:
            file.write(str(temp)+"\n")
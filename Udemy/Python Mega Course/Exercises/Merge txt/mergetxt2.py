import glob2,datetime

filenames = glob2.glob("file*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f.txt"),"w") as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
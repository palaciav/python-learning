import glob,os,datetime
os.chdir("C:\\Users\\Adrian\\Coding\\Python\\Udemy\\Python Mega Course\\Exercises\\Merge txt")

content = ""
for file in glob.glob("file*.txt"):
    content += open(file,"r").read()
    content += "\n"
    #file.close()

filename = datetime.datetime.now()
output = open(str(filename.strftime("%Y-%m-%d-%H-%M-%S-%f.txt")),"w")
output.write(content)
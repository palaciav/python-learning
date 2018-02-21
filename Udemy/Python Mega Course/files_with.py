with open("examples.txt","a+") as file:
    file.seek(0)
    content=file.read()
    file.write("\nLine 6")

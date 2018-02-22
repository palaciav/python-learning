import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def return_def(query):
    query = query.lower()
    if query in data:
        return(data[query])
    elif len(get_close_matches(query, data.keys())) > 0:
        yn = input("Did you mean %s instead?" % get_close_matches(query, data.keys())[0])
        if yn.lower() == "y" or yn.lower() == "yes":
            return data[get_close_matches(query, data.keys())[0]]
        elif yn.lower() == "n" or yn.lower() == "no":
            return "The word does not exist, please double check it."
        else:
            return "I didn't understand your response."
    else:
        return "The word does not exist, please double check."

output = return_def(input("Please enter a word to define: "))
if type(output) == list:
    for i in output:
        print("- "+i)
else:
    print(output)
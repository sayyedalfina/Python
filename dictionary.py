from difflib import get_close_matches
import json

data = json.load(open("data.json"))

def find_meanings(key):
    if type(data[key]) == list:
        for i in data[key]:
            print(i)
    else:
        print(data[key])

print("\n\t\t\t\t\tDICTIONARY : SEARCH SOMETHING!\n")
ch = 'y'
while ch == 'y':
    key = (input("Enter the word you want to search: ")).lower()
    if key in data:
        find_meanings(key)
    else:
        close_matches = get_close_matches(key, data, cutoff=0.7)
        if close_matches == []:
            print("Not found")
        else:
            for i in close_matches:
                choice = input("Did you mean "+i+"? y/n : ").lower()
                if choice == 'n':
                    continue
                else:
                    find_meanings(i)
                    break
    ch = input("Would to like to continue searching? y/n : ").lower()

              

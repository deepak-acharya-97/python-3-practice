## Local Scope

place="Hebri"

def changeMadu():
    global place ## Global Scope
    place="Hanglur"
    print(place)

changeMadu()
print(place)
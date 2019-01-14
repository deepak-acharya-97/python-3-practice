## Local Scope

place="Hebri"

def changeMadu():
    """
    Checking Local/Global Scope
    """
    global place ## Global Scope
    place="Hanglur"
    print(place)

changeMadu()
print(place)


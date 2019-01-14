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
print(changeMadu.__doc__)

## NonLocal Scope (Ensclosing Scope) - scope which is not local/global

def valueFriendShip():
    valueFG=True
    def valueItBasedOnRegion():
        valueFR=False
        nonlocal valueFG ## Keyword for accessing non local. Otherwise this will be local scope
        valueFG=False ## changing nonlocal variable
    valueItBasedOnRegion()
    print(valueFG)

valueFriendShip()
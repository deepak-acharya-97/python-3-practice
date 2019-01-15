class UselessFriend:
    
    UselessFriend.Friends=[]

    def __init__(self, name, age, place, rating):
        self.name=name
        self.age=age
        self.place=place
        self.rating=rating
        UselessFriend.Friends.append(self)

    

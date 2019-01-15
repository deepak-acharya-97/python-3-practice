class UselessFriend:
    
    Friends=[]

    def __init__(self, name, age, place, rating):
        self.name=name
        self.age=age
        self.place=place
        self.rating=rating ## Rating is for friendship level out of 10
        UselessFriend.Friends.append(self)

uselessFriend1=UselessFriend('AAA',23,"Hanglur",8)
uselessFriend2=UselessFriend('BBB',22,"Koteshwara",8.1)

for friend in UselessFriend.Friends:
    print(friend)
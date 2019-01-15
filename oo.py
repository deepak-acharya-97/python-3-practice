class UselessFriend:
    
    Friends=[]

    def __init__(self, name, age, place, rating):
        self.name=name
        self.age=age
        self.place=place
        self.rating=rating ## Rating is for friendship level out of 10
        UselessFriend.Friends.append(self)

    def __add__(self, other):
        try:
            assert self.name==other.name, "Names Should Be Same"
            self.age=other.age?other.age:self.age
            self.place=other.place?other.place:self.place
            self.rating=other.rating?other.rating:self.rating
            return True
        except(Exception e):
            return False

uselessFriend1=UselessFriend('AAA',23,"Hanglur",8)
uselessFriend2=UselessFriend('BBB',22,"Koteshwara",8.1)
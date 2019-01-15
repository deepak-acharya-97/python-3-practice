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
            assert self.name==other.name, "Name should be equal"
            self.age=other.age if other.age else self.age
            self.place=other.place if other.place else self.place
            self.rating=other.rating if other.rating else self.rating
        except:
            print("Not Adding Two Objects as the Names aren't Equal")
        return self
    
    def __str__(self):
        result="".join(('*' for i in range(50)))+"\n"\
        +"Name  :"+self.name+"\n"\
        +"Age   :"+str(self.age)+"\n"\
        +"Place :"+self.place+"\n"\
        +"Rating:"+"".join(('*' for i in range(int(self.rating))))+ " ("+str(self.rating)+")\n"\
        +"".join(('*' for i in range(50)))+"\n"
        return result
uselessFriend1=UselessFriend('AAA',23,"Hanglur",8)
uselessFriend2=UselessFriend('BBB',22,"Koteshwara",8.1)
uselessFriend3=UselessFriend('AAA',None,"Hiriyadka",5.5)
for friend in UselessFriend.Friends: ## Not Accessible as it's private
    print(friend)
uselessFriend4=uselessFriend1+uselessFriend3
print(uselessFriend4)
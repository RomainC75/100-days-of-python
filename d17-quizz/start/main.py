class User:
    def __init__(self, id, username) -> None:
        self.id=id
        self.username=username
        self.follower=0
        self.following=0
    
    def follow(self, user):
        user.follower+=1
        self.following+=1
        
        

user_1=User("001","ange")
user_2=User("002","bob")

user_1.follow(user_2)




print(user_1.follower, user_1.following)
print(user_2.follower, user_2.following)

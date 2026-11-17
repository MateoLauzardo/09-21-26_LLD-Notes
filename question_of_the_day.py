

class User():

    def __init__(self, name):
        self.name = name
        self.followers = set()
        self.following = set()



class Network():

    def __init__(self):
        self.hashset = set() # user hashset 

    #NOTE user is an "User" object "aggregation"
    def add_user(self, user):
        self.hashset.add(user.name) 

    #NOTE follower i& followee are both objects 
    def follow(self, follower, followee):

        # if a string is in an objects array 
        if follower.name in followee.followers:
            return False 
        
        elif follower.name == followee.name:
            return False 
        
        elif follower.name not in self.hashset or followee.name not in self.hashset:
            return False
        
        else:
            followee.followers.add(follower.name)
            follower.following.add(followee.name)
            return True 


    def followers_of(self, user):
        followers = user.followers
        return sorted(followers)


    def common_following(self, u1, u2):
        common_followers = []

        for people in u1.following:
            if people in u2.following:
                common_followers.append(people)


        return common_followers



a = User("ana")
b = User("ben")
c = User("cy")
d = User("dan")
net = Network()
for u in [a, b, c]:
    net.add_user(u)
print(net.follow(a, c))
print(net.follow(b, c))
print(net.follow(a, b))
print(net.follow(a, d))
print(net.follow(a, a))
print(net.followers_of(c))
print(net.common_following(a, b))
del net
print(a.name)


# True
# True
# True
# False
# False
# ['ana', 'ben']
# ['cy']
# ana
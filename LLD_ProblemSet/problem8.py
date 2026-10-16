# Write a class UserProfile that requires a username and accepts any number of extra keyword arguments using **kwargs. 
# Every keyword argument should become an attribute on the object. 
# Add a method to_dict() that returns a dictionary containing the username and every extra attribute that was passed 

class UserProfile():
    def __init__(self, username, **kwargs):
        self.username = username
        self.values = kwargs
        self.city = kwargs.get("city")
        self.age = kwargs.get("age")
        
        
    def to_dict(self):
        return self.values
        
        
user = UserProfile("ana", age=25, city="Miami")
print(user.username)
print(user.city)
print(user.age)
print(user.to_dict())

# {'username': 'ana', 'age': 25, 'city': 'Miami'}

class User:

    def __init__(self, addres,objectName,user):
        self.address = addres
        self.thingverseUsername = ""
        self.userID = user
        self.password = "pending"

    def __str__(self):
        return f"User: {self.userID}, Address: {self.address}, Object Name: {self.thingverseUsername}, Password: {self.password}"

    


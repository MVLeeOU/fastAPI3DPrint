
from app.stlsManager import CalculateCost
class User:

    def __init__(self, addres,objectName,user):
        self.address = addres
        self.thingverseUsername = ""
        self.userID = user
        self.password = "pending"

    def __str__(self):
        return str({"addres":self.address})

    def calculateCost(self):
        CalculateCost(self.stlFilePath)

    
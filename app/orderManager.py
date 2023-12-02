
from app.stlsManager import CalculateCost
class Order:

    def __init__(self, addres,objectName,user):
        self.address = addres
        self.price = 0.0
        self.stlFilePath = objectName
        self.userID = user
        self.status = "pending"

    def __str__(self):
        return str({"addres":self.address})
    
    def confirmPayment(self):
        self.status = "paid"

    def confirmShipment(self):
        self.status = "shipped"

    def calculateCost(self):
        CalculateCost(self.stlFilePath)


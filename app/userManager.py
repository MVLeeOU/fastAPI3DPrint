from app.orderManager import *
from fastapi.exceptions import HTTPException
class User:
    def __init__(self, addres:Address,user:str,password:str):
        self.address = addres
        self.thingverseUsername = ""
        self.userID = user
        self.password = password
        self.objects = {}
        self.orders = {}

    def __str__(self):
        return f"User ID: {self.userID} ,Address: {self.address} ,Thingverse Username: {self.thingverseUsername} ,Password: {self.password} ,Objects: {self.objects}, Orders: {self.orders}"

    
    @staticmethod
    def find_user_by_id(cls, target_user_id):
        for user in cls:
            if user.userID == target_user_id:
                return user
        return None
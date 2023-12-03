# -*- coding: utf-8 -*-
from app.orderManager import *
from app.stlsManager import *
from typing import Union
import time
import json
import shutil
import os
timestr = time.strftime("%Y%m%d-%H%M%S")
from fastapi import FastAPI, File, UploadFile,Body

from fastapi.exceptions import HTTPException


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = "uploads"

# Ensure the UPLOAD_DIR exists
os.makedirs(UPLOAD_DIR, exist_ok=True)


app = FastAPI()

orders = []


@app.get("/")
def read_root():
    return {"Hello":"Fast"}

@app.post("/multiple_inputs")
async def create_item(
    param1: int = Body(...),
    param2: str = Body(...),
    param3: float = Body(...),
):
    return {"param1": param1, "param2": param2, "param3": param3}

@app.post("/checkout/newOrder")
def new_order(street: int = Body(...),
    town: str = Body(...),
    postal: int = Body(...),
    modelName: str = Body(...),userName: str = Body(...),):

    neworder = Order(Address(street,town,postal),modelName,userName)
    orders.append(neworder)
    return {"Hello":str(orders[-1])}

@app.get("/checkout/allorders")
def read_root():
    return {str(orders)}

@app.get("/checkout/orders/{orderID}")
def read_root(orderID:int):
    return {str(orders[orderID])}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return Upload_File(file)

@app.get("/calcfileCost/{filename}")
async def calcfileCost(filename: str):
    return Calc_Cost(filename)
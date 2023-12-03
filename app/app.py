# -*- coding: utf-8 -*-
from app.orderManager import *
from app.stlsManager import *
from typing import Union
import time
import json
import shutil
import os

timestr = time.strftime("%Y%m%d-%H%M%S")
from fastapi import FastAPI, File, UploadFile, Body, HTTPException

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = "uploads"

# Ensure the UPLOAD_DIR exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

orders = []


@app.get("/")
def read_root():
    return {"Hello": "Fast"}


@app.post("/checkout/newOrder")
def new_order(
    street: int = Body(...),
    town: str = Body(...),
    postal: int = Body(...),
    modelName: str = Body(...),
    userName: str = Body(...),
):
    try:
        neworder = Order(Address(street, town, postal), modelName, userName)
        orders.append(neworder)
        return {"Hello": str(orders[-1])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/checkout/allorders")
def read_all_orders():
    return {"orders": [str(order) for order in orders]}


@app.get("/checkout/orders/{orderID}")
def read_order(orderID: int):
    try:
        return {"order": str(orders[orderID])}
    except IndexError:
        raise HTTPException(status_code=404, detail="Order not found")


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        return Upload_File(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/calcfileCost/{filename}")
async def calcfileCost(filename: str):
    try:
        return Calc_Cost(filename)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")

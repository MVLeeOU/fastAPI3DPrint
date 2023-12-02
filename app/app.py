# -*- coding: utf-8 -*-
from app.orderManager import Order
from typing import Union
import time
import json
import os
timestr = time.strftime("%Y%m%d-%H%M%S")
from fastapi import FastAPI,UploadFile
from fastapi.exceptions import HTTPException


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = FastAPI()

orders = []


@app.get("/")
def read_root():
    return {"Hello":"Fast"}

@app.post("/checkout/newOrder")
def new_order():
    neworder = Order("1726 spring creek dr, rochesthills, mi","catmodel","andersen")
    orders.append(neworder)
    return {"Hello":str(orders[-1])}

@app.get("/checkout/orders")
def read_root():
    return {str(orders)}

    
@app.post("/upload")
def upload(file: UploadFile):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}
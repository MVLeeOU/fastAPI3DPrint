from fastapi import FastAPI,UploadFile,File
from fastapi.exceptions import HTTPException
import os
import shutil

UPLOAD_DIR = "uploads"

def CalculateCost(stlsFileName):
    return 1

def Upload_File(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"filename": file.filename}

def Calc_Cost(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    returnvalue = os.stat(file_path).st_size
    return {"filename": filename, "content": returnvalue}


def FindStlFilePath(filename):
    return filename

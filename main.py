from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
import numpy as np
import shutil
import aiofiles

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Tmp(BaseModel):
    x: int


app = FastAPI()


@app.get("/")
async def main():
    return FileResponse(r"misdo.jpg")



@app.post("/uploadfile/")
async def cache_favicon(file: UploadFile = File(...)):
    img = await file.read()
   
    async with aiofiles.open("{}.jpg".format(file.filename) , "wb") as f:
        await f.write(img)
    return file.filename
# @app.post("/uploadfile/")
# async def create_upload_file(image: UploadFile = File(...)):
#     with open("destination.jpg", "wb") as buffer:
#          shutil.copyfileobj(image.file, buffer)
#     return image.filename




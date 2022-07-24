from typing import Optional

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return FileResponse('index.html')

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

class Model(BaseModel):
    name : str 
    phone : int

@app.post("/send")
def send_info(data: Model):
    print(data)
    return '전송완료'
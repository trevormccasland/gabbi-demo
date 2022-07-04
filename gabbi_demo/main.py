import json
import os
import sys
from typing import List
import uuid

from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(middleware=[
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
])


class RequestItem(BaseModel):
    name: str


class Item(RequestItem):
    id: uuid.UUID


items: List[Item] = []


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: RequestItem):
    if any(item.name == i.name for i in items):
        raise HTTPException(status_code=409, detail=f'Item already exists with name {item.name}.')

    new_item = Item(
        id=uuid.uuid4(),
        name=item.name
    )
    items.append(new_item)
    return new_item


@app.get("/items", response_model=Item)
def get_item(item_id: uuid.UUID):
    for i in range(len(items)):
        if item_id == items[i].id:
            return items[i]
    else:
        raise HTTPException(status_code=404, detail='Item does not exist')


@app.get("/list_items", response_model=List[Item])
def get_items():
    return items

@app.delete("/items", status_code=204)
def delete_item(item_id: uuid.UUID):
    for i in range(len(items)):
        if items[i].id == item_id:
            del items[i]
            break
    return Response(status_code=204)

@app.get("/dogs")
def get_dogs():
    f = open(os.path.join(os.path.dirname(__file__), "dogs.json"), "r")
    data = json.loads(f.read())
    f.close()
    return data


def main():
    uvicorn.run("gabbi_demo.main:app", host="0.0.0.0", port=3500, reload=True, log_level="info")


if __name__ == "__main__":
    sys.exit(main())

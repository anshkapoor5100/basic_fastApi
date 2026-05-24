from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema import Order
from service import update_order,get_order_fromId,fetch_order,remove_order
from typing import Dict
app = FastAPI()


@app.get('/')
def test():
    return {"data":"test_path"}

@app.post('/orders',response_model=Dict)
def add_order(order:Order):
    update_order(order)
    return JSONResponse(status_code=200, content=order.model_dump())

@app.get('/orders/{order_id}',response_model=Dict)
def get_order(order_id:str):
    order = get_order_fromId(order_id)
    return order 

@app.get('/orders')
def get_all_orders():
    return fetch_order()

@app.delete('/orders/{order_id}')
def delete_order(order_id:str):
    return remove_order(order_id)
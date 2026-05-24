from schema import Order
from fastapi import HTTPException,status
import json
from json import JSONDecodeError
from typing import List, Dict

def fetch_order()->List[Dict]:
    try:
        with open('db.json', 'r') as file:
            orders_list = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        orders_list = []
    return orders_list

def save_order(order_list:List[Dict]):
    with open('db.json', 'w') as file:
        json.dump(order_list, file, indent=4)

def update_order(order:Order):
    orders_list = fetch_order()
    orders_list.append(order.model_dump())
    save_order(orders_list)

def get_order_fromId(order_id:str)->Dict:
    orders_list = fetch_order()
    for i in orders_list:
        if i.get("order_id")==order_id:
            return i
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Order with ID '{order_id}' not found"
    )
    
def remove_order(order_id:str):
    orders_list = fetch_order()
    order = get_order_fromId(order_id)
    orders_list.remove(order)
    save_order(orders_list)
    return order
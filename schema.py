from pydantic import BaseModel, Field, field_validator,computed_field
from typing import Annotated, List
class OrderItem(BaseModel):
    item_name:str
    price:Annotated[float,Field(gt=0)]
    quantity:Annotated[int,Field(ge=1)]
    
class Order(BaseModel):
    order_id:str
    has_one_membership:bool
    items:List[OrderItem]
    
    @field_validator("items",mode="after")
    @classmethod
    def validate(cls, value:List[OrderItem]):
        if(len(value)>=1):
            return value
        raise ValueError("must order atleast 1 item")
    
    @computed_field
    @property
    def total_bill(self)->float:
        amount:float = 0.0
        for i in self.items:
            amount += i.price*i.quantity
        if(self.has_one_membership):
            amount*=0.85
        return amount
    
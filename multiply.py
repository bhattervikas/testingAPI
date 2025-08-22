from fastapi import FastAPI
from pydantic import BaseModel

class multiplymodel(BaseModel):
    a:int
    b:int

def multiply (a:int,b:int):
    return a*b

@app.post("/multiply")
def subtract_numbers (model: multiplymodel):
    return multiply(model.a,model.b)
print (multiply(7,4))
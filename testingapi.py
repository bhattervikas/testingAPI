
from fastapi import FastAPI
from pydantic import BaseModel
app =FastAPI()

user_db = {

    1:{"name":"Vikas","age":36},
    2:{"name":"Mona","age":35},
    3:{"name":"Reyansh","age":2},
    4:{"name":"XYx","age":13}
}

class User(BaseModel):
    name:str
    age:int

@app.put("/userUpdate/v1/{user_id}")
def user_update(user_id:int,user:User):

    if user_id in user_db:
       user_db[user_id] =user.dict()
       print(user_db)
       return {"message":"User updated successfully","user":user_db[user_id]}
    else:
        return {"message":"user not found"}
@app.delete("/user_delete/{user_id}")    
def delete_user(user_id :int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return {"Message" : "user deleted successfully"}
    else:
        return {"message" :"user not found"}

    
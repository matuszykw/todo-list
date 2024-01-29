from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None
    is_done: bool
    
class  TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id:int
    
    class Config:
        orm_mode = True
        

class UserBase(BaseModel):
    email: str
    username: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    tasks: list[Task] = []
    
    class Config:
        orm_mode = True
    
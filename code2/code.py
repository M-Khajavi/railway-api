from fastapi import FastAPI
from pydantic import BaseModel


myApp=FastAPI()

@myApp.get("/gettest")
def get_command():
  return("you must POST name and age")

class myArgs(BaseModel):
  name:str
  age:int

@myApp.post("/posttest")
def post_command(args:myArgs):
  return(f"Client name is {args.name} and age is {args.age}")

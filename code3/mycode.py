from fastapi import FastAPI
from pydantic import BaseModel
from functools import reduce
from operator import mul,add

myApp=FastAPI()

@myApp.get("/getTest")
def testGet():
  return("Get tested")

class myArg(BaseModel):
  name:str
  age:int

@myApp.post("/postTest")
def testPost(args:myArg):
  return(
      {
      "nam": args.name,
      "ag": args.age
      }
  )

@myApp.post("/postTst2")
def testPost2(nums: list[int]):
  return(reduce(add,nums))

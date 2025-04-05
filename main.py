from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistics import cities, distance_from_cities, print_cities, travel_time

app = FastAPI()

class City_Item(BaseModel):
    name: str
    
@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Logistics"}

@app.get("/cities")
async def get_cities():
    """Get all cities"""
    return cities

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
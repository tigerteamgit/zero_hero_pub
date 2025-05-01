from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from mylib.logistics import (
    cities_list,
    # distance_between_two_points,
    # get_coordinates,
    # travel_time
)
from mylib.wikibot import (
    get_wiki_summary,
    search_wiki_pages,
    scrape,
    get_wiki_keywords,
)


app = FastAPI()


class City_Item(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home Page with GET HTTP Method"""

    return {"message": "Hello Logistics"}


@app.get("/cities")
async def cities():
    """List cities with GET HTTP Method

    Returns back hte list of cities that are available
    """

    return {"cities": cities_list()}

@app.post("/cities")
async def cities_post(city: City_Item):
    """List cities with POST HTTP Method

    Returns back hte list of cities that are available
    """

    return {"cities": cities_list(city.name)}

@app.post("/wikibot")
async def wikibot(name: str, length: int = 1):
    """Get the summary of a wikipedia page"""

    return {"summary": scrape(name, length)}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")

from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import time
app = FastAPI()

class HotelValues(BaseModel):
    hotel_name: int
    location: str
    star_rating: int
    available_room_count: int

@app.get("/hotel")
def get_hotel(hotel_id:int) -> object:
    hotel_id = hotel_id%5

    hotel_names = ["Hotel A", "Hotel B", "Hotel C", "Hotel D", "Hotel E"]
    locations = ["Location A", "Location B", "Location C", "Location D", "Location E"]
    star_ratings = [1, 2, 3, 4, 5]
    available_room_counts = [10, 20, 30, 40, 50]

    time.sleep(1)

    return {
        "hotel_name": hotel_names[hotel_id],
        "location": locations[hotel_id],
        "star_rating": star_ratings[hotel_id],
        "available_room_count": available_room_counts[hotel_id]
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
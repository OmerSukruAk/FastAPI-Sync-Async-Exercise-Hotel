import aiohttp
import time
import asyncio

start = time.time()

async def get_hotel_info(id:int):
    baseurl = f"http://127.0.0.1:8000/hotel?hotel_id={id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(baseurl) as response:
            print(await response.json())

async def main():
    tasks = []
    for idx in range (7):
        tasks.append(asyncio.create_task(get_hotel_info(idx)))
    await asyncio.gather(*tasks)

asyncio.run(main())    
end = time.time() 

print (f"{end-start} seconds")



"""
OUTPUT:
{'hotel_name': 'Hotel A', 'location': 'Location A', 'star_rating': 1, 'available_room_count': 10}
{'hotel_name': 'Hotel C', 'location': 'Location C', 'star_rating': 3, 'available_room_count': 30}
{'hotel_name': 'Hotel B', 'location': 'Location B', 'star_rating': 2, 'available_room_count': 20}
{'hotel_name': 'Hotel D', 'location': 'Location D', 'star_rating': 4, 'available_room_count': 40}
{'hotel_name': 'Hotel E', 'location': 'Location E', 'star_rating': 5, 'available_room_count': 50}
{'hotel_name': 'Hotel A', 'location': 'Location A', 'star_rating': 1, 'available_room_count': 10}
{'hotel_name': 'Hotel B', 'location': 'Location B', 'star_rating': 2, 'available_room_count': 20}
1.019341230392456 seconds
"""
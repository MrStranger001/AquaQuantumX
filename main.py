# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend is running 🚀"}

# @app.get("/api/quantum-otp")
# def get_otp():
#     return {"otp": "123456"}  # placeholder for now
# from fastapi import FastAPI, Query
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic

# app = FastAPI()

# from fastapi.middleware.cors import CORSMiddleware

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],   # allow all domains
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend is running 🚀"}

# @app.get("/api/quantum-otp")
# def get_otp():
#     return {"otp": "123456"}  # placeholder for now

# # --- Nearest Depot API ---
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Vijayawada Harbour": (16.5062, 80.6480),
#     "Tamil Nadu Harbour": (13.0827, 80.2707)  # Chennai approx
# }

# geolocator = Nominatim(user_agent="seafood_app")

# @app.get("/api/nearest-depot")
# def nearest_depot(address: str = Query(..., description="Enter delivery address")):
#     location = geolocator.geocode(address)
#     if not location:
#         return {"error": "Address not found"}
    
#     user_coords = (location.latitude, location.longitude)
    
#     nearest = None
#     min_distance = float("inf")
    
#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot
    
#     return {
#         "user_address": address,
#         "nearest_depot": nearest,
#         "distance_km": round(min_distance, 2)
#     }
# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic

# app = FastAPI()

# # Enable CORS for frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Dictionary of 213 harbours and depots with their coordinates
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Vijayawada Harbour": (16.5062, 80.6480),
#     "Tamil Nadu Harbour": (13.0827, 80.2707),
#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }

# geolocator = Nominatim(user_agent="seafood_app")

# @app.get("/api/nearest-depot")
# def nearest_depot(address: str = Query(..., description="Enter delivery address")):
#     location = geolocator.geocode(address)
#     if not location:
#         return {"error": "Address not found"}

#     user_coords = (location.latitude, location.longitude)
#     nearest = None
#     min_distance = float("inf")

#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot

#     return {
#         "user_address": address,
#         "nearest_depot": nearest,
#         "distance_km": round(min_distance, 2),
#         "user_lat": location.latitude,
#         "user_lng": location.longitude,
#         "depot_lat": depots[nearest][0],
#         "depot_lng": depots[nearest][1]
#     }
# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic

# app = FastAPI()

# # Allow frontend to call backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Unique depots (expand to 213 later)
# depots = {
#         "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

    
# }

# geolocator = Nominatim(user_agent="seafood_app")

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend is running 🚀"}

# @app.get("/api/quantum-route-multiple")
# def quantum_route(address: str = Query(..., description="Enter delivery address")):
#     location = geolocator.geocode(address)
#     if not location:
#         return {"error": "Address not found"}

#     user_coords = (location.latitude, location.longitude)
#     nearest = None
#     min_distance = float("inf")

#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot

#     return {
#         "user_lat": location.latitude,
#         "user_lng": location.longitude,
#         "depot_lat": depots[nearest][0],
#         "depot_lng": depots[nearest][1],
#         "route_order": [nearest, address],
#         "distance_km": round(min_distance, 2)
#     }
# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic

# app = FastAPI()

# # Allow frontend to call backend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Example depots (expand to 213)
# depots = {

#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }
    

# geolocator = Nominatim(user_agent="seafood_app")

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend running 🚀"}

# @app.get("/api/quantum-route-multiple")
# def quantum_route_multiple(addresses: str = Query(..., description="Comma-separated addresses")):
#     user_addresses = [addr.strip() for addr in addresses.split(",")]
#     results = []

#     for address in user_addresses:
#         location = geolocator.geocode(address)
#         if not location:
#             results.append({"address": address, "error": "Address not found"})
#             continue

#         user_coords = (location.latitude, location.longitude)
#         nearest = None
#         min_distance = float("inf")
#         for depot, coords in depots.items():
#             distance = geodesic(user_coords, coords).km
#             if distance < min_distance:
#                 min_distance = distance
#                 nearest = depot

#         results.append({
#             "address": address,
#             "nearest_depot": nearest,
#             "distance_km": round(min_distance, 2),
#             "user_lat": location.latitude,
#             "user_lng": location.longitude,
#             "depot_lat": depots[nearest][0],
#             "depot_lng": depots[nearest][1]
#         })

#     return {"results": results}









# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import random
# import string
# import uuid

# # Initialize FastAPI app
# app = FastAPI()

# # Enable CORS for frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Comprehensive list of 213 major and minor Indian harbors and depots with their coordinates
# # This list has been expanded to a representative 213 locations.
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }

# # Geocoder instance
# geolocator = Nominatim(user_agent="seafood_app")

# # User database (in-memory for this example)
# users_db = {}

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend running 🚀"}

# @app.post("/api/register")
# def register_user(user_data: dict):
#     """
#     Simulates user registration and generates a unique user ID.
#     """
#     user_id = str(uuid.uuid4())
#     users_db[user_id] = user_data
#     return {"status": "success", "user_id": user_id}

# @app.get("/api/quantum-route-multiple")
# def quantum_route_multiple(addresses: str = Query(..., description="Comma-separated addresses")):
#     """
#     Finds the nearest depot to an address using geodesic distance.
#     """
#     user_addresses = [addr.strip() for addr in addresses.split(",")]
#     results = []

#     for address in user_addresses:
#         location = geolocator.geocode(address)
#         if not location:
#             results.append({"address": address, "error": "Address not found"})
#             continue

#         user_coords = (location.latitude, location.longitude)
#         nearest_depot = None
#         min_distance = float("inf")
#         for depot, coords in depots.items():
#             distance = geodesic(user_coords, coords).km
#             if distance < min_distance:
#                 min_distance = distance
#                 nearest_depot = depot

#         results.append({
#             "address": address,
#             "nearest_depot": nearest_depot,
#             "distance_km": round(min_distance, 2),
#             "user_lat": location.latitude,
#             "user_lng": location.longitude,
#             "depot_lat": depots[nearest_depot][0],
#             "depot_lng": depots[nearest_depot][1]
#         })

#     return {"results": results}

# @app.get("/api/generate-otp")
# def generate_otp(user_id: str):
#     """
#     Generates a 6-digit OTP for the user.
#     """
#     if user_id not in users_db:
#         return {"error": "User not found."}
    
#     otp = ''.join(random.choices(string.digits, k=6))
#     return {"status": "success", "otp": otp}










# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import random
# import string
# import uuid

# # Initialize FastAPI app
# app = FastAPI()

# # Enable CORS for frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Comprehensive list of 213 major and minor Indian harbors and depots with their coordinates
# # This list has been expanded to a representative 213 locations.
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }

# # Geocoder instance
# geolocator = Nominatim(user_agent="seafood_app")

# # User database (in-memory for this example)
# users_db = {}

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend running 🚀"}

# @app.post("/api/register")
# def register_user(user_data: dict):
#     """
#     Simulates user registration and generates a unique user ID.
#     """
#     user_id = str(uuid.uuid4())
#     users_db[user_id] = user_data
#     return {"status": "success", "user_id": user_id}

# @app.get("/api/top-10-depots")
# def get_top_10_depots(address: str = Query(..., description="Single delivery address")):
#     """
#     Finds the top 10 nearest depots for a given address.
#     """
#     location = geolocator.geocode(address)
#     if not location:
#         return {"error": "Address not found"}

#     user_coords = (location.latitude, location.longitude)
#     distances = []

#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         distances.append({
#             "depot_name": depot,
#             "distance_km": round(distance, 2),
#             "depot_lat": coords[0],
#             "depot_lng": coords[1]
#         })
    
#     # Sort by distance and return the top 10
#     distances.sort(key=lambda x: x['distance_km'])
    
#     return {
#         "user_lat": location.latitude,
#         "user_lng": location.longitude,
#         "top_10_depots": distances[:10]
#     }

# @app.get("/api/generate-otp")
# def generate_otp(user_id: str):
#     """
#     Generates a 6-digit OTP for the user.
#     """
#     if user_id not in users_db:
#         return {"error": "User not found."}
    
#     otp = ''.join(random.choices(string.digits, k=6))
#     return {"status": "success", "otp": otp}






# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import random
# import math
# import string
# import uuid

# # Initialize FastAPI app
# app = FastAPI()

# # Enable CORS for frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Comprehensive list of 213 major and minor Indian harbors and depots with their coordinates
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }

# # Geocoder instance
# geolocator = Nominatim(user_agent="seafood_app")

# # User database (in-memory for this example)
# users_db = {}

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend running 🚀"}

# @app.post("/api/register")
# def register_user(user_data: dict):
#     """
#     Simulates user registration and generates a unique user ID.
#     """
#     user_id = str(uuid.uuid4())
#     users_db[user_id] = user_data
#     return {"status": "success", "user_id": user_id}

# @app.get("/api/grover-find-depot")
# def grover_find_depot(address: str = Query(..., description="Single delivery address")):
#     """
#     Simulates Grover's algorithm to find the nearest depot.
#     """
#     location = geolocator.geocode(address)
#     if not location:
#         return {"error": "Address not found"}
    
#     user_coords = (location.latitude, location.longitude)
    
#     # Simulating Grover's algorithm by calculating the distance for all,
#     # but claiming a "quantum speedup" with fewer iterations.
#     num_depots = len(depots)
#     iterations = int(math.sqrt(num_depots))
    
#     nearest = None
#     min_distance = float("inf")
    
#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot
            
#     return {
#         "nearest_depot": nearest,
#         "iterations": iterations,
#         "user_lat": location.latitude,
#         "user_lng": location.longitude
#     }


# @app.get("/api/qaoa-optimize-route")
# def qaoa_optimize_route(depot_name: str, user_lat: float, user_lng: float):
#     """
#     Simulates QAOA to find the optimal path.
#     """
#     depot_coords = depots.get(depot_name)
#     if not depot_coords:
#         return {"error": "Depot not found."}

#     user_coords = (user_lat, user_lng)

#     # For a simple path (depot -> user), the optimal path is the direct route.
#     # We simulate QAOA's optimization process by just returning this path.
#     # In a more complex scenario, this would be a complex calculation.
    
#     # Path is the direct route
#     path = [depot_name, "User Address"]

#     return {
#         "start_location": depot_name,
#         "end_location": "User Address",
#         "depot_lat": depot_coords[0],
#         "depot_lng": depot_coords[1],
#         "user_lat": user_lat,
#         "user_lng": user_lng,
#         "path": path,
#     }

# @app.get("/api/generate-otp")
# def generate_otp(user_id: str):
#     """
#     Generates a 6-digit OTP for the user.
#     """
#     if user_id not in users_db:
#         return {"error": "User not found."}
    
#     otp = ''.join(random.choices(string.digits, k=6))
#     return {"status": "success", "otp": otp}




# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import random
# import string
# import uuid

# # Initialize FastAPI app
# app = FastAPI()

# # Enable CORS for frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Comprehensive list of 213 major and minor Indian harbors and depots with their coordinates
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }

# # Geocoder instance
# geolocator = Nominatim(user_agent="seafood_app")

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend running 🚀"}

# @app.get("/api/quantum-route-multiple")
# def quantum_route_multiple(addresses: str = Query(..., description="Comma-separated addresses")):
#     user_addresses = [addr.strip() for addr in addresses.split(",")]
#     results = []

#     for address in user_addresses:
#         location = geolocator.geocode(address)
#         if not location:
#             results.append({"address": address, "error": "Address not found"})
#             continue

#         user_coords = (location.latitude, location.longitude)
#         nearest = None
#         min_distance = float("inf")
#         for depot, coords in depots.items():
#             distance = geodesic(user_coords, coords).km
#             if distance < min_distance:
#                 min_distance = distance
#                 nearest = depot

#         results.append({
#             "address": address,
#             "nearest_depot": nearest,
#             "distance_km": round(min_distance, 2),
#             "user_lat": location.latitude,
#             "user_lng": location.longitude,
#             "depot_lat": depots[nearest][0],
#             "depot_lng": depots[nearest][1]
#         })

#     return {"results": results}




# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import random
# import math
# import string
# import uuid

# # Initialize FastAPI app
# app = FastAPI()

# # Enable CORS for frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Comprehensive list of 213 major and minor Indian harbors and depots with their coordinates
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }

# # Geocoder instance
# geolocator = Nominatim(user_agent="seafood_app")

# # User database (in-memory for this example)
# users_db = {}

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend running 🚀"}

# @app.get("/api/grover-find-depot")
# def grover_find_depot(address: str = Query(..., description="Single delivery address")):
#     """
#     Simulates Grover's algorithm to find the nearest depot.
#     """
#     location = geolocator.geocode(address)
#     if not location:
#         return {"error": "Address not found"}
    
#     user_coords = (location.latitude, location.longitude)
    
#     num_depots = len(depots)
#     iterations = int(math.sqrt(num_depots))
    
#     nearest = None
#     min_distance = float("inf")
    
#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot
            
#     return {
#         "nearest_depot": nearest,
#         "iterations": iterations,
#         "user_lat": location.latitude,
#         "user_lng": location.longitude,
#         "depot_lat": depots[nearest][0],
#         "depot_lng": depots[nearest][1]
#     }


# @app.get("/api/qaoa-optimize-route")
# def qaoa_optimize_route(addresses: str = Query(..., description="Comma-separated addresses")):
#     """
#     Simulates QAOA to find the optimal path for multiple addresses.
#     Returns the nearest depot to the first address and all user coordinates.
#     """
#     user_addresses = [addr.strip() for addr in addresses.split(",")]
    
#     first_address = user_addresses[0]
#     location = geolocator.geocode(first_address)
#     if not location:
#         return {"error": "First address not found"}

#     user_coords = (location.latitude, location.longitude)
#     nearest = None
#     min_distance = float("inf")
#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot
    
#     # Simulate QAOA by providing the list of waypoints to the frontend
#     # In a real quantum app, QAOA would be used to find the optimal order of addresses.
#     all_locations = []
#     for addr in user_addresses:
#         loc = geolocator.geocode(addr)
#         if loc:
#             all_locations.append({"address": addr, "lat": loc.latitude, "lng": loc.longitude})
            
#     return {
#         "nearest_depot": nearest,
#         "depot_lat": depots[nearest][0],
#         "depot_lng": depots[nearest][1],
#         "user_locations": all_locations
#     }

# @app.get("/api/generate-otp")
# def generate_otp(user_id: str):
#     """
#     Generates a 6-digit OTP for the user.
#     """
#     if user_id not in users_db:
#         return {"error": "User not found."}
    
#     otp = ''.join(random.choices(string.digits, k=6))
#     return {"status": "success", "otp": otp}







# from fastapi import FastAPI, Query
# from fastapi.middleware.cors import CORSMiddleware
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
# import random
# import math
# import string
# import uuid

# # Initialize FastAPI app
# app = FastAPI()

# # Enable CORS for frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Comprehensive list of 213 major and minor Indian harbors and depots with their coordinates
# depots = {
#     "Goa Harbour": (15.2993, 74.1240),
#     "Mumbai Harbour": (18.9398, 72.8355),
#     "Chennai Harbour": (13.0827, 80.2785),
#     "Kochi Harbour": (9.9312, 76.2673),
#     "Visakhapatnam Harbour": (17.6868, 83.2185),
#     "Kandla Harbour": (23.0336, 70.2120),
#     "Mormugao Harbour": (15.4400, 73.7869),
#     "New Mangalore Harbour": (12.9150, 74.8550),
#     "Paradip Harbour": (20.2600, 86.6020),
#     "Tuticorin Harbour": (8.7680, 78.1320),
#     "Jawaharlal Nehru Port": (18.9400, 72.8500),
#     "Kamarajar Port": (13.1480, 80.2830),
#     "Ennore Port": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Dabhol Harbour": (17.5000, 73.2000),
#     "Gangavaram Harbour": (17.7000, 83.2000),
#     "Hazira Harbour": (21.1000, 72.6000),
#     "Alang Harbour": (21.3000, 71.9000),
#     "Beypore Harbour": (11.1000, 75.9000),
#     "Cuddalore Harbour": (11.7500, 79.7500),
#     "Car Nicobar Harbour": (9.1667, 92.8333),
#     "Diamond Harbour": (22.3000, 88.2000),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Kochi Port": (9.9300, 76.2700),
#     "Mangalore Port": (12.8700, 74.8500),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Nhava Sheva Port": (18.9400, 72.8500),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
#     "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),
#     "Cochin Port Trust": (9.9312, 76.2673),
#     "Visakhapatnam Port Trust": (17.6868, 83.2185),
#     "Kochi Port Trust": (9.9312, 76.2673),
#     "Mumbai Port Trust": (18.9400, 72.8500),
#     "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
#     "Kandla Port Trust": (23.0336, 70.2120),
#     "Mormugao Port Trust": (15.4400, 73.7869),
#     "New Mangalore Port Trust": (12.9150, 74.8550),
#     "Paradip Port Trust": (20.2600, 86.6020),
#     "Tuticorin Port Trust": (8.7680, 78.1320),
#     "Chennai Port Trust": (13.0827, 80.2785),

# }

# # Geocoder instance
# geolocator = Nominatim(user_agent="seafood_app")

# # User database (in-memory for this example)
# users_db = {}

# @app.get("/")
# def read_root():
#     return {"message": "Seafood Delivery Backend running 🚀"}

# @app.post("/api/register")
# def register_user(user_data: dict):
#     """
#     Simulates user registration and generates a unique user ID.
#     """
#     user_id = str(uuid.uuid4())
#     users_db[user_id] = user_data
#     return {"status": "success", "user_id": user_id}

# @app.get("/api/find-nearest-depot")
# def find_nearest_depot(address: str = Query(..., description="Single delivery address")):
#     """
#     Simulates Grover's algorithm to find the nearest depot for a single address.
#     """
#     location = geolocator.geocode(address)
#     if not location:
#         return {"error": "Address not found"}
    
#     user_coords = (location.latitude, location.longitude)
    
#     num_depots = len(depots)
#     iterations = int(math.sqrt(num_depots))
    
#     nearest = None
#     min_distance = float("inf")
    
#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot
            
#     return {
#         "nearest_depot": nearest,
#         "iterations": iterations,
#         "user_lat": location.latitude,
#         "user_lng": location.longitude,
#         "depot_lat": depots[nearest][0],
#         "depot_lng": depots[nearest][1]
#     }


# @app.get("/api/qaoa-optimize-route")
# def qaoa_optimize_route(addresses: str = Query(..., description="Comma-separated addresses")):
#     """
#     Simulates QAOA to find the optimal path for multiple addresses.
#     Returns the nearest depot to the first address and all user coordinates.
#     """
#     user_addresses = [addr.strip() for addr in addresses.split(",")]
    
#     first_address = user_addresses[0]
#     location = geolocator.geocode(first_address)
#     if not location:
#         return {"error": "First address not found"}

#     user_coords = (location.latitude, location.longitude)
#     nearest = None
#     min_distance = float("inf")
#     for depot, coords in depots.items():
#         distance = geodesic(user_coords, coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest = depot
    
#     all_locations = []
#     for addr in user_addresses:
#         loc = geolocator.geocode(addr)
#         if loc:
#             all_locations.append({"address": addr, "lat": loc.latitude, "lng": loc.longitude})
            
#     return {
#         "nearest_depot": nearest,
#         "depot_lat": depots[nearest][0],
#         "depot_lng": depots[nearest][1],
#         "user_locations": all_locations
#     }

# @app.get("/api/generate-otp")
# def generate_otp(user_id: str):
#     """
#     Generates a 6-digit OTP for the user.
#     """
#     if user_id not in users_db:
#         return {"error": "User not found."}
    
#     otp = ''.join(random.choices(string.digits, k=6))
#     return {"status": "success", "otp": otp}











from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import random
import math
import string
import uuid

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Comprehensive list of 213 major and minor Indian harbors and depots with their coordinates
depots = {
    "Goa Harbour": (15.2993, 74.1240),
    "Mumbai Harbour": (18.9398, 72.8355),
    "Chennai Harbour": (13.0827, 80.2785),
    "Kochi Harbour": (9.9312, 76.2673),
    "Visakhapatnam Harbour": (17.6868, 83.2185),
    "Kandla Harbour": (23.0336, 70.2120),
    "Mormugao Harbour": (15.4400, 73.7869),
    "New Mangalore Harbour": (12.9150, 74.8550),
    "Paradip Harbour": (20.2600, 86.6020),
    "Tuticorin Harbour": (8.7680, 78.1320),
    "Jawaharlal Nehru Port": (18.9400, 72.8500),
    "Kamarajar Port": (13.1480, 80.2830),
    "Ennore Port": (13.2000, 80.3000),
    "Port Blair Harbour": (11.6667, 92.7500),
    "Dabhol Harbour": (17.5000, 73.2000),
    "Gangavaram Harbour": (17.7000, 83.2000),
    "Hazira Harbour": (21.1000, 72.6000),
    "Alang Harbour": (21.3000, 71.9000),
    "Beypore Harbour": (11.1000, 75.9000),
    "Cuddalore Harbour": (11.7500, 79.7500),
    "Car Nicobar Harbour": (9.1667, 92.8333),
    "Diamond Harbour": (22.3000, 88.2000),
    "Haldia Harbour": (22.0700, 88.0800),
    "Kochi Port": (9.9300, 76.2700),
    "Mangalore Port": (12.8700, 74.8500),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Nhava Sheva Port": (18.9400, 72.8500),
    "Port of Kolkata": (22.5726, 88.3639),
    "Syama Prasad Mookerjee Port": (22.5726, 88.3639),
    "Shyama Prasad Mukherjee Port": (22.5726, 88.3639),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),
    "Cochin Port Trust": (9.9312, 76.2673),
    "Visakhapatnam Port Trust": (17.6868, 83.2185),
    "Kochi Port Trust": (9.9312, 76.2673),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),
    "Cochin Port Trust": (9.9312, 76.2673),
    "Visakhapatnam Port Trust": (17.6868, 83.2185),
    "Kochi Port Trust": (9.9312, 76.2673),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Kakinada Harbour": (16.9891, 82.2475),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),
    "Cochin Port Trust": (9.9312, 76.2673),
    "Visakhapatnam Port Trust": (17.6868, 83.2185),
    "Kochi Port Trust": (9.9312, 76.2673),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),
    "Cochin Port Trust": (9.9312, 76.2673),
    "Visakhapatnam Port Trust": (17.6868, 83.2185),
    "Kochi Port Trust": (9.9312, 76.2673),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),
    "Cochin Port Trust": (9.9312, 76.2673),
    "Visakhapatnam Port Trust": (17.6868, 83.2185),
    "Kochi Port Trust": (9.9312, 76.2673),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),
    "Cochin Port Trust": (9.9312, 76.2673),
    "Visakhapatnam Port Trust": (17.6868, 83.2185),
    "Kochi Port Trust": (9.9312, 76.2673),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),
    "Cochin Port Trust": (9.9312, 76.2673),
    "Visakhapatnam Port Trust": (17.6868, 83.2185),
    "Kochi Port Trust": (9.9312, 76.2673),
    "Mumbai Port Trust": (18.9400, 72.8500),
    "Jawaharlal Nehru Port Trust": (18.9400, 72.8500),
    "Kandla Port Trust": (23.0336, 70.2120),
    "Mormugao Port Trust": (15.4400, 73.7869),
    "New Mangalore Port Trust": (12.9150, 74.8550),
    "Paradip Port Trust": (20.2600, 86.6020),
    "Tuticorin Port Trust": (8.7680, 78.1320),
    "Chennai Port Trust": (13.0827, 80.2785),

}

# Geocoder instance
geolocator = Nominatim(user_agent="seafood_app")

# User database (in-memory for this example)
users_db = {}

@app.get("/")
def read_root():
    return {"message": "Seafood Delivery Backend running 🚀"}

@app.post("/api/register")
def register_user(user_data: dict):
    """
    Simulates user registration and generates a unique user ID.
    """
    user_id = str(uuid.uuid4())
    users_db[user_id] = user_data
    return {"status": "success", "user_id": user_id}

@app.get("/api/find-nearest-depot")
def find_nearest_depot(address: str = Query(..., description="Single delivery address")):
    """
    Simulates Grover's algorithm to find the nearest depot for a single address.
    """
    location = geolocator.geocode(address)
    if not location:
        return {"error": "Address not found"}
    
    user_coords = (location.latitude, location.longitude)
    
    num_depots = len(depots)
    iterations = int(math.sqrt(num_depots))
    
    nearest = None
    min_distance = float("inf")
    
    for depot, coords in depots.items():
        distance = geodesic(user_coords, coords).km
        if distance < min_distance:
            min_distance = distance
            nearest = depot
            
    return {
        "nearest_depot": nearest,
        "iterations": iterations,
        "user_lat": location.latitude,
        "user_lng": location.longitude,
        "depot_lat": depots[nearest][0],
        "depot_lng": depots[nearest][1]
    }


@app.get("/api/qaoa-optimize-route")
def qaoa_optimize_route(addresses: str = Query(..., description="Comma-separated addresses")):
    """
    Simulates QAOA to find the optimal path for multiple addresses.
    Returns the nearest depot to the first address and all user coordinates.
    """
    user_addresses = [addr.strip() for addr in addresses.split(",")]
    
    first_address = user_addresses[0]
    location = geolocator.geocode(first_address)
    if not location:
        return {"error": "First address not found"}

    user_coords = (location.latitude, location.longitude)
    nearest = None
    min_distance = float("inf")
    for depot, coords in depots.items():
        distance = geodesic(user_coords, coords).km
        if distance < min_distance:
            min_distance = distance
            nearest = depot
    
    all_locations = []
    for addr in user_addresses:
        loc = geolocator.geocode(addr)
        if loc:
            all_locations.append({"address": addr, "lat": loc.latitude, "lng": loc.longitude})
            
    return {
        "nearest_depot": nearest,
        "depot_lat": depots[nearest][0],
        "depot_lng": depots[nearest][1],
        "user_locations": all_locations
    }

@app.get("/api/generate-otp")
def generate_otp(user_id: str):
    """
    Generates a 6-digit OTP for the user.
    """
    if user_id not in users_db:
        return {"error": "User not found."}
    
    otp = ''.join(random.choices(string.digits, k=6))
    return {"status": "success", "otp": otp}





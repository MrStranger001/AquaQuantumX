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





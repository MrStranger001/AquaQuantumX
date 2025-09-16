<<<<<<< HEAD

# import math
# import random
# import uuid
# from typing import Dict, List

# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic

# # --- CORRECTED Qiskit Imports ---
# # Aer is now in its own package: qiskit-aer
# from qiskit import QuantumCircuit, execute
# from qiskit_aer import AerSimulator # <-- Use AerSimulator

# # --- 1. FastAPI App Initialization ---
# app = FastAPI(
#     title="Quantum Logistics API",
#     description="API for finding nearest depots and generating quantum-inspired security codes.",
# )

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # --- 2. Services and Data ---
# geolocator = Nominatim(user_agent="quantum_logistics_app_v2", timeout=10)

# # Cleaned and verified list of depots
# DEPOTS = {
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
#     "Kamarajar Port (Ennore)": (13.2000, 80.3000),
#     "Port Blair Harbour": (11.6667, 92.7500),
#     "Kakinada Harbour": (16.9891, 82.2475),
#     "Haldia Harbour": (22.0700, 88.0800),
#     "Port of Kolkata": (22.5726, 88.3639),
#     "Avanti Feeds Ltd., Kovvur": (17.0118, 81.7271),
#     "Coastal Corporation Ltd., Vizag": (17.7277, 83.3039),
#     "Apex Frozen Foods Ltd., Kakinada": (16.9664, 82.2427),
#     "Gadre Marine Export, Ratnagiri": (16.9912, 73.3120),
# }

# # --- 3. Quantum-Inspired Random Number Generator (Corrected) ---
# def get_quantum_random_bits(num_bits):
#     """Generates true random bits using a quantum simulator."""
#     # Use the correct modern simulator
#     simulator = AerSimulator()
#     # Create a quantum circuit with one qubit and one classical bit per requested bit
#     circuit = QuantumCircuit(num_bits, num_bits)
#     # Apply Hadamard gate to create superposition
#     circuit.h(range(num_bits))
#     # Measure the qubits
#     circuit.measure(range(num_bits), range(num_bits))
#     # Execute the circuit
#     job = execute(circuit, simulator, shots=1)
#     result = job.result()
#     counts = result.get_counts(circuit)
#     # The result is a bitstring, e.g., '10110'
#     return list(counts.keys())[0]

# # --- 4. Pydantic Models for API Data Structure ---
# class Location(BaseModel):
#     address: str
#     lat: float
#     lng: float

# class NearestDepotResponse(BaseModel):
#     nearest_depot_name: str
#     depot_location: Location
#     user_location: Location
#     distance_km: float

# class QuantumOTPResponse(BaseModel):
#     otp: str

# class QuantumPasswordResponse(BaseModel):
#     password: str

# # --- 5. API Endpoints ---
# @app.get("/")
# def read_root():
#     return {"message": "Quantum Logistics API is running"}

# @app.get("/api/find-nearest-depot", response_model=NearestDepotResponse)
# def find_nearest_depot_endpoint(address: str):
#     """
#     Finds the nearest depot to a single address or coordinate pair.
#     This is the core endpoint for the route planner.
#     """
#     try:
#         location = geolocator.geocode(address)
#         if not location:
#             raise HTTPException(status_code=404, detail=f"Address not found: {address}")
#     except Exception:
#         raise HTTPException(status_code=500, detail="Geocoding service failed. Please try again later.")
        
#     user_coords = (location.latitude, location.longitude)
    
#     nearest_depot_name = None
#     min_distance = float('inf')
    
#     for depot_name, depot_coords in DEPOTS.items():
#         distance = geodesic(user_coords, depot_coords).km
#         if distance < min_distance:
#             min_distance = distance
#             nearest_depot_name = depot_name
            
#     depot_location = DEPOTS[nearest_depot_name]
    
#     return {
#         "nearest_depot_name": nearest_depot_name,
#         "depot_location": {"address": nearest_depot_name, "lat": depot_location[0], "lng": depot_location[1]},
#         "user_location": {"address": address, "lat": user_coords[0], "lng": user_coords[1]},
#         "distance_km": round(min_distance, 2)
#     }

# @app.get("/api/generate-quantum-otp", response_model=QuantumOTPResponse)
# def generate_otp():
#     """Generates a 6-digit OTP using quantum random bits."""
#     # We need enough bits to generate numbers up to 999999
#     num_bits = 20 # 2^20 is > 1,000,000, which is sufficient
#     random_bit_string = get_quantum_random_bits(num_bits)
#     random_int = int(random_bit_string, 2)
#     otp = str(random_int % 1000000).zfill(6) # Ensure it's 6 digits
#     return {"otp": otp}

# @app.get("/api/generate-quantum-password", response_model=QuantumPasswordResponse)
# def generate_password(length: int = 12):
#     """Generates a secure password using quantum random bits."""
#     if not 8 <= length <= 64:
#         raise HTTPException(status_code=400, detail="Password length must be between 8 and 64 characters.")
    
#     chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
#     password = ""
#     for _ in range(length):
#         # Generate enough bits to select an index from the character list
#         num_bits = math.ceil(math.log2(len(chars)))
#         while True:
#             random_bit_string = get_quantum_random_bits(num_bits)
#             random_int = int(random_bit_string, 2)
#             if random_int < len(chars):
#                 password += chars[random_int]
#                 break
#     return {"password": password}





import math
import random
import uuid
from typing import Dict, List

from fastapi import FastAPI, HTTPException
=======
from fastapi import FastAPI, Query
>>>>>>> 080975ecf100cab5785aecd48c65970d26126103
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# --- FINAL CORRECTED Qiskit Imports ---
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# --- 1. FastAPI App Initialization ---
app = FastAPI(
    title="Quantum Logistics API",
    description="API for finding nearest depots and generating quantum-inspired security codes.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 2. Services and Data ---
geolocator = Nominatim(user_agent="quantum_logistics_app_v2", timeout=10)

# Cleaned and verified list of depots
DEPOTS = {
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
    "Kamarajar Port (Ennore)": (13.2000, 80.3000),
    "Port Blair Harbour": (11.6667, 92.7500),
    "Kakinada Harbour": (16.9891, 82.2475),
    "Haldia Harbour": (22.0700, 88.0800),
    "Port of Kolkata": (22.5726, 88.3639),
    "Avanti Feeds Ltd., Kovvur": (17.0118, 81.7271),
    "Coastal Corporation Ltd., Vizag": (17.7277, 83.3039),
    "Apex Frozen Foods Ltd., Kakinada": (16.9664, 82.2427),
    "Gadre Marine Export, Ratnagiri": (16.9912, 73.3120),
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
     "Port of Shanghai": (31.2304, 121.4737),        # World's busiest container port.
    "Port of Ningbo-Zhoushan": (29.8683, 121.5439),  # World's busiest port by cargo tonnage.
    "Port of Shenzhen": (22.5431, 114.0579),        # Comprises multiple ports like Yantian and Shekou.
    "Port of Guangzhou": (23.1291, 113.2644),       # Major hub in the Pearl River Delta.
    "Port of Qingdao": (36.0671, 120.3826),         # Key port in the north, major seafood hub.
    "Port of Tianjin": (39.0842, 117.2008),         # Primary maritime gateway to Beijing.
    "Port of Hong Kong": (22.3193, 114.1694),       # A major international transshipment hub.
    "Port of Xiamen": (24.4798, 118.0894),          # Important deepwater port opposite Taiwan.
    
    # --- Other Major Ports & Fishing Hubs ---
    "Port of Dalian": (38.9140, 121.6147),          # Northern China's largest multi-purpose port.
    "Port of Yingkou": (40.6692, 122.2336),         # Important port in Liaoning province.
    "Shidao Fishing Port, Shandong": (36.8881, 122.4419), # One of China's largest fishing harbors.
    "Shenjiamen Fishing Port, Zhoushan": (29.9573, 122.3004), # Famous, very large fishing port.
    "Fuzhou Port": (26.0745, 119.2965),             # Key port in Fujian province.
    "Zhanjiang Port": (21.2707, 110.3983),          # Major port in Guangdong, southern coast.
     # --- Major Publicly Traded Companies ---
    "Zhangzidao Group Co., Ltd.": (39.0081, 122.6953),  # Dalian-based, major producer of scallops & sea cucumbers.
    "Zoneco Group (formerly Dalian獐子岛)": (38.9140, 121.6147), # Another major Dalian-based aquaculture giant.
    "Guolian Aquatic Products": (21.2707, 110.3983),   # Zhanjiang-based, one of China's largest shrimp exporters.
    "Homey Aquatic Development": (29.9573, 122.3004),   # Zhoushan-based, large integrated seafood company.
    "Baiyang Investment Group": (22.8159, 108.3422),   # Nanning-based, focus on tilapia and aquaculture feed.
    "Shantou Yuexing Aquatic Co.": (23.3687, 116.7148),# Shantou-based processor and exporter.

    # --- Other Significant Players ---
    "Qingdao Meichu Foodstuff": (36.0671, 120.3826),     # Processor of various seafood in Qingdao.
    "Rongcheng Taixiang Food": (37.1642, 122.4144),      # Based in Rongcheng, a major fishing city.
    "Leizhou Hengrun Aquatic": (20.9100, 109.7800),     # Leizhou-based, shrimp farming and processing.
    "Fujian Anjoy Foods": (24.4798, 118.0894),          # Xiamen-based, known for frozen food products including seafood.
    "Dalian Ridu Food Co.": (38.9140, 121.6147),       # Dalian-based processor.

       # --- Bohai Sea / Northern Ports ---
    "Port of Qinhuangdao": (39.9321, 119.5931), # Major port for coal, but also handles general cargo.
    "Weihai Port": (37.5143, 122.1135),         # Important commercial and fishing port in Shandong.
    "Yantai Port": (37.5540, 121.4011),         # Major fishing base and ferry hub in Shandong.
    "Rizhao Port": (35.4194, 119.5311),         # Growing port for bulk cargo and containers.
    "Panjin Port": (40.9234, 121.9423),         # Located in the Liaohe River Delta.

    # --- Yellow Sea / Eastern Ports ---
    "Lianyungang Port": (34.7578, 119.4539),    # Key port at the start of the New Eurasian Land Bridge.
    "Nantong Port": (32.0292, 120.8872),       # An important river and sea port on the Yangtze.
    "Wenzhou Port": (28.0193, 120.6970),        # Major port in Zhejiang province.
    "Taizhou Port, Zhejiang": (28.6761, 121.4246), # Not to be confused with Taizhou in Jiangsu.

    # --- South China Sea / Southern Ports ---
    "Beihai Port": (21.4800, 109.1200),         # Key port in the Guangxi region.
    "Haikou Port": (20.0471, 110.3150),         # Main port for Hainan island province.
    "Shantou Port": (23.3687, 116.7148),       # A key port in eastern Guangdong.
    "Quanzhou Port": (24.9139, 118.5858),       # Historically significant port in Fujian.
    "Fangcheng Port": (21.6167, 108.3500),      # Major hub in the Beibu Gulf.
    "Yangjiang Port": (21.8587, 111.9818),      # Significant fishing port in Guangdong.
    # --- Processors and Exporters ---
    "Fujian Haohui Aquatic Development": (26.0745, 119.2965), # Fuzhou-based, processing & trading.
    "Beihai Qunlin Industrial": (21.4800, 109.1200),         # Frozen shrimp and tilapia processor in Beihai.
    "Dalian Fugu Seafood": (38.9140, 121.6147),             # Specializes in canned seafood and processing.
    "Qingdao Yuanyin Food Co.": (36.0671, 120.3826),         # Focus on frozen fish fillets and squid.
    "Yantai Longwin Foods": (37.5540, 121.4011),            # Processor of squid, pollock, and other fish.
    "Hainan Xiangtai Fishery": (18.2523, 109.5118),         # Sanya-based, covers fishing and processing.
    "Shandong Oriental Ocean Sci-Tech": (37.5540, 121.4011), # Yantai-based, aquaculture and processing.
    "Zhejiang Ocean Family Co.": (29.8683, 121.5439),        # Ningbo-based, focuses on tuna processing.
    # --- Aquaculture and Feed Specialists ---
    "Tongwei Group": (30.6586, 104.0649),                   # Chengdu-based giant in aquaculture feed.
    "Haida Group": (23.1291, 113.2644),                     # Guangzhou-based, major aquatic feed and farming.
    "Evergreen Conglomerate (Haida)": (21.2707, 110.3983),  # Zhanjiang-based large aquaculture enterprise.
    "Fuhuang Aquatic Products": (21.2707, 110.3983),        # Another major player in Zhanjiang's shrimp industry.
    "Rongcheng Lida Aquatic Food": (37.1642, 122.4144),     # Squid and fish processor in Rongcheng.
    "Ningbo Tech-Bank Co.": (29.8683, 121.5439),  
      # --- West Coast ---
    "Port of Los Angeles, California": (33.7292, -118.2620),
    "Port of Long Beach, California": (33.7542, -118.2165),
    "Port of Oakland, California": (37.7957, -122.2886),
    "Port of Seattle-Tacoma, Washington": (47.5874, -122.3445), # Northwest Seaport Alliance

    # --- East Coast ---
    "Port of New York and New Jersey": (40.6835, -74.0435),
    "Port of Savannah, Georgia": (32.1229, -81.1685),
    "Port of Virginia (Norfolk)": (36.9315, -76.3025),
    "Port of Charleston, South Carolina": (32.7831, -79.9311),

    # --- Gulf Coast ---
    "Port of Houston, Texas": (29.7183, -95.2935),
    "Port of South Louisiana, Louisiana": (29.9511, -90.0715),
    "Port of Corpus Christi, Texas": (27.8131, -97.3964),
      # --- Alaska (Leads the nation in volume) ---
    "Dutch Harbor, Alaska": (53.8861, -166.5425),     # Consistently the #1 fishing port by volume in the USA.
    "Naknek, Alaska (Bristol Bay)": (58.7297, -157.0114), # Heart of the world's largest sockeye salmon fishery.
    "Kodiak, Alaska": (57.7900, -152.4072),             # Major hub for salmon, halibut, and cod.

    # --- New England (Leads the nation in value) ---
    "New Bedford, Massachusetts": (41.6362, -70.9342), # Consistently the #1 fishing port by value (scallops).
    "Gloucester, Massachusetts": (42.6148, -70.6620),  # America's oldest seaport.
    "Portland, Maine": (43.6615, -70.2553),            # Major lobster and groundfish port.

    # --- Pacific Northwest ---
    "Astoria, Oregon": (46.1879, -123.8313),           # Major hub at the mouth of the Columbia River for Dungeness crab.
    "Westport, Washington": (46.8851, -124.1096),      # Key port for crab, shrimp, and salmon.

    # --- Gulf Coast ---
    "Empire-Venice, Louisiana": (29.2319, -89.3528),   # Important hub for shrimp and oysters.
    "Brownsville-Port Isabel, Texas": (26.0426, -97.2025), # Major shrimp fleet harbor.
     # --- Major Processors & Brands ---
    "Trident Seafoods Corporation HQ": (47.6163, -122.3361), # Seattle, WA - Largest seafood company in the US.
    "Bumble Bee Foods HQ": (32.7157, -117.1611),             # San Diego, CA (Canned tuna and seafood).
    "Starkist Co. (Dongwon) US HQ": (40.4406, -79.9959),       # Pittsburgh, PA (Major tuna brand).
    "Sysco Corporation HQ": (29.7604, -95.3698),               # Houston, TX - A massive food distributor, including seafood.
    "Pacific Seafood Group HQ": (45.4246, -122.7431),         # Clackamas, OR - Vertically integrated processor.
    
    # --- Regional & Specialized Leaders ---
    "Red Lobster HQ": (28.5383, -81.3792),                    # Orlando, FL (Largest seafood restaurant chain).
    "Gorton's of Gloucester": (42.6148, -70.6620),             # Gloucester, MA (Famous for frozen fish products).
    "Silver Bay Seafoods": (57.0450, -135.3300),              # Sitka, AK - A major salmon processor.
    "Icicle Seafoods (Cooke Inc.)": (47.6062, -122.3321),     # Seattle, WA - Major Alaska salmon and pollock processor.
    "Taylor Shellfish Farms": (48.4552, -122.7538),           # Shelton, WA - Largest shellfish farmer in the US.
    "The Lobster Place (distributor)": (40.7421, -74.0048),  
     # --- Major Container & Cargo Hubs ---
    "Port of Tokyo": (35.6330, 139.7923),        # Japan's capital port, a massive hub for container traffic.
    "Port of Yokohama": (35.4552, 139.6380),     # Major deepwater port, part of the Greater Tokyo Area.
    "Port of Nagoya": (35.0842, 136.8815),       # Japan's largest and busiest port by cargo tonnage.
    "Port of Osaka": (34.6533, 135.4332),        # A key port for the Kansai region.
    "Port of Kobe": (34.6800, 135.1950),         # One of Japan's most important historic and modern ports.
    "Port of Hakata (Fukuoka)": (33.6065, 130.4183), # Main port for the island of Kyushu.
    "Port of Tomakomai, Hokkaido": (42.6370, 141.6042), # Largest port on the northern island of Hokkaido.
    "Port of Chiba": (35.5804, 140.1119), 
      # --- World-Famous & High-Volume Ports ---
    "Yaizu Fishing Port, Shizuoka": (34.8625, 138.3275),  # Famous for its massive bonito (katsuo) and tuna landings.
    "Choshi Fishing Port, Chiba": (35.7336, 140.8524),  # One of the highest-volume fishing ports in Japan.
    "Kushiro Port, Hokkaido": (42.9748, 144.3814),    # A major base for Japan's northern pacific fishing fleet.
    "Sakaiminato, Tottori": (35.5492, 133.2306),       # Known for crab and a wide variety of seafood.
    "Hachinohe Port, Aomori": (40.5284, 141.5204),     # Japan's leading port for squid landings.
    "Misaki Port, Kanagawa": (35.1394, 139.6163),      # A historic and famous port specializing in high-quality tuna.
    "Shimonoseki, Yamaguchi": (33.9567, 130.9412),    # Famed as the "Pufferfish Capital" of Japan.
    "Kesen-numa, Miyagi": (38.9064, 141.5714),       # Important deep-sea fishing port, known for sharks and swordfish.
     # --- Global Seafood Giants ---
    "Maruha Nichiro Corporation HQ": (35.6762, 139.7671), # Tokyo - The world's largest seafood company by revenue.
    "Nippon Suisan Kaisha (Nissui) HQ": (35.6895, 139.7650), # Tokyo - Another global giant in fishing and food processing.
    "Kyokuyo Co., Ltd. HQ": (35.6812, 139.7661),        # Tokyo - Major player in fishing, processing, and logistics.
    
    # --- Major Processors & Brands ---
    "Toyo Suisan Kaisha, Ltd. HQ": (35.6895, 139.7671),  # Tokyo - Owns the "Maruchan" brand, major in instant noodles & seafood.
    "Nichirei Corporation HQ": (35.6734, 139.7626),        # Tokyo - Leader in frozen foods, including seafood.
    "Hagoromo Foods Corporation": (34.9756, 138.3846),   # Shizuoka - Famous for its canned tuna ("Sea Chicken").
    
    # --- Aquaculture & Specialized Companies ---
    "Kindai University Aquaculture": (34.1610, 135.2440), # Wakayama - Famed for pioneering fully farm-raised bluefin tuna.
    "Japan NUS Co., Ltd. (Aquaculture)": (32.7833, 130.2667), # Kumamoto - Focus on aquaculture technology and farming.
    "Hayashikane Sangyo Co. Ltd.": (33.9567, 130.9412),  # Shimonoseki - Processor of fish sausages and other products.
    "Tassal Group (owned by Cooke Inc.)": (43.0642, 141.3469),
    # --- Pacific Far East (Most important for fishing) ---
    "Port of Vladivostok": (43.1156, 131.8855),  # Russia's largest port on the Pacific, primary hub for seafood.
    "Port of Nakhodka": (42.8167, 132.8667),    # Major commercial port near Vladivostok.
    "Port of Vostochny": (42.7550, 133.0460),   # One of Russia's largest deep-water ports.
    "Port of Petropavlovsk-Kamchatsky": (53.0167, 158.6500), # Critical for the Kamchatka crab and salmon fisheries.

    # --- Baltic Sea ---
    "Port of Saint Petersburg": (59.9343, 30.3351), # Russia's primary historical gateway to Europe.
    "Port of Primorsk": (60.3667, 28.7167),       # A major port for oil, but also handles other cargo.
    "Port of Ust-Luga": (59.6644, 28.3242),       # One of Russia's newest and most modern ports on the Baltic.

    # --- Arctic Ocean ---
    "Port of Murmansk": (68.9667, 33.0833),       # World's largest city north of the Arctic Circle, key for cod fishing.
    "Port of Arkhangelsk": (64.5333, 40.5167),    # Historic port on the White Sea.

    # --- Black Sea ---
    "Port of Novorossiysk": (44.7167, 37.7667), # Russia's busiest port by cargo turnover, on the Black Sea.
    "Port of Sevastopol": (44.6167, 33.5254), 
    # --- World's Largest Pollock & Cod Producers ---
    "Russian Fishery Company (RFC)": (43.1156, 131.8855),  # Vladivostok - One of the world's largest producers of pollock.
    "Norebo Holding": (68.9667, 33.0833),                  # Murmansk - Russia's largest fish harvesting quota holder (cod, pollock).
    "Gidrostroy": (46.9631, 142.7297),                     # Yuzhno-Sakhalinsk - A major salmon and pollock company.

    # --- King Crab & Other Major Players ---
    "Russian Crab Group (Русский Краб)": (43.1156, 131.8855), # Vladivostok - Russia's largest crab harvesting company.
    "Okeanrybflot": (53.0167, 158.6500),                   # Petropavlovsk-Kamchatsky - One of the largest fishing companies in the Far East.
    "Antey": (43.1156, 131.8855),                          # Vladivostok - Another major player in the King Crab fishery.
    "Vostok-1 Fishing Collective": (43.1156, 131.8855),     # Vladivostok - A large, historic fishing enterprise.
    "NBAMR (Nakhodka Active Marine Fishery Base)": (42.8167, 132.8667), # Nakhodka - Large fleet operator.
    "Sakhalin Island": (46.9631, 142.7297),                # Yuzhno-Sakhalinsk - A major processor of salmon roe (ikura).
    
    # --- European Russia ---
    "Arkhangelsk Trawl Fleet": (64.5333, 40.5167),         # Arkhangelsk - Major player in the Northern (Arctic) basin.
    "Murmansk Trawl Fleet": (68.9667, 33.0833),   












}


# --- 3. Quantum-Inspired Random Number Generator (Corrected) ---
def get_quantum_random_bits(num_bits):
    """Generates true random bits using a quantum simulator."""
    simulator = AerSimulator()
    circuit = QuantumCircuit(num_bits, num_bits)
    circuit.h(range(num_bits))
    circuit.measure(range(num_bits), range(num_bits))
    
    # --- THIS IS THE CORRECTED LINE ---
    # The new method is to call .run() directly on the simulator
    job = simulator.run(circuit, shots=1)
    
    result = job.result()
    counts = result.get_counts(circuit)
    return list(counts.keys())[0]

# --- 4. Pydantic Models for API Data Structure ---
class Location(BaseModel):
    address: str
    lat: float
    lng: float

class NearestDepotResponse(BaseModel):
    nearest_depot_name: str
    depot_location: Location
    user_location: Location
    distance_km: float

class QuantumOTPResponse(BaseModel):
    otp: str

class QuantumPasswordResponse(BaseModel):
    password: str

# --- 5. API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Quantum Logistics API is running"}

@app.get("/api/find-nearest-depot", response_model=NearestDepotResponse)
def find_nearest_depot_endpoint(address: str):
    """
    Finds the nearest depot to a single address or coordinate pair.
    This is the core endpoint for the route planner.
    """
    try:
        location = geolocator.geocode(address)
        if not location:
            raise HTTPException(status_code=404, detail=f"Address not found: {address}")
    except Exception:
        raise HTTPException(status_code=500, detail="Geocoding service failed. Please try again later.")
        
    user_coords = (location.latitude, location.longitude)
    
    nearest_depot_name = None
    min_distance = float('inf')
    
    for depot_name, depot_coords in DEPOTS.items():
        distance = geodesic(user_coords, depot_coords).km
        if distance < min_distance:
            min_distance = distance
            nearest_depot_name = depot_name
            
    depot_location = DEPOTS[nearest_depot_name]
    
    return {
        "nearest_depot_name": nearest_depot_name,
        "depot_location": {"address": nearest_depot_name, "lat": depot_location[0], "lng": depot_location[1]},
        "user_location": {"address": address, "lat": user_coords[0], "lng": user_coords[1]},
        "distance_km": round(min_distance, 2)
    }

@app.get("/api/generate-quantum-otp", response_model=QuantumOTPResponse)
def generate_otp():
    """Generates a 6-digit OTP using quantum random bits."""
    num_bits = 20
    random_bit_string = get_quantum_random_bits(num_bits)
    random_int = int(random_bit_string, 2)
    otp = str(random_int % 1000000).zfill(6)
    return {"otp": otp}

@app.get("/api/generate-quantum-password", response_model=QuantumPasswordResponse)
def generate_password(length: int = 12):
    """Generates a secure password using quantum random bits."""
    if not 8 <= length <= 64:
        raise HTTPException(status_code=400, detail="Password length must be between 8 and 64 characters.")
    
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for _ in range(length):
        num_bits = math.ceil(math.log2(len(chars)))
        while True:
            random_bit_string = get_quantum_random_bits(num_bits)
            random_int = int(random_bit_string, 2)
            if random_int < len(chars):
                password += chars[random_int]
                break
    return {"password": password}

# --- 6. Main execution block (for direct script running) ---
if __name__ == "__main__":
    import uvicorn
    # Note: Use "main:app" to specify the file and the app object
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


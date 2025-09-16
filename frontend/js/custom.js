

// API URL for your Python backend
const API_URL = "https://aqua-quantum-backend.onrender.com";

// --- Map Initialization ---
const map = L.map('map').setView([20.5937, 78.9629], 5);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

let markers = [];
let routeLines = [];

// --- Custom Icons (Updated) ---
// Using a person for the user and a truck for the depot
const userIcon = L.divIcon({ html: '<div class="bg-blue-500 text-white w-8 h-8 flex items-center justify-center rounded-full shadow-lg border-2 border-white"><i class="fas fa-user"></i></div>', iconSize: [32, 32] });
const depotIcon = L.divIcon({ html: '<div class="bg-purple-600 text-white w-8 h-8 flex items-center justify-center rounded-full shadow-lg border-2 border-white"><i class="fas fa-truck"></i></div>', iconSize: [32, 32] });

// --- Helper Functions ---
const clearMap = () => {
    markers.forEach(marker => map.removeLayer(marker));
    routeLines.forEach(line => map.removeLayer(line));
    markers = [];
    routeLines = [];
};

// --- Main Function to Find Routes ---
const findRoutes = async () => {
    const locationInput = document.getElementById('locationInput').value.trim();
    const statusMessage = document.getElementById('statusMessage');
    const findBtn = document.getElementById('findRouteBtn');
    const resultsContainer = document.getElementById('resultsContainer');
    const resultList = document.getElementById('resultList');

    if (!locationInput) {
        statusMessage.innerHTML = `<span class="text-yellow-300">Please provide at least one address.</span>`;
        statusMessage.classList.remove('hidden');
        return;
    }
    
    const addresses = locationInput.split(',').map(addr => addr.trim()).filter(addr => addr);

    clearMap();
    statusMessage.innerHTML = `<span class="animate-pulse">Simulating quantum pathways...</span>`;
    statusMessage.classList.remove('hidden');
    findBtn.disabled = true;
    resultsContainer.classList.add('hidden');
    resultList.innerHTML = '';

    const bounds = L.latLngBounds();
    let allRoutesFound = true;

    for (const address of addresses) {
        try {
            // Step 1: Call our backend to find the nearest depot
            const depotResponse = await fetch(`${API_URL}/api/find-nearest-depot?address=${encodeURIComponent(address)}`);
            const depotData = await depotResponse.json();

            if (!depotResponse.ok) {
                throw new Error(depotData.detail || 'Failed to find depot.');
            }

            const userCoords = L.latLng(depotData.user_location.lat, depotData.user_location.lng);
            const depotCoords = L.latLng(depotData.depot_location.lat, depotData.depot_location.lng);

            const userMarker = L.marker(userCoords, { icon: userIcon }).addTo(map).bindPopup(`<b>Your Address:</b><br>${address}`);
            const depotMarker = L.marker(depotCoords, { icon: depotIcon }).addTo(map).bindPopup(`<b>Depot:</b><br>${depotData.nearest_depot_name}`);
            markers.push(userMarker, depotMarker);
            bounds.extend(userCoords);
            bounds.extend(depotCoords);

            // Step 2: Call OSRM API with reversed route (Depot -> User)
            const osrmUrl = `https://router.project-osrm.org/route/v1/driving/${depotCoords.lng},${depotCoords.lat};${userCoords.lng},${userCoords.lat}?overview=full&geometries=geojson`;
            const osrmResponse = await fetch(osrmUrl);
            const osrmData = await osrmResponse.json();
            if (osrmData.code !== 'Ok') {
                throw new Error('Could not calculate a road route.');
            }

            const route = osrmData.routes[0];
            const distanceKm = route.distance / 1000;

            // Calculate travel time for a bike at 40 km/h
            const bikeSpeedKmph = 40;
            const timeHours = distanceKm / bikeSpeedKmph;
            const travelTimeMinutes = Math.round(timeHours * 60);
            
            // Draw the route line on the map
            const routeLine = L.geoJSON(route.geometry, { style: { color: '#8b5cf6', weight: 5, opacity: 0.9 } }).addTo(map);
            routeLines.push(routeLine);
            
            // Display the result in the list
            const resultItem = document.createElement('div');
            resultItem.className = "p-2 bg-white rounded-md shadow-sm";
            resultItem.innerHTML = `
                <div class="text-sm font-semibold text-gray-800">${depotData.nearest_depot_name}</div>
                <div class="text-xs text-gray-600">
                    → To Address: <strong>${address}</strong>
                </div>
                <div class="text-xs text-gray-500 mt-1">
                    <i class="fas fa-road mr-1"></i>${distanceKm.toFixed(2)} km
                    <i class="fas fa-clock mr-1 ml-3"></i>~${travelTimeMinutes} min (Bike)
                </div>
            `;
            resultList.appendChild(resultItem);

        } catch (error) {
            allRoutesFound = false;
            const errorItem = document.createElement('div');
            errorItem.className = "p-2 bg-red-100 text-red-700 rounded-md shadow-sm";
            errorItem.innerHTML = `<p class="text-sm font-semibold">${address}</p><p class="text-xs">${error.message}</p>`;
            resultList.appendChild(errorItem);
        }
    }

    if (allRoutesFound) {
        statusMessage.innerHTML = `<span class="text-green-300">✅ Quantum simulation complete.</span>`;
    } else {
         statusMessage.innerHTML = `<span class="text-yellow-400">⚠️ Some routes could not be calculated.</span>`;
    }
    
    resultsContainer.classList.remove('hidden');
    if (markers.length > 0) {
        map.fitBounds(bounds, { padding: [50, 50] });
    }

    findBtn.disabled = false;
};

// --- Event Listeners ---
document.getElementById('findRouteBtn').addEventListener('click', findRoutes);
document.getElementById('locationInput').addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent form submission
        findRoutes();
    }
});



# generate_telemetry.py

import csv
import random
import os

# Output path
os.makedirs("data", exist_ok=True)
filename = "data/telemetry.csv"

# Simulate 100 telemetry records
rows = []
for t in range(100):
    altitude = t * 10  # each row = 10 meters higher
    temp = 1500 + random.uniform(-50, 150) + (t * 2)  # rising temperature
    o2 = max(21 - t * 0.05 + random.uniform(-0.2, 0.2), 0)  # slowly falling O2
    co2 = 4000 + random.uniform(0, 20) + (t * 3)  # rising CO2
    rad = 300 + random.uniform(0, 50) + (t * 4)  # radiation spikes
    g_force = 1 + random.uniform(0, 0.3) + (t * 0.01)  # gradual g-force rise

    rows.append({
        "time": t,
        "altitude": altitude,
        "TEMP": round(temp, 2),
        "OXY": round(o2, 2),
        "CO2": round(co2, 2),
        "RAD": round(rad, 2),
        "G_FORCE": round(g_force, 2)
    })

# Write to CSV
with open(filename, mode="w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ Telemetry data written to {filename}")

# 🚀 SpaceX Dynamics GUI Simulator

A real-time Python simulation showcasing rocket movement and environmental telemetry monitoring, inspired by the Starship Dynamics team at SpaceX. Built using **PyQt5** and **Matplotlib**, this GUI features live rocket animation, telemetry data generation, and dynamically updating environmental charts.

---

## 🔧 Features

- 🛰️ **Live Rocket Simulation**  
  Realistic rocket ascent visualized in a space-themed environment.

- 📈 **Dynamic Telemetry Charts**  
  Live-updating graphs for:
  - Temperature
  - CO₂ concentration
  - Oxygen levels
  - Radiation exposure

- 🚨 **Error Monitoring**  
  Displays critical events like overheating, low oxygen, and radiation spikes in real-time.

- 🧠 **Auto-Generated Data**  
  Synthetic telemetry values evolve as the rocket moves, simulating real flight data.

---

## 🗂️ Project Structure

```
.
├── assets/
│   └── rocket.png
├── core/
│   └── graph_loader.py
├── data/
│   └── telemetry.csv
├── gui/
│   └── main_window.py
└── README.md
```

---

## ▶️ How to Run

1. **Install dependencies**  
```bash
pip install PyQt5 matplotlib
```

2. **Run the simulator**  
```bash
python gui/main_window.py
```

3. Click **Launch** to start simulation. Watch charts and error log update live!

---

## 🧪 Demo Use Case

This tool simulates the kind of system you'd use to monitor and debug vibration, environmental risk, and structural telemetry aboard Starship — useful for candidates applying to roles like **Software Engineer (Dynamics)** at SpaceX.

---

## 📁 Output

- `data/telemetry.csv` — automatically written to every second.
- Charts update in real time as data changes.

---

## 📌 Notes

- Designed to be self-contained and offline.
- Can be extended with real telemetry ingestion, physics engines, or ML integration.
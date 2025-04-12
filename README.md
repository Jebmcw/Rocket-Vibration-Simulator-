# Rocket-Vibration-Simulator-

# 🚀 Rocket Vibration Simulator

A lightweight Python simulation that models structural vibration in a rocket system and runs rule-based AI to detect mission-critical failures from simulated telemetry (e.g., heat shield overheating, oxygen drop, radiation spikes).

## 💡 Features
- Simulates spring-mass-damper dynamics
- Generates synthetic telemetry data
- Detects mission risks with rule-based alert logic
- Exports charts and alert summaries
- Modular and expandable (ML-ready)

## 📁 Project Structure
- `sim/` - All simulation and alert logic
- `data/` - Sample telemetry for testing
- `output/` - Charts + alert reports
- `main.py` - Runs the full process

## 🚀 How to Run
```bash
pip install -r requirements.txt
python main.py
'''

### 📊 Output Example
## 🛠️ Built With

- Python

- NumPy

- SciPy

- Matplotlib

- ReportLab (optional)

### 📌 Future Additions
- ML-based predictive alert system

- Flask UI for web visualization

- Real sensor data integration

### ✅ Suggested File Goals:
- `dynamics.py`: Solve a second-order ODE (mass-spring-damper) and return displacement data.
- `telemetry_gen.py`: Randomly simulate rocket conditions (temp, O2, CO2, rad).
- `alert_engine.py`: Scan telemetry rows and flag alerts like `🔥 Overheat`, `❗ Oxygen Low`.

---
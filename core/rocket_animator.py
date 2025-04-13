# === core/rocket_animator.py ===
# This module controls the rocket's visual position based on telemetry

from PyQt5.QtCore import QTimer, QPointF  # QTimer for animation, QPointF not used but imported
from PyQt5.QtWidgets import QLabel        # QLabel used to show rocket image
from PyQt5.QtGui import QPixmap           # QPixmap to load and scale the rocket image
import pandas as pd                       # Pandas for reading telemetry CSV
import os                                 # OS to check if telemetry file exists

class RocketAnimator:
    def __init__(self, rocket_label: QLabel, telemetry_path: str):
        # QLabel to hold the rocket image
        self.rocket_label = rocket_label

        # Path to the telemetry data file (CSV)
        self.telemetry_path = telemetry_path

        # Timer to control periodic rocket updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_position)

        # Loaded telemetry data
        self.telemetry_data = []

        # Index of the current telemetry row
        self.index = 0

        # Load and scale the rocket image
        self.rocket_pixmap = QPixmap("assets/rocket.png").scaled(60,60)
        self.rocket_label.setPixmap(self.rocket_pixmap) 
        self.rocket_label.setFixedSize(60,60)

    def load_telemetry(self):
        # If telemetry file doesn't exist, skip loading
        if not os.path.exists(self.telemetry_path):
            return
        try:
            # Load telemetry into a list of dictionaries
            df = pd.read_csv(self.telemetry_path)
            self.telemetry_data = df.to_dict("records")
            self.index = 0
        except Exception as e:
            print(f"[RocketAnimator] Failed to load telemetry: {e}")

    def start(self, interval_ms=100):
        # Load data and start timer to update every 'interval_ms'
        self.load_telemetry()
        self.timer.start(interval_ms)

    def stop(self):
        # Stop the timer when animation ends or stops
        self.timer.stop()

    def update_position(self):
        # If no data or reached end, stop animation
        if not self.telemetry_data or self.index >= len(self.telemetry_data):
            self.stop()
            return
         # Get current telemetry point
        point = self.telemetry_data[self.index]
        x = int(point.get("distance", 0))  # Distance drives horizontal movement
        y = int(point.get("time", 0))      # Time drives vertical alignment

        # Position the rocket using top-left origin
        self.rocket_label.move(x, y)
        self.index += 1  # Move to next telemetry point for next update
import sys
import os
import csv
import random
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFrame, QTextEdit
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap
from core.graph_loader import LiveChart

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🚀 Space Environment Simulator")
        self.setFixedSize(1400, 800)

        self.telemetry_path = "data/telemetry.csv"
        self.time_counter = 0
        self._init_csv()

        # Rocket movement parameters
        self.rocket_x = 50
        self.rocket_y = 640

        # Rocket image
        self.rocket_label = QLabel()
        rocket_img = QPixmap("assets/rocket.png").scaled(100, 100)
        self.rocket_label.setPixmap(rocket_img)
        self.rocket_label.setFixedSize(100, 100)

        # Chart-style frame
        self.space_chart = QFrame()
        self.space_chart.setStyleSheet("background-color: black; border")
        self.space_chart.setFixedSize(600, 700)
        self.space_chart_layout = QVBoxLayout(self.space_chart)
        self.space_chart_layout.setContentsMargins(0, 0, 0, 0)
        self.space_chart_layout.addWidget(self.rocket_label, alignment=Qt.AlignTop | Qt.AlignLeft)

        # Error monitor text box
        self.error_log = QTextEdit()
        self.error_log.setReadOnly(True)
        self.error_log.setFixedSize(200, 200)

        # Live charts
        self.graph1 = LiveChart("Temperature Over Time", "TEMP (K)", ["TEMP"], ["red"])
        self.graph2 = LiveChart("CO₂ Concentration", "ppm", ["CO2"], ["green"])
        self.graph3 = LiveChart("O₂ and Radiation", "Levels", ["OXY", "RAD"], ["blue", "orange"])

        # Buttons
        self.launch_btn = QPushButton("Launch")
        self.stop_btn = QPushButton("Stop")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.launch_btn)
        button_layout.addWidget(self.stop_btn)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.space_chart)
        main_layout.addWidget(self.error_log)  # Add error log between rocket and charts

        center_layout = QVBoxLayout()
        center_layout.addLayout(button_layout)
        center_layout.addStretch()

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.graph1)
        right_layout.addWidget(self.graph2)
        right_layout.addWidget(self.graph3)

        main_layout.addLayout(center_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

        # Timers
        self.move_timer = QTimer()
        self.move_timer.timeout.connect(self.move_rocket)

        self.telemetry_timer = QTimer()
        self.telemetry_timer.timeout.connect(self.append_telemetry_row)

        self.launch_btn.clicked.connect(self.start_simulation)
        self.stop_btn.clicked.connect(self.stop_simulation)

    def _init_csv(self):
        os.makedirs("data", exist_ok=True)
        with open(self.telemetry_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["time", "TEMP", "CO2", "OXY", "RAD"])

    def append_telemetry_row(self):
        print(f"[Telemetry] Writing data point at time {self.time_counter + 1}")
        self.time_counter += 1
        temp = 1500 + random.uniform(-50, 300)
        co2 = 4000 + random.uniform(-50, 700)
        o2 = max(15, 21 - self.time_counter * 0.05 + random.uniform(-0.2, 0.2))
        rad = 300 + random.uniform(-50, 200)

        if temp > 1600:
            self.error_log.append("🔥 Heat shield overheating")
        if o2 < 19:
            self.error_log.append("❗ Oxygen level dangerously low")
        if co2 > 5000:
            self.error_log.append("🛑 CO₂ level too high")
        if rad > 500:
            self.error_log.append("☢️ Radiation critical")

        with open(self.telemetry_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.time_counter, round(temp, 2), round(co2, 2), round(o2, 2), round(rad, 2)])

    def start_simulation(self):
        self.move_timer.start(50)          # Smooth rocket movement
        self.telemetry_timer.start(1000)   # One telemetry row per second

    def stop_simulation(self):
        self.move_timer.stop()
        self.telemetry_timer.stop()

    def move_rocket(self):
        self.rocket_y -= 2
        if self.rocket_y < -100:
            self.rocket_y = 640
        self.rocket_label.move(self.rocket_x, self.rocket_y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
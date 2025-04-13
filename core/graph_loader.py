import pandas as pd
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer

class LiveChart(QWidget):
    def __init__(self, title, y_label, series_labels, colors):
        super().__init__()
        self.figure = Figure(figsize=(5, 2), tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.title = title
        self.y_label = y_label
        self.series_labels = series_labels
        self.colors = colors

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_chart)
        self.timer.start(1000)  # Updates chart every second; make sure telemetry.csv is written to at similar intervals

    def update_chart(self):
        try:
            # To make the chart dynamic, the telemetry.csv file needs to be written to during runtime by the rocket simulation.
            # Consider adding logic to your rocket update loop that appends new telemetry data here.
            df = pd.read_csv("data/telemetry.csv")
            if df.empty or "time" not in df.columns:
                return

            self.ax.clear()
            self.ax.set_title(self.title)
            self.ax.set_xlabel("Time")
            self.ax.set_ylabel(self.y_label)

            for label, color in zip(self.series_labels, self.colors):
                if label in df.columns:
                    self.ax.plot(df["time"], df[label], label=label, color=color)

            self.ax.legend(loc="upper right")
            self.ax.grid(True)
            self.canvas.draw_idle()
        except Exception as e:
            print(f"[LiveChart] Failed to update chart: {e}")

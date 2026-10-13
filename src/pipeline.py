from src.thermal_loader import ThermalLoader
from src.hotspot_detector import HotspotDetector
from src.report import InspectionReport

class ThermalInspectionPipeline:
    def __init__(self):
        self.loader = ThermalLoader()
        self.detector = HotspotDetector()
        self.report = InspectionReport()

    def run(self, thermal_path):
        temp = self.loader.load(thermal_path)
        hotspots = self.detector.detect(temp)
        for h in hotspots:
            sev = "CRITICAL" if h["delta"] > 20 else \
                  "HIGH" if h["delta"] > 15 else "MEDIUM"
            self.report.add(h["bbox"], h["max_temp"], sev)
        return self.report.summary()

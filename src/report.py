import json
import csv
from datetime import datetime

class InspectionReport:
    def __init__(self):
        self.items = []

    def add(self, bbox, temp_max, severity, lat=None, lon=None):
        self.items.append({
            "bbox": bbox, "temp_max": temp_max,
            "severity": severity, "lat": lat, "lon": lon,
            "timestamp": datetime.utcnow().isoformat()
        })

    def to_json(self, path="inspection_report.json"):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.items, f, ensure_ascii=False, indent=2)

    def to_csv(self, path="inspection_report.csv"):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.items[0].keys())
            writer.writeheader()
            writer.writerows(self.items)

    def summary(self):
        n = len(self.items)
        crit = sum(1 for x in self.items if x["severity"] == "CRITICAL")
        return {"total": n, "critical": crit, "ok": n - crit}

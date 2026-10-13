import cv2
import numpy as np

class HotspotDetector:
    def __init__(self, delta_c=10.0, min_area=20):
        self.delta_c = delta_c
        self.min_area = min_area

    def detect(self, temp):
        mean = np.median(temp)
        mask = ((temp - mean) > self.delta_c).astype(np.uint8) * 255
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        hotspots = []
        for c in contours:
            area = cv2.contourArea(c)
            if area < self.min_area:
                continue
            x, y, w, h = cv2.boundingRect(c)
            max_temp = float(temp[y:y+h, x:x+w].max())
            hotspots.append({"bbox": [x, y, w, h], "max_temp": max_temp,
                             "delta": max_temp - mean, "area": area})
        return hotspots

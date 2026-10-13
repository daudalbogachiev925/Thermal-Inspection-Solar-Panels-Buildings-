import cv2
import numpy as np

class PanelSegmenter:
    """Сегментация солнечных панелей по контурам."""
    def segment(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        panels = []
        for c in contours:
            area = cv2.contourArea(c)
            if area < 500:
                continue
            x, y, w, h = cv2.boundingRect(c)
            ar = w / max(h, 1)
            if 0.3 < ar < 3.0:
                panels.append([x, y, w, h])
        return panels

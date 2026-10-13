import numpy as np
from src.hotspot_detector import HotspotDetector

def test_detects_hotspot():
    temp = np.ones((100, 100)) * 25.0
    temp[40:60, 40:60] = 45.0
    spots = HotspotDetector(delta_c=10, min_area=10).detect(temp)
    assert len(spots) >= 1
    assert spots[0]["max_temp"] >= 44

def test_no_hotspot_uniform():
    temp = np.ones((100, 100)) * 25.0
    assert HotspotDetector().detect(temp) == []

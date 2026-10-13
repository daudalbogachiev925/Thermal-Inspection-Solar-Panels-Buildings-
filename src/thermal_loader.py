import cv2
import numpy as np

class ThermalLoader:
    """Загрузка теплового изображения (Radiometric JPEG / PNG)."""
    def load(self, path):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if img is None:
            raise FileNotFoundError(path)
        if img.dtype == np.uint16:
            # радиометрический — перевести в °C (примерный коэффициент)
            return img.astype(np.float32) / 100.0 - 273.15
        return img.astype(np.float32)

    def normalize(self, temp):
        return (temp - temp.min()) / (temp.max() - temp.min() + 1e-6)

import numpy as np
from PIL import Image


# Genera matrice random per "Prima Parte"
def generate_random_matrix(N: int, seed: int = 42) -> np.ndarray:
    np.random.seed(seed)
    return np.random.rand(N, N) * 255  # valori simili a immagini in scala di grigi


#
def load_grayscale_image(path):
    image = Image.open(path).convert("L")  # 'L' = grayscale
    return np.array(image)

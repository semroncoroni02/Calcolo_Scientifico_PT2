import numpy as np
from scipy.fftpack import dct

def dct2_fast(block):
    """
    Applica la DCT2 veloce (type II) a un blocco 2D.
    Usa DCT-II normalizzata ortonormalmente.
    """
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

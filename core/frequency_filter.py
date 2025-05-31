import numpy as np
from scipy.fftpack import dct, idct


def dct2(block):
    """Applica la DCT2 a un blocco 2D."""
    return dct(dct(block.T, norm='ortho').T, norm='ortho')


def idct2(coefficients):
    """Applica la DCT2 inversa a un blocco di coefficienti."""
    return idct(idct(coefficients.T, norm='ortho').T, norm='ortho')


def process_block(block, d):
    """
    Applica DCT2, filtra le frequenze in base a d, esegue la IDCT2 e normalizza i valori.

    Args:
        block (ndarray): Blocco F x F di pixel in scala di grigi.
        d (int): Soglia di taglio delle frequenze (0 <= d <= 2F-2).

    Returns:
        ndarray: Blocco F x F ricostruito dopo il filtraggio.
    """
    F = block.shape[0]
    c = dct2(block)

    # Filtraggio: azzera i coefficienti per cui k + l >= d
    for k in range(F):
        for l in range(F):
            if k + l >= d:
                c[k, l] = 0

    ff = idct2(c)

    # Arrotondamento e normalizzazione dei valori in [0, 255]
    ff = np.round(ff).astype(np.int32)
    ff = np.clip(ff, 0, 255).astype(np.uint8)

    return ff


def process_all_blocks(blocks, d):
    """
    Applica il filtro di frequenza a ogni blocco.

    Parameters:
        blocks (list of np.ndarray): Lista di blocchi F×F.
        d (int): Soglia di taglio per le frequenze.

    Returns:
        list of np.ndarray: Lista di blocchi filtrati.
    """
    filtered_blocks = [process_block(block, d) for block in blocks]
    return filtered_blocks

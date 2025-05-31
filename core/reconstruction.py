import numpy as np


def reconstruct_image_from_blocks(blocks, image_shape, F):
    """
    Ricompone un'immagine a partire dai blocchi filtrati.

    Parameters:
        blocks (list of np.ndarray): Lista di blocchi F×F.
        image_shape (tuple): Altezza e larghezza dell’immagine originale (dopo il ritaglio).
        F (int): Dimensione dei blocchi quadrati.

    Returns:
        np.ndarray: Immagine ricostruita come array 2D.
    """
    h, w = image_shape
    reconstructed = np.zeros((h, w), dtype=np.uint8)

    idx = 0
    for i in range(0, h, F):
        for j in range(0, w, F):
            reconstructed[i:i + F, j:j + F] = blocks[idx]
            idx += 1

    return reconstructed

import numpy as np


def compute_dct_matrix(N: int) -> np.ndarray:
    """
    Calcola la matrice D della DCT2 normalizzata secondo la definizione vista a lezione.
    """
    D = np.zeros((N, N))
    for k in range(N):
        for n in range(N):
            alpha = np.sqrt(1 / N) if k == 0 else np.sqrt(2 / N)
            D[k, n] = alpha * np.cos(np.pi * (2 * n + 1) * k / (2 * N))
    return D


def dct2_custom(f_mat: np.ndarray) -> np.ndarray:
    """
    Implementazione fedele a quella MATLAB per la DCT2 fatta in casa.
    Applica la DCT1 alle colonne, poi alle righe.
    """
    N = f_mat.shape[0]
    assert f_mat.shape[0] == f_mat.shape[1], "La matrice deve essere quadrata"

    D = compute_dct_matrix(N)
    c_mat = np.copy(f_mat)

    # DCT1 per colonne
    for j in range(N):
        c_mat[:, j] = D @ c_mat[:, j]

    # DCT1 per righe
    for i in range(N):
        c_mat[i, :] = (D @ c_mat[i, :].T).T

    return c_mat

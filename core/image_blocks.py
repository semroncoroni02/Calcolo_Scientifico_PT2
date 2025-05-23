import numpy as np


def divide_into_blocks(image_array, F):
    h, w = image_array.shape
    h_trim = h - (h % F)
    w_trim = w - (w % F)
    image_array = image_array[:h_trim, :w_trim]

    blocks = []
    for i in range(0, h_trim, F):
        for j in range(0, w_trim, F):
            block = image_array[i:i + F, j:j + F]
            blocks.append(block)

    return blocks, (h_trim, w_trim)

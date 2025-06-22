from core.dct_custom import dct2_custom
from core.dct_library import dct2_fast
from utils.helpers import generate_random_matrix
from utils.timer import measure_execution_time
from utils.plotter import plot_timings

# SECONDA PARTE
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from interface.gui import get_user_inputs
from core.image_blocks import divide_into_blocks
from core.frequency_filter import process_all_blocks
from core.reconstruction import reconstruct_image_from_blocks


def main_1():
    sizes = [8, 16, 32, 64, 128, 256, 512]
    times_custom = []
    times_fast = []

    risultati = []

    print("- " * 30)
    print("📊 \033[32mCONFRONTO TEMPI DCT2\033[0m 📊 | 🧪 \033[32mTEST SU MATRICI RANDOM\033[0m 🧪")
    print("-" * 60)
    print("N (dim.)    |  🧮 Tempo Custom (s)  |  \033[33m⚡\033[0m Tempo Fast (s)")
    print("-" * 60)

    for N in sizes:
        matrix = generate_random_matrix(N)

        t_custom = measure_execution_time(dct2_custom, matrix)
        t_fast = measure_execution_time(dct2_fast, matrix)

        times_custom.append(t_custom)
        times_fast.append(t_fast)

        risultati.append((N, t_custom, t_fast))

        print(f"{N:<9}   |  {t_custom:17.6f}    |{t_fast:17.6f}")

    print("-" * 60)
    plot_timings(sizes, times_custom, times_fast)


def main_2():
    def load_image_as_gray_array(path):
        img = Image.open(path).convert('L')  # Converti in scala di grigi
        return np.array(img)

    # 1. Ottieni input dalla GUI
    image_path, F, d = get_user_inputs()

    # 2. Carica immagine
    original_array = load_image_as_gray_array(image_path)

    # 3. Suddividi in blocchi F×F
    blocks, image_shape = divide_into_blocks(original_array, F)

    # 4. Applica DCT2, filtra frequenze, IDCT2, normalizza
    processed_blocks = process_all_blocks(blocks, d)

    # 5. Ricostruisci immagine
    compressed_array = reconstruct_image_from_blocks(processed_blocks, image_shape, F)

    # 6. Visualizza originale e compressa
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(original_array, cmap='gray')
    axs[0].set_title('Originale', fontsize=15)
    axs[0].axis('off')

    axs[1].imshow(compressed_array, cmap='gray')
    axs[1].set_title(f'Compressione: F={F}, d={d}', fontsize=15)
    axs[1].axis('off')

    plt.suptitle("RISULTATO COMPRESSIONE\n", fontsize=20, fontweight="bold")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("\033[92mDigitare [1] per PRIMA PARTE\nDigitare [2] per SECONDA PARTE\n↓ ")
    sel = input()

    if sel == '1':
        main_1()
    else:
        main_2()

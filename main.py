from core.dct_custom import dct2_custom
from core.dct_library import dct2_fast
from utils.helpers import generate_random_matrix
from utils.timer import measure_execution_time
from utils.plotter import plot_timings


def benchmark_dct_methods():
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


if __name__ == "__main__":
    benchmark_dct_methods()

import matplotlib.pyplot as plt


def plot_timings(sizes, times_custom, times_fast):
    plt.figure(figsize=(10, 6))
    plt.semilogy(sizes, times_custom, 'o-', label='DCT2 Custom')
    plt.semilogy(sizes, times_fast, 's--', label='DCT2 Fast (Libreria)')

    plt.xlabel("Dimensione N")
    plt.ylabel("Tempo di esecuzione (s) [scala log]")
    plt.title("Confronto tempi [DCT2 Custom] VS [DCT2 Fast]")
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

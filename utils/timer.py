import time


def measure_execution_time(func, *args, **kwargs) -> float:
    """
    Misura il tempo di esecuzione di una funzione in secondi.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start

import time
import random
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Algoritmo de fuerza bruta O(n^2)
# ------------------------------------------------------------
def max_subarray_bruteforce(arr):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

# ------------------------------------------------------------
# Algoritmo divide y vencerás O(n log n)
# ------------------------------------------------------------
def max_crossing_subarray(arr, low, mid, high):
    # Suma máxima hacia la izquierda desde mid
    left_sum = float('-inf')
    total = 0
    for i in range(mid, low - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
    # Suma máxima hacia la derecha desde mid+1
    right_sum = float('-inf')
    total = 0
    for i in range(mid + 1, high + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
    return left_sum + right_sum

def max_subarray_dac(arr, low, high):
    if low == high:  # caso base
        return arr[low]
    mid = (low + high) // 2
    left_max = max_subarray_dac(arr, low, mid)
    right_max = max_subarray_dac(arr, mid + 1, high)
    cross_max = max_crossing_subarray(arr, low, mid, high)
    return max(left_max, right_max, cross_max)

# ------------------------------------------------------------
# Medición de tiempos para diferentes tamaños
# ------------------------------------------------------------
def measure_times():
    sizes = [10, 50, 100, 200, 500, 1000]
    times_bf = []
    times_dac = []

    for n in sizes:
        # Generar arreglo aleatorio con números entre -100 y 100
        arr = [random.randint(-100, 100) for _ in range(n)]

        # Fuerza bruta
        start = time.perf_counter()
        max_subarray_bruteforce(arr)
        end = time.perf_counter()
        times_bf.append(end - start)

        # Divide y vencerás
        start = time.perf_counter()
        max_subarray_dac(arr, 0, n-1)
        end = time.perf_counter()
        times_dac.append(end - start)

        print(f"n={n:4d} | BF: {times_bf[-1]:.6f}s | DAC: {times_dac[-1]:.6f}s")

    return sizes, times_bf, times_dac

# ------------------------------------------------------------
# Graficar
# ------------------------------------------------------------
def plot_results(sizes, times_bf, times_dac):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_bf, 'o-', label='Fuerza Bruta (O(n²))', color='red')
    plt.plot(sizes, times_dac, 's-', label='Divide y Vencerás (O(n log n))', color='blue')
    plt.xlabel('Tamaño del arreglo (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación de algoritmos para el subarreglo máximo')
    plt.legend()
    plt.grid(True)
    plt.savefig('subarreglo_comparacion.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    sizes, times_bf, times_dac = measure_times()
    plot_results(sizes, times_bf, times_dac)
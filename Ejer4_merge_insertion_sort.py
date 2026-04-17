import time
import random
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Insertion Sort O(n^2)
# ------------------------------------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            
            j -= 1
        arr[j + 1] = key
    return arr

# ------------------------------------------------------------
# Merge Sort O(n log n)
# ------------------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ------------------------------------------------------------
# Medición de tiempos
# ------------------------------------------------------------
def measure_times():
    sizes = [10, 50, 100, 500, 1000, 5000]
    times_insertion = []
    times_merge = []

    for n in sizes:
        # Generar arreglo aleatorio (mismo para ambos)
        arr = [random.randint(0, 10000) for _ in range(n)]

        # Insertion Sort (sobre copia)
        arr_copy = arr.copy()
        start = time.perf_counter()
        insertion_sort(arr_copy)
        end = time.perf_counter()
        times_insertion.append(end - start)

        # Merge Sort (sobre copia)
        arr_copy = arr.copy()
        start = time.perf_counter()
        merge_sort(arr_copy)
        end = time.perf_counter()
        times_merge.append(end - start)

        print(f"n={n:5d} | Insertion: {times_insertion[-1]:.6f}s | Merge: {times_merge[-1]:.6f}s")

    return sizes, times_insertion, times_merge

# ------------------------------------------------------------
# Graficar
# ------------------------------------------------------------
def plot_results(sizes, times_insertion, times_merge):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_insertion, 'o-', label='Insertion Sort (O(n²))', color='orange')
    plt.plot(sizes, times_merge, 's-', label='Merge Sort (O(n log n))', color='green')
    plt.xlabel('Tamaño del arreglo (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Comparación: Merge Sort vs Insertion Sort')
    plt.legend()
    plt.grid(True)
    plt.savefig('ordenamiento_comparacion.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    sizes, times_insertion, times_merge = measure_times()
    plot_results(sizes, times_insertion, times_merge)
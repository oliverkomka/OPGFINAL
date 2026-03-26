import random
import time
import sys

sys.setrecursionlimit(50000)

from treesort import tree_sort


def bubble_sort(arr, length):
    comparisons = 0
    assignments = 0
    sorted_until = 0
    while True:
        swaps = 0
        for i in range(length - 1 - sorted_until):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                assignments += 3
                swaps += 1
        if swaps == 0:
            return arr, comparisons, assignments
        sorted_until += 1


def selection_sort(arr, length):
    comparisons = 0
    assignments = 0
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        assignments += 3
    return arr, comparisons, assignments


def insertion_sort(arr, length):
    comparisons = 0
    assignments = 0
    for i in range(1, length):
        key = arr[i]
        assignments += 1
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                assignments += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        assignments += 1
    return arr, comparisons, assignments


def insertion_sort_binary(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    for i in range(1, n):
        key = arr[i]
        assignments += 1
        left, right = 0, i
        while left < right:
            comparisons += 1
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid
        j = i
        while j > left:
            arr[j] = arr[j - 1]
            assignments += 1
            j -= 1
        arr[left] = key
        assignments += 1
    return arr, comparisons, assignments


class QuickSortMetrics:
    def __init__(self):
        self.comparisons = 0
        self.assignments = 0

    def quick_sort(self, arr, low, high):
        if low < high:
            pivot_index = low
            for j in range(low, high):
                self.comparisons += 1
                if arr[j] < arr[high]:
                    arr[j], arr[pivot_index] = arr[pivot_index], arr[j]
                    self.assignments += 3
                    pivot_index += 1
            arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
            self.assignments += 3
            self.quick_sort(arr, low, pivot_index - 1)
            self.quick_sort(arr, pivot_index + 1, high)
        return arr


class MergeSortMetrics:
    def __init__(self):
        self.comparisons = 0
        self.assignments = 0

    def merge_sort(self, lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                self.comparisons += 1
                if left[i] < right[j]:
                    lst[k] = left[i]
                    self.assignments += 1
                    i += 1
                else:
                    lst[k] = right[j]
                    self.assignments += 1
                    j += 1
                k += 1
            while i < len(left):
                lst[k] = left[i]
                self.assignments += 1
                i += 1
                k += 1
            while j < len(right):
                lst[k] = right[j]
                self.assignments += 1
                j += 1
                k += 1


def radix_sort(arr, length):
    comparisons = 0
    assignments = 0
    max_val = max(arr)
    exp = 1
    result = [0] * length
    while exp <= max_val:
        digit_count = [0] * 10
        for num in arr:
            digit_count[num // exp % 10] += 1
        total = 0
        for i in range(10):
            digit_count[i], total = total, total + digit_count[i]
        for num in arr:
            result[digit_count[num // exp % 10]] = num
            assignments += 1
            digit_count[num // exp % 10] += 1
        arr, result = result, arr
        exp *= 10
    return arr, comparisons, assignments


# === HLAVNY PROGRAM ===
n = 20000  # <-- ZMen na 20000 pre druhe meranie

print(f"Vysledky pre N={n} - kolisavo klesajuce data\n")

algorithms = [
    ("Bubble Sort",                    lambda data, size: bubble_sort(data, size)),
    ("Selection Sort",                 lambda data, size: selection_sort(data, size)),
    ("Insertion Sort",                 lambda data, size: insertion_sort(data, size)),
    ("Insertion Sort + Binary Search", lambda data, size: insertion_sort_binary(data)),
    ("Quick Sort",                     None),
    ("Merge Sort",                     None),
    ("Radix Sort",                     lambda data, size: radix_sort(data, size)),
    ("Tree Sort",                      lambda data, size: tree_sort(data, size)),
]

for name, func in algorithms:
    print(name)
    print("Test | Cas(ms) | Porovnania | Priradenia")
    for run in range(1, 6):
        data = []
        current_value = n * 10
        while len(data) < n:
            dec = random.randint(1, 10)
            data.append(current_value - dec)
            current_value = data[-1]
            if len(data) < n:
                inc = random.randint(1, 5)
                data.append(current_value + inc)
                current_value = data[-1]
        data = data[:n]

        start = time.time()
        if name == "Quick Sort":
            counter = QuickSortMetrics()
            counter.quick_sort(data, 0, n - 1)
            comps, assigns = counter.comparisons, counter.assignments
        elif name == "Merge Sort":
            counter = MergeSortMetrics()
            counter.merge_sort(data)
            comps, assigns = counter.comparisons, counter.assignments
        else:
            _, comps, assigns = func(data, n)
        elapsed = (time.time() - start) * 1000
        print(f"{run} | {elapsed:.2f} | {comps} | {assigns}")
    print()

print("POZNAMKA: Data su kolisavo klesajuce.\n")

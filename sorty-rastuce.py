import random
import time
import sys

sys.setrecursionlimit(50000)

from treesort import tree_sort


def bubble_sort(arr, length):
    comparisons = 0
    assignments = 0
    pass_num = 0
    while True:
        swap_count = 0
        for i in range(length - 1 - pass_num):
            comparisons += 1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                assignments += 3
                swap_count += 1
        if swap_count == 0:
            return arr, comparisons, assignments
        pass_num += 1


def selection_sort(arr, length):
    comparisons = 0
    assignments = 0
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            comparisons += 1
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
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


def insertion_sort_with_binary_search(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0
    for i in range(1, n):
        key = arr[i]
        assignments += 1
        low, high = 0, i
        while low < high:
            comparisons += 1
            mid = (low + high) // 2
            if arr[mid] <= key:
                low = mid + 1
            else:
                high = mid
        j = i
        while j > low:
            arr[j] = arr[j - 1]
            assignments += 1
            j -= 1
        arr[low] = key
        assignments += 1
    return arr, comparisons, assignments


class QuickSortMetrics:
    def __init__(self):
        self.comparisons = 0
        self.assignments = 0

    def quick_sort(self, arr, left, right):
        if left < right:
            pivot_index = left
            for j in range(left, right):
                self.comparisons += 1
                if arr[j] < arr[right]:
                    arr[j], arr[pivot_index] = arr[pivot_index], arr[j]
                    self.assignments += 3
                    pivot_index += 1
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            self.assignments += 3
            self.quick_sort(arr, left, pivot_index - 1)
            self.quick_sort(arr, pivot_index + 1, right)
        return arr


class MergeSortMetrics:
    def __init__(self):
        self.comparisons = 0
        self.assignments = 0

    def merge_sort(self, lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left_part = lst[:mid]
            right_part = lst[mid:]
            self.merge_sort(left_part)
            self.merge_sort(right_part)
            i = j = k = 0
            while i < len(left_part) and j < len(right_part):
                self.comparisons += 1
                if left_part[i] < right_part[j]:
                    lst[k] = left_part[i]
                    self.assignments += 1
                    i += 1
                else:
                    lst[k] = right_part[j]
                    self.assignments += 1
                    j += 1
                k += 1
            while i < len(left_part):
                lst[k] = left_part[i]
                self.assignments += 1
                i += 1
                k += 1
            while j < len(right_part):
                lst[k] = right_part[j]
                self.assignments += 1
                j += 1
                k += 1


def radix_sort(arr, length):
    comparisons = 0
    assignments = 0
    max_value = max(arr)
    exp = 1
    output = [0] * length
    while exp <= max_value:
        count = [0] * 10
        for num in arr:
            count[num // exp % 10] += 1
        total = 0
        for i in range(10):
            count[i], total = total, total + count[i]
        for num in arr:
            output[count[num // exp % 10]] = num
            assignments += 1
            count[num // exp % 10] += 1
        arr, output = output, arr
        exp *= 10
    return arr, comparisons, assignments


# === HLAVNY PROGRAM ===
n = 20000  # <-- ZMen na 20000 pre druhe meranie

print(f"Vysledky pre N={n} - kolisavo rastucie data\n")

algorithms = [
    ("Bubble Sort",                    lambda arr, size: bubble_sort(arr, size)),
    ("Selection Sort",                 lambda arr, size: selection_sort(arr, size)),
    ("Insertion Sort",                 lambda arr, size: insertion_sort(arr, size)),
    ("Insertion Sort + Binary Search", lambda arr, size: insertion_sort_with_binary_search(arr)),
    ("Quick Sort",                     None),
    ("Merge Sort",                     None),
    ("Radix Sort",                     lambda arr, size: radix_sort(arr, size)),
    ("Tree Sort",                      lambda arr, size: tree_sort(arr, size)),
]

for name, func in algorithms:
    print(name)
    print("Test | Cas(ms) | Porovnania | Priradenia")
    for run in range(1, 6):
        data = []
        current = 0
        while len(data) < n:
            inc = random.randint(1, 10)
            data.append(current + inc)
            current = data[-1]
            if len(data) < n:
                dec = random.randint(1, 5)
                data.append(current - dec)
                current = data[-1]
        data = data[:n]

        start = time.time()
        if name == "Quick Sort":
            sorter = QuickSortMetrics()
            sorter.quick_sort(data, 0, n - 1)
            comps, assigns = sorter.comparisons, sorter.assignments
        elif name == "Merge Sort":
            sorter = MergeSortMetrics()
            sorter.merge_sort(data)
            comps, assigns = sorter.comparisons, sorter.assignments
        else:
            _, comps, assigns = func(data, n)
        elapsed = (time.time() - start) * 1000
        print(f"{run} | {elapsed:.2f} | {comps} | {assigns}")
    print()

print("POZNAMKA: Data su kolisavo rastucie.\n")

"""Ejemplo simple de ordenamiento"""

def demo():
    nums = [5, 2, 9, 1, 5, 6]
    print('Original:', nums)

    nums_sorted = sorted(nums)
    print('Ordenado (built-in sorted):', nums_sorted)

    # Implementación simple de bubble sort para fines educativos
    def bubble_sort(lst):
        a = lst.copy()
        n = len(a)
        for i in range(n):
            for j in range(0, n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        return a

    print('Ordenado (bubble_sort):', bubble_sort(nums))


if __name__ == "__main__":
    demo()

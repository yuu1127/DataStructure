def BubbleSort(arr):
    size = len(arr)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    BubbleSort(arr)
    print(arr)
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        MergeSort(left)
        MergeSort(right)

        m = n = z = 0

        while m < len(left) and n < len(right):
            if left[m] <= right[n]:
                arr[z] = left[m]
                m += 1
            else:
                arr[z] = right[n]
                n += 1
            z += 1
        while m < len(left):
            arr[z] = left[m]
            m += 1
            z += 1
        while n < len(right):
            arr[z] = right[n]
            n += 1
            z += 1


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    MergeSort(arr)
    print(arr)
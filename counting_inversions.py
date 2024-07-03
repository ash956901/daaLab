#Counting Inversions
def merge(arr, start, mid, end):
    first = arr[start:mid + 1]
    second = arr[mid + 1:end + 1]

    i = 0
    j = 0
    k = start
    inversions = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            arr[k] = first[i]
            i += 1
        else:
            arr[k] = second[j]
            j += 1
            inversions += (mid - i + 1 - start)  # Count inversions
        k += 1

    while i < len(first):
        arr[k] = first[i]
        i += 1
        k += 1

    while j < len(second):
        arr[k] = second[j]
        j += 1
        k += 1

    return inversions

def merge_sort_and_count(arr, start, end):
    if start >= end:
        return 0

    mid = (start + end) // 2

    inversions = merge_sort_and_count(arr, start, mid)
    inversions += merge_sort_and_count(arr, mid + 1, end)
    inversions += merge(arr, start, mid, end)

    return inversions

if __name__ == "__main__":
    l = [10, 50, 100, 35, 45, 23, 72]
    inversion_count = merge_sort_and_count(l, 0, len(l) - 1)
    print("Sorted array:", l)
    print("Number of inversions:", inversion_count)

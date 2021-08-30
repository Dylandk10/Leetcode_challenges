
#recurse binary Search
def binarySearch(arr, low, high, target) -> int:
    if low > high:
        return -1

    mid = (high + low)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, low, mid-1, target)
    else:
        return binarySearch(arr, mid+1, high, target)


if __name__ == '__main__':
    arr = []
    for i in range(0, 100, 2):
        arr.append(i)
    result = binarySearch(arr, 0, len(arr), 14)

    if result == -1:
        print("Target not in array")
    else:
        print("Target found at index " + str(result))

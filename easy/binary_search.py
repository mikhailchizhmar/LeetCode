def binary_search(arr, val):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if val < arr[mid]:
            r = mid - 1
        elif val > arr[mid]:
            l = mid + 1
        else:
            return mid
    return -1


assert binary_search([1, 2, 3, 4, 5, 6], 6) == 5
assert binary_search([1, 2, 3, 4, 5, 6], 1) == 0
assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
assert binary_search([1, 2, 3, 4, 5], 3) == 2
assert binary_search([1], 1) == 0
assert binary_search([1, 3, 6, 7, 8, 9, 10], 2) == -1
assert binary_search([], 2) == -1

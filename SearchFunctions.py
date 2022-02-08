# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binary_search_sub(arr, l, r, x):

    # allow mid from each prev loop to persist
    mid = 0  ### new line
    while l <= r:

        mid = l + (r - l)  # 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present so return the last midpoint chosen
    return mid  ### new line was -1



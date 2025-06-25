def reverse_subarray(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_left(arr, d):
    n = len(arr)
    d %= n  # In case d > n

    if d == 0:
        return

    # Step 1: Reverse first d elements
    reverse_subarray(arr, 0, d - 1)

    # Step 2: Reverse remaining elements
    reverse_subarray(arr, d, n - 1)

    # Step 3: Reverse the entire array
    reverse_subarray(arr, 0, n - 1)

def main():
    n = int(input("Enter number of elements in the array: "))
    arr = list(map(int, input(f"Enter {n} elements separated by space: ").split()))
    d = int(input("Enter number of steps to rotate left: "))

    if len(arr) != n:
        print("Error: Number of elements doesn't match the given size.")
        return

    rotate_left(arr, d)

    print("Array after left rotation:", arr)

if __name__ == "__main__":
    main()

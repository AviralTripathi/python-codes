def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

def main():
    n = int(input("Enter number of elements in the array: "))
    arr = list(map(int, input(f"Enter {n} elements separated by space: ").split()))

    if len(arr) != n:
        print("Error: Number of elements does not match the given size.")
        return

    print("Original array:", arr)
    reversed_arr = reverse_array(arr)
    print("Reversed array:", reversed_arr)

if __name__ == "__main__":
    main()

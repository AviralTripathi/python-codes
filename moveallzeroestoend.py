def move_zeroes(arr: list[int]) -> None:
    """
    Moves all zeros in `arr` to the end in-place.
    Constraints:
    - 1 ≤ len(arr) ≤ 10**5
    - 0 ≤ arr[i] ≤ 10**5
    Time Complexity: O(n), Space: O(1)
    """
    n = len(arr)
    if n < 2:
        return

    j = 0  # next position to place a non-zero element
    for i in range(n):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    move_zeroes(arr)
    print(*arr)

def get_second_largest(arr):
    if len(arr) < 2:
        return -1
    largest = second = float('-inf')
    for n in arr:
        if n >= largest:
            if n != largest:
                second = largest
            largest = n
        elif n > second and n != largest:
            second = n
    return second if second != float('-inf') else -1

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(get_second_largest(arr))

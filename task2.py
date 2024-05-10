import random

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0 # рахує кількість ітерацій

# перевіряє введене число на придатність до вирішення задачі
    if x > arr[high]:
        return 'The task is impossible to solve'


    while low <= high:
        i += 1
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return (i, arr[mid]) # виводиться при повному співпадінні

    return (i, arr[high+1]) # виводиться у разі неспівпадіння


arr = sorted([random.uniform(0, 100) for _ in range(30)])
print(arr)
x = 15

result = binary_search(arr, x)
print(result)
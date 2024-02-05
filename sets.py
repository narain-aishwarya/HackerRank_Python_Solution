def average(array):
    # your code goes here
    a = sum(set(arr))
    b = len(set(arr))
    array = a/b
    return array

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

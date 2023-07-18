# Test cases

test = [
    {
        "input": {
            "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "num": 8,
            "start_index": 0,
            "end_index": 9
        },
        "result": 7
    },
    {
        "input": {
            "array": [123, 256, 450, 900, 1000, 1293, 9999],
            "num": 900,
            "start_index": 0,
            "end_index": 6
        },
        "result": 3
    },
    {
        "input": {
            "array": [1, 5, 12, 15, 17, 19, 22, 24, 31, 33, 37],
            "num": 22,
            "start_index": 0,
            "end_index": 10
        },
        "result": 6
    },
    {
        "input": {
            "array": [0, 1, 2, 5, 7, 9, 11, 13, 15, 17, 19],
            "num": 11,
            "start_index": 0,
            "end_index": 10
        },
        "result": 6
    },
    {
        "input": {
            "array": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
            "num": 85,
            "start_index": 0,
            "end_index": 9
        },
        "result": None
    }]


def binary_search(array, num, start_index=0, end_index=0):
    if start_index > end_index:
        return None
    mid = (start_index + end_index) // 2
    guess = array[mid]
    if guess == num:
        return mid
    elif guess > num:
        return binary_search(array, num, start_index, mid - 1)
    else:
        return binary_search(array, num, mid + 1, end_index)


case = 1
for test_case in test:
    if binary_search(**test_case["input"]) == test_case["result"]:
        print(f"case {case} --> OK")
    else:
        print(f"case {case} --> Error")
    case += 1

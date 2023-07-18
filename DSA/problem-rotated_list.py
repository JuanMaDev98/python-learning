testing = [
    {
    "input": {
        "arr": [5, 6, 9, 0, 2, 3, 4]
    },
    "output": 3
    },
    {
    "input": {
        "arr": [500, 501, 600, 800, 901, 999, 0, 1]
    },
    "output": 6
    },
    {
    "input": {
        "arr": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    "output": 0
    },
        {
    "input": {
        "arr": [0]
    },
    "output": 0
    }
]



def find_rotations(arr):
    start = 0
    end = len(arr) - 1
    
    if arr[start] <= arr[end]:
        return 0
    
    mid = 0 # Para salir del dichoso unbound error 
    number = arr[end]
    while end >= start:
        mid = (start + end) // 2
        mid_index = (start + end) // 2
        
        if arr[mid] < number:
            end = mid - 1
        elif arr[mid] > number:
            start = mid + 1
            number = arr[mid]
            if number > arr[start]:
                return mid + 1
    return mid + 1


case = 1
for test_cases in testing:
    if find_rotations(**test_cases["input"]) == test_cases["output"]:
        print(f"Case{case} --> Passed")
    else:
        print(f"Case{case} --> Error")
    case += 1













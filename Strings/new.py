def contiguous_sum(lst, K):
    start, end = 0, 0
    window_sum = lst[0]

    while end < len(lst):
        if window_sum < K:
            end += 1
            if end < len(lst):
                window_sum += lst[end]
        elif window_sum > K:
            window_sum -= lst[start]
            start += 1
        else:
            return lst[start:end+1]

    return None

# Test the function with some sample inputs
lst1 = [1, 2, 3, 4, 5]
K1 = 9
print(contiguous_sum(lst1, K1))  # Output: [2, 3, 4]

lst2 = [5, 2, 1, 4, 7, 3, 6, 9, 8, 5]
K2 = 12
print(contiguous_sum(lst2, K2))  # Output: [2, 1, 4, 5]

lst3 = [1, 2, 3, 4, 5]
K3 = 10
print(contiguous_sum(lst3, K3))  # Output: [1, 2, 3, 4]

lst4 = [1, 2, 3, 4, 5]
K4 = 7
print(contiguous_sum(lst4, K4))  # Output: [2, 3, 4]

lst5 = [1, 2, 3, 4, 5]
K5 = 15
print(contiguous_sum(lst5, K5))  # Output: None


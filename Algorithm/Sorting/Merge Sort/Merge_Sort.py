def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(list):
    if (len(list) <= 1):
        return list
    mid = int(len(list) / 2)
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge(left, right)


arr = [8, 2, 6, 4]
print(merge_sort(arr))

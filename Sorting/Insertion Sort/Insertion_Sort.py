def insertion_sort(list):
    for i in range(1, len(list)):
        value = list[i]
        j = i-1
        while j >= 0:
            if value < list[j]:
                list[j+1] = list[j]
                list[j] = value
                j = j-1
            else:
                break
    return list


list = [12, 11, 13, 5, 6]
print(insertion_sort(list))
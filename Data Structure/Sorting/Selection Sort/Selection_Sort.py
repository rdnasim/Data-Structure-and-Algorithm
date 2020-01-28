def selection_sort(list):
    for i in range(0, len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        if min !=i:
            list[i], list[min] = list[min], list[i]
    return list

list = [64, 25, 12, 22, 11]
print(selection_sort(list))
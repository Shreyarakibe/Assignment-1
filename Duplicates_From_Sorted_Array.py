def remove_duplicates(sorted_array):
    if not sorted_array:
        return []

    final_array = [sorted_array[0]]

    for i in range(1, len(sorted_array)):
        if sorted_array[i] != sorted_array[i - 1]:
            final_array.append(sorted_array[i])

    return final_array

sorted_array = [1, 1, 6, 6, 3, 9, 9, 5]
final_array = remove_duplicates(sorted_array)
print("Array after removing duplicates:", final_array)

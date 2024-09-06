arr1 = [23,89,7,56,44]
for i in range (len(arr1)):
    for j in range (0, len(arr1) - i - 1):
        if arr1[j] > arr1[j + 1]:
            arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
print ("arr1 Bubble Sort Ascending")
print(arr1)
print("=======================================")
arr2 = [12,78,91,34,62]
for i in range (1,len(arr2)):
    key = arr2[i]
    j = i-1
    while j >= 0 and key < arr2[j]:
        arr2[ j+1 ] = arr2[j]
        j-=1
    arr2[j + 1] = key
print("arr2 InsertionSort : Ascending")
print(arr2)
print("=======================================")
arr3 = [5,99,48,15,67]
for i in range(len(arr3)):
    min_idx = i
    for j in range(i + 1, len(arr3)):
        if arr3[min_idx] < arr3[j]:
            min_idx = j
    arr3[i],arr3[min_idx] = arr3[min_idx], arr3[i]
print("arr3 as Selection Sort : Descending")
print(arr3)
print("=======================================")
arr4 = [38,82,25,74,13]
for i in range (1,len(arr4)):
    key = arr4[i]
    j = i-1
    while j >= 0 and key > arr4[j]:
        arr4[ j+1 ] = arr4[j]
        j-=1
    arr4[j + 1] = key
print("arr4 Insertion Sort : Descending")
print(arr4)
print("=======================================")
arr5 = [44,56,62,78,48,15,38,25]
for i in range (1,len(arr5)):
    key = arr5[i]
    j = i-1
    while j >= 0 and key < arr5[j]:
        arr5[ j+1 ] = arr5[j]
        j-=1
    arr5[j + 1] = key
print("arr5 Insertion Sort : Ascending")
print(arr5)
print("=======================================")

arr6 = [44,56,62,78,48,15,38,25]
for i in range (1,len(arr6)):
    key = arr6[i]
    j = i-1
    while j >= 0 and key > arr6[j]:
        arr6[ j+1 ] = arr6[j]
        j-=1
    arr6[j + 1] = key
print("arr6 Insertion Sort : Descending")
print(arr6)
print("=======================================")
arr7 = [23,89,7,56,44,12,78,91,34,62,5,99,48,15,67,38,82,25,74,13]
for i in range(len(arr7)):
    min_idx = i
    for j in range(i + 1, len(arr7)):
        if arr7[min_idx] > arr7[j]:
            min_idx = j
    arr7[i],arr7[min_idx] = arr7[min_idx], arr7[i]
print("Arr7 values after Selection Sort : Ascending")
print(arr7)


even = [num for num in arr7 if num %2 ==0]
odd = [num for num in arr7 if num %2 != 0]
print("=======================================")
print("Even Values")
print(even)
print("=======================================")
print("Odd Values")
print(odd)
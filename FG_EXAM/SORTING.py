arr1 = [1,2,21,33,45,65,12]
print(arr1)
print("arr1 InsertionSort : Descending Order")
for i in range (1,len(arr1)):
    min_idx = arr1[i]
    j = i-1
    while j >= 0 and min_idx > arr1[j]:
        arr1[ j+1 ] = arr1[j]
        j-=1
    arr1[j + 1] = min_idx
print(arr1)
print("arr2 Selection Sort :: ASCENDING")
for i in range(len(arr1)):
    min_idx = i
    for j in range(i + 1, len(arr1)):
        if arr1[min_idx] > arr1[j]:
            min_idx = j
    arr1[i],arr1[min_idx] = arr1[min_idx], arr1[i]
print(arr1)


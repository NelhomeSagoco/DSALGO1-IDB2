arr1=[10,2,3,1,1,4,89,21]
#PRINTING the values arr1
print()

print(arr1)
for i in range (1,len(arr1)):
    key = arr1[i]
    j = i-1
    #move element of arr1[0..i-1]
    #that are greater than the key
    #to one poition ahgead of
    #their current position
    while j >= 0 and key > arr1[j]:
        arr1[ j+1 ] = arr1[j]
        j-=1
    arr1[j + 1] = key
print(arr1)
#selection sort
arr2 = [10,2,3,1,1,4,89,21]
#printing the values of arr2 before sorting
print("Arr2 before selection sort:")
print(arr2)
for i in range(len(arr2)):
    min_idx = i
    for j in range(i + 1, len(arr2)):
        if arr2[min_idx] > arr2[j]:
            min_idx = j
        #swapping the values from our array
    arr2[i],arr2[min_idx] = arr2[min_idx], arr2[i]
print("Arr2 values after Selection Sort")
print(arr2)
#Bubble Sort
arr3 = [10,2,3,1,1,4,89,21]
print("Arr3 values before Bubble Sort")
print(arr3)
for i in range (len(arr3)):
    for j in range (0, len(arr3) - i - 1):
        if arr3[j] > arr3[j + 1]:
            arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
print("Arr3 values before Bubble Sort")
print(arr3)

def bubblesort(array):
    for i in range (len(array)):
        for j in range (0, len(array)-i-1):
            if array[j]>array[j+1]:
                t=array[j]
                array[j]=array[j+1]
                array[j+1]=t
data = [7, 10, 12, 9, 1, 5 ]
bubblesort(data)
print("sıralı dizi:")
print(data)


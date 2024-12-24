# Merge two sorted array's
# arr1 = [0, 3, 4, 31]
# arr2 = [4, 6, 30]

def merge (arr1, arr2) : 
    if len(arr1) == 0 or len(arr2) == 0 :
        return arr1 + arr2
    i=0
    j=0
    
    mergedArray = []
    while i < len(arr1) and j < len(arr2) :
        if(arr1[i] <= arr2[j]) :
            mergedArray.append(arr1[i])
            i = i+1
        elif (arr1[i] >= arr2[j]):
            mergedArray.append(arr2[j])
            j = j+1
    
    print(mergedArray + arr1[i:] + arr2[j:])


merge([10], [5,6,7,8])
        


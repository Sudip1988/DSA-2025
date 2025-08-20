from typing import List
def merge_sort(nums :List[int] ) -> List[int] :

    if len(nums) == 1 :
        return nums
    mid = len(nums) // 2

    l = nums[mid:]
    r = nums[:mid]
    print(l)
    print(r)
    l = merge_sort(l)
    r = merge_sort(r)
    print(l)
    print(r)
    return merge(l, r)

def merge(l, r) -> List[int] :
    i = 0
    j = 0
    result = []
    while i < len(l) and j < len(r) :
        if l[i] < r[j] :
            result.append(l[i])
            i += 1
        else :
            result.append(r[j])
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    print(result)
    return result


merge_sort([10,8,4,2])
            

def merge_sort(numbers):
    if len(numbers)<=1:
        return numbers
    middle = len(numbers)//2

    left=numbers[ :middle]
    right= numbers[middle: ]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result=[]
    i=0
    j=0

    while i<len(left) and j< len(right):
        if left[i]<right[j] :
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right) :
        result.append(right[j])
        j+=1

    return result

numbers = [7,4,9,2,5]
print ("Before :",numbers)
print(merge_sort(numbers))
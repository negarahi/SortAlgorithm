numbers = [7,4,9,2,5]
def insertion_sort(numbers):
    
    for i in range(1 , len(numbers)):
     current=numbers[i]
     j= i-1
     while j>=0 and numbers[j]>current :
            numbers[j+1]=numbers[j]
            j-=1
    numbers[j+1] = current
    return numbers
print(insertion_sort(numbers))
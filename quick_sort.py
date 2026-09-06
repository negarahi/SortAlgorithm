def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]

    left = []
    right = []

    for number in numbers[:-1]:
        if number < pivot:
            left.append(number)
        else:
            right.append(number)

    left = quick_sort(left)
    right = quick_sort(right)

    return left + [pivot] + right


numbers = [7,4,9,2,5]

print("Before:", numbers)
print(quick_sort(numbers))
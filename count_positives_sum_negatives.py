def count_positives_sum_negatives(arr):
    # 1. Check if the array is empty or None
    # If it's empty, we stop immediately and return []
    if not arr:
        return []
    
    # 2. Set up your two trackers starting at 0
    count_positives = 0
    sum_negatives = 0

    # 3. Use a loop to look at each number one-by-one
    for num in arr:
        if num > 0:
            # If the number is greater than 0, add 1 to our count
            count_positives += 1
        elif num < 0:
            # If the number is less than 0, add its value to our sum
            sum_negatives += num

    # 4. Return the final answer as a list containing both trackers
    return [count_positives, sum_negatives]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# Output will be: [10, -65] (because there are 10 positive numbers and the sum of negative numbers is -65)
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
# Output will be: [8, -50] (because there are 8 positive numbers and the sum of negative numbers is -50)
print(count_positives_sum_negatives([1]))
# Output will be: [1, 0] (because there is 1 positive number and 0 negative numbers)
print(count_positives_sum_negatives([-1]))
# Output will be: [0, -1] (because there are 0 positive numbers and the sum of negative numbers is -1)
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]))
# Output will be: [0, 0] (because there are 0 positive numbers and the sum of negative numbers is 0)
print(count_positives_sum_negatives([]))
# Output will be: [] (because the array is empty)
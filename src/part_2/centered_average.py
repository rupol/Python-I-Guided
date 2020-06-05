# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

def centered_average(nums):
  # find the max number of nums
  max_num = max(nums)
  # find the min number
  min_num = min(nums)
  # get the sum of nums
  current_sum = sum(nums)
  # subtract the max and min
  final_sum = current_sum - max_num - min_num
  # divide the value by len(nums)/2
  return final_sum // (len(nums) - 2) ## // chops off the decimals - floor

print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
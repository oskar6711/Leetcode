def remove_duplicates(nums):

    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i)
            nums.extend('_')
        i += 1

    k = 0
    while str(nums[k]).isdigit():
        k += 1

    return k



x = [1, 1, 2, 2, 3]
print(remove_duplicates(x))

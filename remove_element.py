def remove_element(nums: list[int], val: int):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            nums.extend('_')
        else:
            i += 1
    k = 0

    for i in range(len(nums)):
        if str(nums[i]).isdigit():
            k += 1
    return k


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
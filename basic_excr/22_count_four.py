# Write a Python program to count the number 4 in a given list.


def count_four(nums: list[int]) -> int:
    c = 0
    for i in nums:
        if i == 4:
            c = c + 1
    return c


nums_list = [1, 4, 6, 4, 7, 4, 4, 4]
res = count_four(nums=nums_list)
print(res)

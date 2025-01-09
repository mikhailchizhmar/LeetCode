# https://leetcode.com/problems/move-zeroes

def move_zeroes(nums):
    cnt = 0
    new_nums = []
    for n in nums:
        if n != 0:
            new_nums.append(n)
        else:
            cnt += 1

    new_nums.extend([0] * cnt)
    nums = new_nums.copy()
    # print(nums)


def moveZeroes(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    while count < n:
        nums[count] = 0
        count += 1


moveZeroes([0, 1, 0, 3, 12])
# assert move_zeroes([0,1,0,3,12]) == [1,3,12,0,0]

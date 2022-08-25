import time
import random

"""
new_list erstellen
for loob mit nums
guck ob Anfang oder Ende passt
so lange nach rechts gehn bis es links kleiner/gleich und rechts größer ist
"""


def quicksort(nums: list):
    def partion(nums):
        end = len(nums) - 1
        l, r = 0, end - 1
        while r > l:
            if nums[l] < nums[end]:
                l += 1
            elif nums[r] > nums[end]:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
        assert l == r
        if nums[r] > nums[end]:
            nums[l], nums[end] = nums[end], nums[l]
            return r
        return end

    if len(nums) in [0, 1]:
        return nums

    pivot = partion(nums)
    print(nums, nums[pivot])


if __name__ == "__main__":
    tests = []
    tests.append({"input": {"nums": [1, 2, 3, 4, 5, 6]}, "output": [1, 2, 3, 4, 5, 6]})
    tests.append({"input": {"nums": []}, "output": []})
    tests.append({"input": {"nums": [1]}, "output": [1]})
    tests.append({"input": {"nums": [3, 1, 2, 5, 4, 6]}, "output": [1, 2, 3, 4, 5, 6]})
    tests.append(
        {"input": {"nums": [3, -1, -2, 5, 1, 4, 6]}, "output": [-1, -2, 1, 3, 4, 5, 6]}
    )
    tests.append(
        {
            "input": {"nums": [8, 0, 1, 7, 4, 13, 6, 12, 9, 3, 10, 5, 11, 2, 14]},
            "output": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        }
    )
    tests.append(
        {"input": {"nums": [3, 1, 2, 5, 4, 4, 6]}, "output": [1, 2, 3, 4, 4, 5, 6]}
    )
    tests.append(
        {
            "input": {"nums": [2, 13, 10, 0, 7, 14, 4, 9, 6, 3, 12, 11, 8, 1, 5]},
            "output": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        }
    )

    # x = 10000
    # list1 = list(range(x))
    # list2 = list(range(x))
    # random.shuffle(list2)
    # tests.append({"input": {"nums": list2}, "output": list1})
    # pass
    for test in tests:
        start_time = time.time()
        output = quicksort(test["input"]["nums"])
        # print(output == test["output"], end="")
        # print(f" output: {output}", end="")
        # print(f" dauer: {time.time()-start_time}")

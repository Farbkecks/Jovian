import time
import random

"""
new_list erstellen
for loob mit nums
guck ob Anfang oder Ende passt
so lange nach rechts gehn bis es links kleiner/gleich und rechts größer ist
"""


def sort_linear(nums: list) -> list:
    def insert(num: int):
        if not list:
            list.append(num)
            return
        if list[0] >= num:
            list.insert(0, num)
            return
        if list[-1] < num:
            list.append(num)
            return
        i = 0
        while not list[i] <= num or not list[i + 1] > num:
            i += 1
        list.insert(i + 1, num)
        pass

    list = []
    for num in nums:
        insert(num)
    return list


if __name__ == "__main__":
    tests = []
    tests.append({"input": {"nums": [1, 2, 3, 4, 5, 6]}, "output": [1, 2, 3, 4, 5, 6]})
    tests.append({"input": {"nums": []}, "output": []})
    tests.append({"input": {"nums": [1]}, "output": [1]})
    tests.append({"input": {"nums": [3, 1, 2, 5, 4, 6]}, "output": [1, 2, 3, 4, 5, 6]})
    tests.append(
        {"input": {"nums": [3, 1, 2, 5, 4, 4, 6]}, "output": [1, 2, 3, 4, 4, 5, 6]}
    )
    tests.append(
        {
            "input": {"nums": [2, 13, 10, 0, 7, 14, 4, 9, 6, 3, 12, 11, 8, 1, 5]},
            "output": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        }
    )
    x = 10000
    list1 = list(range(x))
    list2 = list(range(x))
    random.shuffle(list2)
    tests.append({"input": {"nums": list2}, "output": list1})
    pass
    for test in tests:
        start_time = time.time()
        output = sort_linear(test["input"]["nums"])
        print(output == test["output"], end="")
        # print(f" output: {output}", end="")
        print(f" dauer: {time.time()-start_time}")

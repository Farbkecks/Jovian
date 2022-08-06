"""
Problem:
Es gibt einen Input list aus int. Diese waren in einer aufsteigenden sortierten Liste. 
Die aufgabe ist es raus zufinden wie oft ich die Liste Rotieren musste um die aktuelle Liste zu bekommen.
Rotieren heißt hier das letzte Elemtnt nach vorne verschieben.

Input:
[int, int,...]
[5, 6, 9, 0, 2, 3, 4]
Output:
3

Solution:
Brute Force 1 :
1. liste Sortieren gucken ob sie sich ändert wenn nein diese zurückgeben
2. letztes Elemtnt nach vorne, counter +1

Brute Force 2 :
1. durch die liste durchgehn index finden wenn die gegebene zahl größer als die Zahl rechts von ihr ist.

"""


def count_rotations(nums: list) -> int:
    index = 0
    if len(nums) == 0:
        return -1
    while index < len(nums) - 1 and len(nums) > 1:
        if nums[index] > nums[index + 1]:
            return index + 1
        index += 1
    return 0


tests = []
tests.append({"input": {"nums": [6, 1, 2, 3, 4, 5]}, "output": 1})
tests.append({"input": {"nums": [5, 6, 9, 0, 2, 3, 4]}, "output": 3})
tests.append({"input": {"nums": [0, 2, 3, 4]}, "output": 0})
tests.append({"input": {"nums": [20, 24, 25, 30, 1]}, "output": 4})
tests.append({"input": {"nums": []}, "output": -1})
tests.append({"input": {"nums": [1]}, "output": 0})


test_count = 1
for test in tests:
    print(f"Test {test_count}: ", end="")
    test_count += 1
    output = count_rotations(**test["input"])
    print(f" output: {output} ", end="")
    print(output == test["output"])
